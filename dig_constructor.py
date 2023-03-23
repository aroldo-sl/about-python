#!/usr/bin/env python3
# @file: dig_constructor.py
# @date: 2023-03-23T09:18:54
# @author: Aroldo Souza-Leite
# @description: 
"""
inline documentation of this module (99:.\\*.py)
"""
import os, sys, logging
__level__ = logging.INFO
import pytest


######################### <_get_slog>   #########
def _get_slog ( level = __level__):
    "Wrapper for the get_slog function"

    import  random, string

    class SLogFormatter(logging.Formatter):
        "A log formatter for SLogHandler"
        fmt = "%(levelname)s:%(name)s:%(module)s.%(funcName)s:%(lineno)s\n%(message)s"
        def __init__(self, fmt = None):
            if fmt is None:
                fmt = SLogFormatter.fmt
            super().__init__(fmt = fmt)

    class SLogHandler(logging.StreamHandler):
        "Simple logging handler."
        def __init__(self, stream = sys.stderr, level = __level__):
            super().__init__(stream = stream)
            self.setLevel(level)
            self.setFormatter(SLogFormatter())

    def get_slog(handler = None, level = __level__):
        "Make a simple logger"
        if handler is None:
            handler = SLogHandler()
        handler.setLevel(level)
        random_string = "".join(random.sample(string.ascii_letters, 4))
        log_name  = __name__ + "-" + random_string
        slog = logging.getLogger(log_name)
        slog.addHandler(handler)
        slog.setLevel(level)
        return slog
    return get_slog(level = level)
######################### </_get_slog>  #########

_slog = _get_slog(level = __level__)

## to unhide a code block got to the block top and press "<f5> h"
from pathlib import Path

class NPath(Path):
    def __new__(cls, *p, **kwargs):
        path = super().__new__(cls)
        return path

    def __init__(self, *p, **kwargs):
        super().__init__(*p, **kwargs)

@pytest.mark.skip(reason = "See this test's inline doc")
def test_NPath():
    """
    Tests ste NPath class with an implemented __new__.
    This tests is causing a TypeError:

    cls = <class 'dig_constructor.NPath'>, args = ()

        @classmethod
        def _parse_args(cls, args):
            # This is useful when you don't want to create an instance, just
            # canonicalize some constructor arguments.
            parts = []
            for a in args:
                if isinstance(a, PurePath):
                    parts += a._parts
                else:
                    a = os.fspath(a)
                    if isinstance(a, str):
                        # Force-cast str subclasses to str (issue #21127)
                        parts.append(str(a))
                    else:
                        raise TypeError(
                            "argument should be a str object or an os.PathLike "
                            "object returning str, not %r"
                            % type(a))
    >       return cls._flavour.parse_parts(parts)
    E       AttributeError: type object 'NPath' has no attribute '_flavour'
    """
    npath = NPath('/home/aroldo/')
    assert isinstance(npath, Path)


class PlusOne(int):
    def __new__(cls, *p, **kwargs):
        """
        Builds an instance of int incremented by 1
        """
        n = super().__new__(cls, *p, **kwargs)
        plus_one = n + 1
        return plus_one


def test_PlusOne():
    """
    Instantiates a PlusOne object.
    """
    plus_one = PlusOne(5)
    assert isinstance(plus_one, (PlusOne, int))
    assert plus_one == 6
    seven = plus_one  + 1
    assert seven == 7


def _script():
    """
    Runs if this module is called as a
    Python script.
    """
    _slog.info("Perfect!")
    pytest.main(["-v", __file__])


if __name__ == "__main__":
   _script()


# yasnippet: 

