import cli

from ..config import PASSWORD, USER_EMAIL


@click.group()
def cli():
    pass


@cli.command()
def search(options):
    return NotImplemented


@cli.command()
@cli.argument('set')
@cli.argument('get')
def config(set):
    return NotImplemented


@cli.command()
@cli.option('--lines', default=5, help='lines')
def head(lines):
    return NotImplemented


@cli.command()
@cli.option('--lines', default=5, help='lines')
def tail(lines):
    return NotImplemented


@cli.command()
@cli.argument('from')
@cli.argument('to')
@cli.argument('message')
@cli.option('--subject', default=None)
@cli.option('--carbon-copy', default=None)
@cli.option('--blind-carbon-copy', default=None)
def send(options):
    return NotImplemented
