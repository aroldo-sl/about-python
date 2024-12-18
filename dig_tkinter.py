#!/usr/bin/env python
print("Trying out tkinter")

import tkinter as tk
from tkinter import ttk
import subprocess, shutil, shlex

url=""

executable = shutil.which("yt-dlp")
command_line = f'xterm -hold -132 -bg white -fg black -fa Monospace -fs 14 -geometry 150x30  -e "{executable}; bash"'
print(command_line)
arg_list = shlex.split(command_line)
print(arg_list)

root = tk.Tk()
root.title("Herrquesada YouTube App")
root.geometry('1200x100+150+150')

prompt = ttk.Label(root, text = 'Type the video url here:')
inputBox = ttk.Entry(root, textvariable = tk.StringVar(), width = 140)
okButton = ttk.Button(text="Download")

def download(event):
    text = inputBox.get()
    print ("Downloading", text)
    proc = subprocess.run(arg_list,
                          stdout = subprocess.PIPE,
                          stderr = subprocess.PIPE)
    return proc
    
okButton.bind("<Button-1>", download)
okButton.bind("<Return>", download)

for w in (prompt, inputBox, okButton):
    w.pack()
inputBox.focus()

root.mainloop()
