import logging
import os
from os import getenv
from pathlib import Path

from pymail import __version__
from pymail.core import do_bulk, do_read, do_send
from pymail.utils import contacts_from_file, prepare_message

logging.basicConfig(level=logging.DEBUG)

examples = Path('tests/examples')

with open('secrets/pymail/.env', 'r') as f:
    test_env = dict(s.split('=') for s in f.read().strip().split())

message = examples.joinpath('message.txt').read_text()
msg = prepare_message(
    to_addrs=contacts_from_file(examples / 'contacts.csv'),
    message=message,
    from_addr=os.getenv('USERNAME'),
    attachments=None,
    headers={'SUBJECT': f'Testing pymail version {__version__}.'})


def test_do_send(msg=msg,
                 port=test_env['MAIL_PORT'],
                 host=test_env['MAIL_HOST'],
                 username=test_env['MAIL_USERNAME'],
                 password=test_env['MAIL_PASSWORD']):
    results = do_send(**locals())
    assert results is not None
