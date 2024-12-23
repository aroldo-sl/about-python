#!/usr/bin/env python

import tkinter as tk
from tkinter import ttk
import subprocess, shutil, shlex, sys, os
import pyperclip
from pathlib import Path

command_line_fmt = 'xterm -hold -132 -bg white -fg black -fa Monospace -fs 14 -geometry 150x30  -e {executable} --config-locations  {config_dir} -- {url}'
url_default="https://www.youtube.com/watch?v=S-rB0pHI9fU"
executable = Path(shutil.which("yt-dlp"))
config_subdir = "mp3.d"

HOME_path = Path(os.environ.get("HOME"))
XDG_CONFIG_HOME_path  = HOME_path/".config"
config_dir_path = XDG_CONFIG_HOME_path/executable.name/config_subdir
subprocess_env = dict(
    XDG_CONFIG_HOME = str(XDG_CONFIG_HOME_path),
    config_dir = str(config_dir_path))
os.environ.update(subprocess_env)

root = tk.Tk()
root.title("Herrquesada YouTube App")
root.geometry('1200x100+150+150')
url_tkstring = tk.StringVar(root)
url_tkstring.set(url_default)
# ## <debug>
print("Default url:", url_tkstring.get())
# ##</debug>


prompt = ttk.Label(root, text = 'Type the video url here:')
inputBox = ttk.Entry(root, textvariable = url_tkstring, width = 140)
url_default_length = len(url_tkstring.get())
inputBox.selection_range(0,url_default_length)
okButton = ttk.Button(text="Download")

def insert_url(event):
    text = pyperclip.paste()
    event.widget.delete(0, tk.END)
    event.widget.insert(0,text)
inputBox.bind("<Button-3>", insert_url)
    
def download(event):
    url = inputBox.get()
    command_line = command_line_fmt.format(config_dir = os.environ.get("config_dir"),
                                           executable = executable,
                                           url = url)
    arg_list = shlex.split(command_line)
    print(arg_list)
    proc = subprocess.run(arg_list,
                          stdout = subprocess.PIPE,
                          stderr = subprocess.PIPE)
    root.destroy()
    
okButton.bind("<Button-1>", download)
okButton.bind("<Return>", download)

for w in (prompt, inputBox, okButton):
    w.pack()
inputBox.focus()

root.mainloop()
