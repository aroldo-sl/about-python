import tkinter

def ende():
    main.destroy()

def farbwechsel():
    fr["bg"] = farbe.get()

def randwechsel():
    if rand.get():
        fr["relief"] = "ridge"
    else:
        fr["relief"] = "flat"

main = tkinter.Tk()

# Zielobjekt der Menubefehle
fr = tkinter.Frame(main, height=100, width=300,
                   bg="#FFFFFF", bd=10)
fr.pack()

# erzeugt gesamte Menuleiste
mBar = tkinter.Menu(main)

# erzeugt erstes Menuobjekt der Menuleiste
mFile = tkinter.Menu(mBar)

# erzeugt Elemente in erstem Menu
mFile.add_command(label="Neu")
mFile.add_command(label="Laden")
mFile.add_command(label="Speichern")
mFile.add_separator()
mFile.add_command(label="Beenden", command=ende)

# Widget-Variablen der Radiobutton-Menupunkte
# bzw. Checkbutton-Menupunkte
farbe = tkinter.StringVar()
farbe.set("#FFFFFF")
rand = tkinter.IntVar()
rand.set(0)

# erzeugt zweites Menuobjekt der Menuleiste
mView = tkinter.Menu(mBar)
mView["tearoff"] = 0     # Menu nicht abtrennbar

# erzeugt Elemente in zweitem Menu
mView.add_radiobutton(label="Rot", variable=farbe,
   value="#FF0000", underline=0, command=farbwechsel)
mView.add_radiobutton(label="Gelb", variable=farbe,
   value="#FFFF00", underline=0, command=farbwechsel)
mView.add_radiobutton(label="Blau", variable=farbe,
   value="#0000FF", underline=0, command=farbwechsel)
mView.add_radiobutton(label="Magenta", variable=farbe,
   value="#FF00FF", underline=0, command=farbwechsel)
mView.add_separator()
mView.add_checkbutton(label="Rand sichtbar",
   variable=rand, onvalue=1, offvalue=0, underline=5,
   command=randwechsel)

# erstes und zweites Menu zur Menuleiste hinzu
mBar.add_cascade(label="Datei", menu=mFile)
mBar.add_cascade(label="Ansicht", menu=mView)

# gesamte Menuleiste zu Fenster hinzu
main["menu"] = mBar

main.mainloop()

