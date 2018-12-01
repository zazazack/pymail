import logging
import sys

import click_completion
from click import argument, echo, group, option, pass_context, version_option
from click_didyoumean import DYMCommandCollection
from gooey import Gooey

from ..__about__ import __version__

click_completion.init()


@group()
@option('--debug', '-d', is_flag=True, default=False)
@version_option(version=__version__)
@pass_context
@Gooey
def cli(context, debug: bool):
    context.ensure_object(dict)
    context.obj['DEBUG'] = debug
    if debug:
        logging.basicConfig(level=logging.DEBUG)


@cli.command()
@argument('to_addrs', type=str, nargs=-1)
@argument('message', type=str)
@option('--attachments', '-a', type=list, nargs=+1, default=None)
@option('--dry-run/--no-dry-run', '-d', is_flag=True, default=False)
@option('--from_addr', '-f', type=str, default=None)
@option('--headers', type=dict, nargs=+1, default=None)
@option('--host', '-h', type=str, default='localhost')
@option('--password', '-p', type=str, default=None)
@option('--port', type=int, default=25)
@option('--username', '-u', type=str, default=None)
@pass_context
def send(context, dry_run, to_addrs, message, from_addr, attachments, host,
         port, headers, username, password):
    echo(f"Debug is {context.obj['DEBUG'] and 'on' or 'off'}")

    if context.obj['DEBUG']:
        dry_run = True

    echo(f"Dry run is {dry_run and 'enabled' or 'disabled'}")
    from ..utils import prepare_message
    from ..core import do_send
    msg = prepare_message(
        to_addrs=to_addrs,
        message=message,
        from_addr=from_addr,
        attachments=attachments,
        headers=headers)
    if dry_run:
        echo(
            f"Message prepared for transmitall from {msg['FROM']} to {msg['TO']}."
        )
        echo(f"This message will NOT be sent.")
        return
    else:
        retcode = do_send(
            msg, host=host, port=port, username=username, password=password)
        echo(f"Message: {msg}\nSuccesfully sent.")
        return retcode


@cli.command()
@pass_context
@option('--path', '-p', type=str, default='.')
def startproject(path: str):
    from ..core import do_startproject
    retcode = do_startproject(path)
    return retcode


if "-" not in "".join(sys.argv) and len(sys.argv) > 1:
    cli = DYMCommandCollection(sources=[cli])
if __name__ == "__main__":
    cli()
