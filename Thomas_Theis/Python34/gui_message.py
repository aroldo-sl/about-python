import tkinter, tkinter.messagebox

def ende():
    main.destroy()

def msginfo():
    tkinter.messagebox.showinfo \
       ("Info","Eine Info-Box")

def msgwarning():
    tkinter.messagebox.showwarning \
       ("Warnung","Eine Warnungs-Box")

def msgerror():
    tkinter.messagebox.showerror \
       ("Fehler","Eine Fehler-Box")

def msgyesno():
    antwort = tkinter.messagebox.askyesno \
       ("Ja/Nein", "Eine Ja/Nein-Box")
    if antwort == 1:
        lbanz["text"] = "Ja"
    else:
        lbanz["text"] = "Nein"

def msgokcancel():
    antwort = tkinter.messagebox.askokcancel \
       ("Ok/Abbrechen", "Eine Ok/Abbrechen-Box")
    if antwort == 1:
        lbanz["text"] = "Ok"
    else:
        lbanz["text"] = "Abbrechen"

def msgretrycancel():
    antwort = tkinter.messagebox.askretrycancel \
       ("Wiederholen/Abbrechen",
        "Eine Wiederholen/Abbrechen-Box")
    if antwort == 1:
        lbanz["text"] = "Wiederholen"
    else:
        lbanz["text"] = "Abbrechen"

def msgfrage():
    # hier einmal in allgemeiner Technik, ohne Komfort
    msgbox = tkinter.messagebox.Message(main,
        type=tkinter.messagebox.ABORTRETRYIGNORE,
        icon=tkinter.messagebox.QUESTION,
        title="Beenden/Wiederholen/Ignorieren",
        message="Beenden, Wiederholen oder Ignorieren")
    
    antwort = msgbox.show()

    if antwort == "abort":
        lbanz["text"] = "Beenden"
    elif antwort == "retry":
        lbanz["text"] = "Wiederholen"
    else:
        lbanz["text"] = "Ignorieren"

main = tkinter.Tk()

# Button: Message Info
binfo = tkinter.Button(main,
   text = "Info", command=msginfo)
binfo.pack()

# Button: Message Box Warning
bwarning = tkinter.Button(main,
   text = "Warnung", command=msgwarning)
bwarning.pack()

# Button: Message Box Error
berror = tkinter.Button(main,
   text = "Fehler", command=msgerror)
berror.pack()

# Button: Message Box Ja/Nein
byesno = tkinter.Button(main,
   text = "Ja/Nein", command=msgyesno)
byesno.pack()

# Button: Message Box OK/Cancel
bokcancel = tkinter.Button(main,
   text = "Ok/Abbrechen", command=msgokcancel)
bokcancel.pack()

# Button: Message Box Retry/Cancel
bretrycancel = tkinter.Button(main,
   text = "Wiederholen/Abbrechen",
   command=msgretrycancel)
bretrycancel.pack()

# Button: Message Box Frage
bfrage = tkinter.Button(main,
   text = "Allgemeine Frage", command=msgfrage)
bfrage.pack()

# Ende-Button
bende = tkinter.Button(main,
   text = "Ende", command=ende)
bende.pack()

# Anzeige-Label
lbanz = tkinter.Label(main)
lbanz.pack()

main.mainloop()
