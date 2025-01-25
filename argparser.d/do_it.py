#!/usr/bin/env python
"""
Usage examples of 'argparse'.
"""
import sys, logging, pathlib
import argparse
__level__ = logging.DEBUG
logging.basicConfig()
_slog = logging.getLogger()
_slog.setLevel(__level__)
_script_path = pathlib.Path(sys.argv[0]).resolve()
_script_name = _script_path.with_suffix("").name 
msg = f"\nSCRIPT: {_script_name}\n"
_slog.debug(msg)

#
parser = argparse.ArgumentParser(description = """
    This script reads each line of the batch file and
    interprets each line  as the name of one package to be installed.
    """)
parser.add_argument(
    "-c",
    "--command",
    metavar = "COMMAND",
    type = str,
    dest = "command",
    default = "echo",
    help = "One argument per line.",
)
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

if __name__ == "__main__":
    print(args.batch_file)
    print()



