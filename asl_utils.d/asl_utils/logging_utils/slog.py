"""
Constructor for Simple Logger.
A simple method for logging in Python,
especialolly for small code development projects.
Avoidind 'print' during code development.
"""
import sys, uuid, logging # for _make_slog

fmt_str = (
"%(levelname)s"
"|logger:%(name)s"
"|line number:%(lineno)s"
"|namespace:%(funcName)s"
"\n%(message)s"
)

def make_slog(stream = sys.stderr,
        level = logging.DEBUG,
        fmt_str = fmt_str):
    """
    Constructor for a simple unique logger.
    Each call of this function returns a logger with a
    unique name, that is, a Logger object different from loggers
    instantiated through preceding calls of the same function.
    """
    
    # ## <formatter>
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
    slog.setLevel(level)
    # ## </slog>
    
    return slog

