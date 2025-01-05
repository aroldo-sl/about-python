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

# ## This test function cannot be used outside pytest.
# ## Only pytest can import caplog as a fixture.
def test_slog_in_rubbish(caplog):
    """
    Tests if a simple log object
    works in the rubbish function
    namespace.
    """
    with caplog.at_level(_slog.level):
        rubbish()
    assert "666" in caplog.text 

# ## This test function cannot be used outside pytest.
# ## Only pytest can import caplog as a fixture.
def test_slog_in_garbage(caplog):
    """
    Tests if a simple log object
    works in the garbage function
    namespace.
    """
    with caplog.at_level(_slog.level):
        garbage()
    assert "666" in caplog.text, "666 or Beelzebub?" 
