#!/usr/bin/env python
"""
Uses the 'click' package.
Installing click:
'pip install click'
"""

import click


@click.group()
def _g():
    pass

@_g.command()
def command1():
    click.echo('Executing command1')

@_g.command()
def command2():
    click.echo('Executing command2')

if __name__ == "__main__":
    _g()
