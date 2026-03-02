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
with subprocess.Popen(["./slow-output2.sh"],
                       text=True,
                       stdout = subprocess.PIPE,
                       stderr = subprocess.PIPE) as proc:
    while True:
        out=(proc.stdout.readline()).rstrip()
        err=(proc.stderr.readline()).rstrip()
        if  (out,err) == ("",""):
              break
        else:
            print("OUTPUT:" + out, file = sys.stdout)
            print("ERROR:" + err, file=sys.stderr)

print(f"END of {this_file}")
    






