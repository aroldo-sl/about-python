#!/usr/bin/env python
"""
Handling ini files with ConfigParser.
"""
import sys
from configparser import ConfigParser
from collections import OrderedDict
import pytest

class PackageListParser(ConfigParser):
    """
    Simple settings for a ConfigParser.
    """
    def __init__(self):
        super().__init__(self,
                         allow_no_value = True,
                         dict_type = OrderedDict,
                         delimiters = (":",),
                         )
        self.optionxform = lambda option:option


def test_PackageListParser_initializing():
    """
    Initializes a ConfigParser object.
    """
    CPS = PackageListParser
    config = CPS()
    assert isinstance(config, CPS)
    assert isinstance(config, ConfigParser)

def test_read_ini():
    """
    Reads an 'ini' file.
    """
    CPS = PackageListParser
    config = CPS()
    config.read("packages.in.ini")
    assert config["DEFAULT"] is not None
    assert config["packages.Emacs-deps"]["build-essential"] is None

def test_write_ini():
    """
    Reads an 'ini' file.
    """
    CPS = PackageListParser
    config = CPS()
    config.read("packages.in.ini")
    config["packages.Emacs-deps"]["build-essential"] = "installed"
    with open("packages.out.ini", "w") as outfile:
        config.write(outfile)


def main():
    """
    Runs the tests.
    """
    pytest.main(["-v", sys.argv[0]])

if __name__ == "__main__":
    main()
