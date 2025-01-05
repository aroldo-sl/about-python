#!/usr/bin/env python
from asl_logging import make_slog
import logging
__level__ = logging.DEBUG 
_slog = make_slog(level = __level__)
def rubbish():
    _slog.info("Guten Tag!")
    pass
rubbish()

