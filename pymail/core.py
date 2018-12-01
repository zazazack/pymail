import logging
import os
from email.message import EmailMessage
from smtplib import SMTP, SMTP_SSL, SMTPAuthenticationError

from .utils import get_config

logging.basicConfig(level=logging.DEBUG)


def do_startproject(path: str):
    return NotImplemented


def do_send(msg: EmailMessage,
            host: str = 'localhost',
            port: int = 25,
            username: str = None,
            password: str = None):

    logging.debug(f"Connecting to {host}")
    if password and username:
        server = SMTP_SSL
    else:
        server = SMTP
    with server(host=host) as smtp:
        logging.debug(f"Succesfully connected to {host}.")
        smtp.set_debuglevel(1)
        try:
            logging.debug(f"Logging in to {host} as {username}")
            smtp.login(username, password)
        except SMTPAuthenticationError as e:
            logging.debug(e)
        logging.debug(f"Sending {msg} as {msg['FROM']} to {msg['TO']}.")
        return smtp.send_message(msg)
    smtp.close()


def do_read():
    return NotImplemented


def do_bulk():
    return NotImplemented
