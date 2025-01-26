#!/usr/bin/env python
"""
Usage examples of 'argparse'.
"""
import sys, logging, pathlib, argparse, pprint, uuid
__level__ = logging.DEBUG

## #<slog>
def _make_slog(prefix = __name__, level = None):
    """
    Returns a simpler logger.
    The logger name is unique to the current module.
    Requires the 'logging' module 
    """
    import logging, uuid
    if level is none:
        try:
            level = __level__
        except NameError:
            level = logging.DEBUG
    random_string = uuid.uuid4().hex[:6]
    slog_name = f"{prefix}-{random_string}"
    logging.basicConfig()
    slog = logging.getLogger(slog_name)
    slog.setLevel(level)
    return slog 
_slog = _make_slog()
## #</slog>

## # <cli-parser-config>
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
    help = "Command to be called on the batch file lines.",
)
parser.add_argument(
    "-f",
    "--file",
    metavar = "BATCH_FILE",
    type = str,
    dest = "batch_file",
    default = "batch-file.txt",
    help = "One argument per line in the batch file..",
)
# # </cli-parser-config>

#
def batch_processing(batch_file = None, command = None):

    """
    Apply command to each line of batch_file.
    """
    if command is None:
        pass
    if batch_file is None:
        pass

#   
def test_parse_args():
    _slog.debug("\n Testing argparse args.")
    args = parser.parse_args(["-c","echo", "-f","batch-file.txt"])
    assert args.command == "echo"
    assert args.batch_file == "batch-file.txt"

#
def main(cli_options  = None):
    """
    Called with the script's cli options as args.
    """
    if cli_options is None:
        cli_options = sys.argv[1:]
    msg = pprint.pformat(cli_options)
    _slog.debug(f'\n cli options:{msg}')

#
def test_main():
    cli_options = ["-c", "echo", "-f", "batch-file.txt"]
    main(cli_options)
    pass

#   
if __name__ == "__main__":
    main()
