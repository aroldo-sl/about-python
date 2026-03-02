#!/usr/bin/env python
"""
Simple usage of the 'click' package.
"""
import click

@click.command()
@click.option("-t","--tomlfile", default = "packages.toml", nargs=1, help = "The toml file with deb package names.")
@click.option("-s", "--section", help = "The section titles.")
def info(tomlfile, section):
    """
    Info about the toml file and the selected sections.
    """
    click.echo(f"Processing {tomlfile}")
    click.echo(f"section: {section}")
    

if __name__=='__main__':
    info()
