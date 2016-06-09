# -*- encoding: utf-8 -*-
"""
Redmon command line tool
"""

import click

from redmon import Redmon

# Disable the warning that Click displays (as of Click version 5.0) when users
# use unicode_literals in Python 2.
# See http://click.pocoo.org/dev/python3/#unicode-literals for more details.
click.disable_unicode_literals_warning = True

@click.group()
def main():
    """Redmon command line tool."""
    pass

@main.command()
@click.option('--key', '-k', help='Redis key to be watched')
@click.option('--trueval', '-t', default=None, help='Value that Redis key will be compared against')
@click.option('--interval', '-i', default=None, help='Refresh interval in seconds')
def monitor(key, trueval=None, interval=None):
    """Watching Redis for key."""
    redmon = Redmon(key=key, trueval=trueval, interval=interval)
    redmon.monitor()
