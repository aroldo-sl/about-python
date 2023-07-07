import tkinter

# Funktion zu Button Ende
def ende():
    main.destroy()

# Hauptfenster
main = tkinter.Tk()

# Button Ende
b = tkinter.Button(main, text = "Ende", command = ende)
b.pack()

# Endlosschleife
main.mainloop()
