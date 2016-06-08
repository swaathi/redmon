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
@click.option('--key', help='Redis key to be watched')
def monitor(key):
    """Watching Redis for key."""
    redmon = Redmon()
    redmon.monitor(key)
