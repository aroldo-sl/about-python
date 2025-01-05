#!/usr/bin/env python
from .. import make_slog
import logging
__level__ = logging.DEBUG 
_slog = make_slog(level = __level__)

def rubbish():
    x = 666
    _slog.info(f"Guten Tag {x}!")
    return x

def garbage():
    x = "Beelzebub"
    _slog.info(f"Guten Tag {x}!")
    return x

def test_slog_in_rubbish():
    """
    Tests if a simple log object
    works in the rubbish function
    namespace.
    """
    x = rubbish()
    assert x == 666 

def test_slog_in_garbage():
    """
    Tests if a simple log object
    works in the garbage function
    namespace.
    """
    x = garbage()
    assert x == 666, "Beelzebub or 666?" 
