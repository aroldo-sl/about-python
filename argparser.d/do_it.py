#!/usr/bin/env python
"""
Usage examples of 'argparse'.
"""
import sys
import argparse
from pathlib import Path
_this_script_path = Path(sys.argv[0]).resolve()

#
parser = argparse.ArgumentParser(description = """
    This script reads each line of the batch file and
    interprets each line  as the name of one package to be installed.
    """)
parser.add_argument(
    "-f",
    "--file",
    metavar = "BATCH_FILE",
    type = str,
    dest = "batch_file",
    default = "packages-input.list",
    help = "One argument per line.",
)
args = parser.parse_args()
if len(sys.argv) == 1:
    exit(parser.print_help())
print(args)

if __name__ == "__main__":
    print(f"Calling {_this_script_path}")
    print()



