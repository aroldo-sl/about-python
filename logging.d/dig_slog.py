#!/usr/bin/env python
"""
Digging a simple method for logging
in Python.
"""
import sys, uuid, logging # for _make_slog
__level__ = logging.DEBUG

def _make_slog(stream = sys.stderr):
    """
    Constructor for a simple unique logger.
    Each call of this function returns a logger with a
    unique name, that is, a Logger object different from loggers
    instantiated through preceding calls of the same function.
    """
    
    # ## <formatter>
    fmt_str = """%(levelname)s|logger:%(name)s|line number:%(lineno)s|namespace:%(funcName)s
    %(message)s"""
    formatter = logging.Formatter(fmt = fmt_str) # fmt -> a format string
    # ## </formatter>

    # ## <handler>
    handler = logging.StreamHandler(stream = stream)
    handler.setFormatter(fmt = formatter) # fmt -> a Formatter object
    # ## </handler>

    # ## <slog>
    slog_name = uuid.uuid4().hex[:6]
    slog = logging.getLogger(slog_name)
    slog.addHandler(handler)
    slog.setLevel(__level__)
    # ## </slog>
    
    return slog

_slog = _make_slog()

class Nothing:
    def __init__(self):
        _slog.info("Created a nothing object.")
    _slog.info("Created a nothing class")

def rubbish():
    nogthing = Nothing()
    _slog.debug("Just plain rubbish.")
    pass

rubbish()
_slog.warning("Nicht schlimm.")
