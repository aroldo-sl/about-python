import tkinter

def ende():
    main.destroy()

def lbpop(e):
    global lbx, lby
    
    # ermittelt geometrischen Ort des Hauptfensters
    # Form: "width*height+x+y"
    gm = main.geometry()
    teil = gm.split("+")
    mainx = int(teil[1])
    mainy = int(teil[2])

    # Ermittlung der Position des Popup-Menus:
    # Fensterposition plus Labelposition plus Position
    # innerhalb des Labels plus Versatz
    mpop.tk_popup(mainx + lbx + e.x + 5,
                  mainy + lby + e.y + 30)

def farbwechsel():
    lb["bg"] = farbe.get()

main = tkinter.Tk()

# Frame zur Erzeugung der Fenstermasse
fr = tkinter.Frame(main, height=200, width=300)
fr.pack()

# Label mit Bild, Rahmen und Farbe
# Koordinaten des Labels in Variablen
im = tkinter.PhotoImage(file="figur.gif")
lb = tkinter.Label(main, image=im, relief="ridge",
                   bd=5, bg="#000000")
lb.bind("<Button 3>",lbpop)
lbx = 60
lby = 30
lb.place(x=lbx, y=lby, anchor="nw")

# Widget-Variable der Farbe
farbe = tkinter.StringVar()
farbe.set("#000000")

# Menu zur Farbeinstellung
mpop = tkinter.Menu(main)
mpop["tearoff"] = 0
mpop.add_radiobutton(label="rot", variable=farbe,
   value="#FF0000", command=farbwechsel)
mpop.add_radiobutton(label="gelb", variable=farbe,
   value="#FFFF00", command=farbwechsel)
mpop.add_radiobutton(label="schwarz", variable=farbe,
   value="#000000", command=farbwechsel)

# Ende
bende = tkinter.Button(main, text="Ende",
                       command=ende)
bende.place(relx=1, rely=0, anchor="ne")

main.mainloop()

