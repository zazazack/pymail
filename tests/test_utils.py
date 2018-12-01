import logging
from csv import DictReader
from glob import glob
from os import getenv
from pathlib import Path

from pymail.utils import (contacts_from_file, get_config, parse_contacts,
                          prepare_attachments, prepare_message)

logging.basicConfig(level=logging.DEBUG)

examples = Path('tests/examples')

with open('secrets/pymail/.env', 'r') as f:
    test_env = dict(s.split('=') for s in f.read().strip().split())

message = examples.joinpath('message.txt').read_text()


def test_prepare_attachments(
        attachments=[examples / 'attachment.txt']) -> tuple:
    results = prepare_attachments(attachments)
    logging.debug(results)
    assert results is not None


def test_prepare_message(
        to_addrs=contacts_from_file(examples / 'contacts.csv'),
        from_addr=getenv('USERNAME'),
        message=message,
        attachments=None,
        headers=None):
    results = prepare_message(
        to_addrs=to_addrs,
        from_addr=from_addr,
        message=message,
        attachments=attachments,
        headers=headers)
    assert results is not None


def test_contacts_from_file(path=examples / 'contacts.csv'):
    results = contacts_from_file(path)
    assert results is not None


def test_get_config():
    retcode = get_config()
    logging.debug(retcode)
    assert retcode == 0
