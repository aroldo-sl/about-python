#!/usr/bin/env python
"""
Usage examples of 'argparse'.
"""
import sys, logging, pathlib, argparse
__level__ = logging.DEBUG

## #<slog>
def _make_slog():
    try:
        from asl.utils import make_slog
        slog = make_slog()
    except ImportError:
        logging.basicConfig()
        from uuid import uuid4
        slog_name = __name__ + uuid4().hex[:6]
        slog = logging.getLogger(_slog_name)
    slog.setLevel(__level__)
    return slog 
_slog = _make_slog()
## #</slog>
_slog.debug("BEGIN " + sys.argv[0])

## # <parse-arguments>
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
## # </parse-arguments>

class BatchLine(str):
    def __init__(self, *p, **kw):
        str.__init__(self, *p, **kw)

def test_BatchLine_instance():
    _slog.debug("Testing instantiation.")
    line = BatchLine()
    assert isinstance(line, BatchLine)

if __name__ == "__main__":
    test_BatchLine_instance()


