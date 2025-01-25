#!/usr/bin/env python
"""
Usage examples of 'argparse'.
"""
from argparse import ArgumentParser
import sys
_this_script = sys.argv[0]
print("Number or arguments:{nargs}".format(nargs = len(sys.argv)))
parser = ArgumentParser(description = """
    This script reads each line of the package list and
    interprets is as the0 name of a package to be installed.
    """)
parser.add_argument(
    "-f",
    "--file",
    type = str,
    dest = "packages_input_list",
    default = "packages-input.list",
    help = "File containing a list of names of packages to be installed.",
)
args = parser.parse_args()
if len(sys.argv) == 1:
    exit(parser.print_help())
print(args)
print(f"END of {_this_script}")



