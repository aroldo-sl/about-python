#!/usr/bin/env python
"""
Beispiele subprocess PIPE.
"""
import os, sys, subprocess
from pathlib import Path
this_file = Path(sys.argv[0])
print(f"BEGIN of {this_file}")

proc_env = dict(GARBAGE="garbage",
                # RUBBISH="rubbish",
                )
os.environ.update(proc_env)
with subprocess.Popen(["./slow-output.sh"],
                       text=True,
                       stdout = subprocess.PIPE,
                       stderr = subprocess.PIPE) as proc:
    while True:
        line=(proc.stdout.readline()).rstrip()
        if  line == "":
              break
        else:
            print(line)

print(f"END of {this_file}")
    






