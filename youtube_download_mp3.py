#!/usr/bin/env python
"""
tkinter GUI for yt-dlp in a subprocess.
Uses xterm for yt-dlp.
"""
import tkinter as tk
from tkinter import ttk
import subprocess, shutil, shlex, sys, os
import pyperclip
from pathlib import Path

# ## Defining the subprocess.
command_fmt = 'xterm -hold -132 -bg white -fg black -fa Monospace -fs 14 -geometry 150x30  -e {executable} --config-locations  {config_dir} -- {url}'
url_default="https://www.youtube.com/watch?v=S-rB0pHI9fU"
executable = Path(shutil.which("yt-dlp"))
config_subdir = "mp3.d"

# ## The suprocess environment.
HOME = Path(os.environ.get("HOME"))
XDG_CONFIG_HOME  = HOME/".config"
config_dir = XDG_CONFIG_HOME/executable.name/config_subdir
subprocess_env = dict(
    XDG_CONFIG_HOME = str(XDG_CONFIG_HOME),
    config_dir = str(config_dir))
os.environ.update(subprocess_env)

## # The GUI to get the url and call the subprocess.
root = tk.Tk()
root.geometry('1200x150+150+150')
root.title("")
frame = ttk.Frame(root)
style = ttk.Style()
## TButton and TLabel layouts seem to be pre-defined in ttk.
style.configure("Title.TLabel", font = ("Helvetia", 20), foreground = "magenta")
style.configure("DButton.TButton", font = ("Helvetia",14), foreground = 'red')
style.configure("DLabel.TLabel", font = ("Helvetia",16), foreground = "green")
url_tkstring = tk.StringVar(frame)
url_tkstring.set(url_default)
# ## <debug>
print("Default url:", url_tkstring.get())
# ##</debug>
titleLabel = ttk.Label(frame, style = "Title.TLabel",
                       text = "Herrquesada YouTube App")
prompt = ttk.Label(frame,
                   style = "DLabel.TLabel",
                   text = 'Type the video url here:')
inputBox = ttk.Entry(frame,
                     font='georgia 16 bold',
                     foreground='green',
                     width = 200,
                     textvariable = url_tkstring,
                     )
inputBox.selection_range(0, tk.END)

okButton = ttk.Button(frame,
                      style = "DButton.TButton", 
                      text="Download")

# ## the inputBox event handler
def insert_url(event):
    text = pyperclip.paste()
    event.widget.delete(0, tk.END)
    event.widget.insert(0,text)
inputBox.bind("<Button-3>", insert_url)

# ## The okButton event handler.
def download(event):
    url = inputBox.get()
    command_line = command_fmt.format(config_dir = os.environ.get("config_dir"),
                                           executable = executable,
                                           url = url)
    arg_list = shlex.split(command_line)
    # ##<debug>
    print(arg_list)
    # ##</debug>
    proc = subprocess.run(arg_list,
                          stdout = subprocess.PIPE,
                          stderr = subprocess.PIPE)
    root.destroy()
okButton.bind("<Button-1>", download)
okButton.bind("<Return>", download)

# ## Packing everything using the Pack layout manager without parameters:
widgets = (
    frame,
    titleLabel,
    prompt,
    inputBox,
    okButton,
    )
for w in widgets:
    w.pack()
inputBox.focus()

# ## Triggering the GUI.
root.mainloop()
