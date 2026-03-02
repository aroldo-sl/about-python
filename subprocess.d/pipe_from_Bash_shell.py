#!/usr/bin/env python
"""
Beispiele subprocess PIPE.
Using a Popen object as a context manager.
Streaming the subprocess standard output and
the subprocess error output separately from
each other.
"""
import os, sys, subprocess
from pathlib import Path
this_file = Path(sys.argv[0])
print(f"BEGIN of {this_file}")

proc_env = dict(GARBAGE="garbage",
                # RUBBISH="rubbish",
                )
# The subprocess will be executed in an extended environment:
os.environ.update(proc_env)
cmd_tuple = ["./pipe-to-Python.sh"]
with subprocess.Popen(cmd_tuple, # the executable and parameters
                      text=True,
                      stdout = subprocess.PIPE,
                      stderr = subprocess.PIPE) as proc:
    while True:
        out=(proc.stdout.readline()).rstrip()
        err=(proc.stderr.readline()).rstrip()
        if  (out,err) == ("",""):
              break
        if not out == "":
            print("OUTPUT:" + out, file = sys.stdout)
        if not err == "":
            print("ERROR:" + err, file=sys.stderr)
        # controlling the process depending on its latest output line:
        if "bbbb" in out:
            print("bbbb in out: killing the process.")
            proc.kill()
                  
print(f"END of {this_file}")
    






