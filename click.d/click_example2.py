#!/usr/bin/env python
"""
Uses the 'click' package.
Installing click:
"""

from asl._lib import click as _click


@_click.group()
def main():
    pass

@main.command()
def command1():
    _click.echo('Executing command1')

@main.command()
def command2():
    _click.echo('Executing command2')

if __name__ == "__main__":
    main()
