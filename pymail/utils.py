import logging
import mimetypes
import os
from configparser import ConfigParser
from csv import DictReader
from email.headerregistry import Address
from email.message import EmailMessage
from email.policy import SMTP
from pathlib import Path


def prepare_attachments(attachments: list):
    for path in attachments:
        if not os.path.isfile(path):
            continue
        ctype, encoding = mimetypes.guess_type(path)
        if ctype is None or encoding is not None:
            # no guess, use a generic bytes object
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        with open(path, 'rb') as f:
            yield f.read(), maintype, subtype, os.path.basename(path)


def prepare_message(to_addrs: list, message: str, from_addr: str,
                    attachments: list, headers: dict) -> EmailMessage:
    logging.debug(f"Creating EmailMessage from {locals()}.")
    msg = EmailMessage(policy=SMTP)
    if from_addr is None:
        try:
            from_addr = get_config()['smtp']['username']
        except Exception as e:
            logging.error(e)
            from_addr = os.getenv('MAIL_USERNAME')
        except Exception as e:
            logging.error(e)
            print("Please provide a valid --from_addr.")

    msg['FROM'] = from_addr
    msg['TO'] = to_addrs
    msg.set_content(message)
    if headers:
        for k, v in headers.items():
            try:
                msg.add_header(k, v)
            except ValueError as e:
                logging.error(e)
                msg[k] = v
    if attachments:
        for a in prepare_attachments(attachments):
            msg.add_attachment(*a)
    logging.debug(f"Message {message} created.")
    return msg


def parse_contacts(contacts: dict) -> Address:
    for contact in contacts:
        logging.debug(f"Parsing {contact}")
        username, domain = contact['email'].split('@')
        yield Address(
            display_name=contact['display_name'],
            username=username,
            domain=domain)


def contacts_from_file(path):
    with open(path, 'r') as f:
        reader = DictReader(f, f.readline().strip().split(','))
        data = []
        for row in reader:
            data.append(row)
        logging.debug(data)
        return list(parse_contacts(data))
    f.close()


def message_from_file(path):
    with open(path) as f:
        return f.read().strip()


def get_config():
    here = Path(__file__).absolute()
    logging.debug(
        f'Recursively searching {here.parent} for configuration files.')
    files = list(here.parent.glob('**/pymail.cfg'))
    logging.debug(f"Found {len(files)}:\n{files}")
    config = ConfigParser()
    config.read(files)
    return config
