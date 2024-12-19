#!/usr/bin/env python
print("Trying out tkinter")

import tkinter as tk
from tkinter import ttk
import subprocess, shutil, shlex, sys
import pyperclip

root = tk.Tk()

url_default="https://www.youtube.com/watch?v=S-rB0pHI9fU"
url_string = tk.StringVar(root)
url_string.set(url_default)
print("Default url:", url_string.get())

executable = shutil.which("yt-dlp")
command_line = f'xterm -hold -132 -bg white -fg black -fa Monospace -fs 14 -geometry 150x30  -e "{executable}"'
print(command_line, file = sys.stderr)
arg_list = shlex.split(command_line)
print(arg_list, file = sys.stderr)

root.title("Herrquesada YouTube App")
root.geometry('1200x100+150+150')

prompt = ttk.Label(root, text = 'Type the video url here:')
inputBox = ttk.Entry(root, textvariable = url_string, width = 140)
url_default_length = len(url_string.get())
inputBox.selection_range(0,url_default_length)
okButton = ttk.Button(text="Download")

def insert_url(event):
    text = pyperclip.paste()
    event.widget.delete(0, tk.END)
    event.widget.insert(0,text)
inputBox.bind("<Button-3>", insert_url)
    
def download(event):
    url = inputBox.get()
    arg_list.append(url)
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
