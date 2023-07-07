import random, time

# Klasse "Spiel"
class Spiel:
    def __init__(self):
        # Start des Spiels
        random.seed()
        self.richtig = 0

        # Anzahl bestimmen
        self.anzahl = -1
        while self.anzahl<0 or self.anzahl>10:
            try:
                print("Wieviele Aufgaben (1 bis 10):")
                self.anzahl = int(input())
            except:
                continue

    def spielen(self):
        # Spielablauf
        for i in range(1,self.anzahl+1):
            a = Aufgabe(i, self.anzahl)
            print(a)
            self.richtig += a.beantworten()

    def messen(self, start):
        # Zeitmessung
        if start:
            self.startzeit = time.time()
        else:
            endzeit = time.time()
            self.zeit = endzeit - self.startzeit

    def __str__(self):
        # Ergebnis
        ausgabe = "Richtig: {0:d} von {1:d} in " \
            "{2:.2f} Sekunden".format(self.richtig, \
            self.anzahl, self.zeit)
        ausgabe += "\nam " + time.strftime("%d.%m.%Y") \
            + " um " + time.strftime("%H:%M:%S")
        return ausgabe

# Klasse "Aufgabe"
class Aufgabe:
    # Aufgabe initialisieren
    def __init__(self, i, anzahl):
        self.nr = i
        self.gesamt = anzahl

    # Aufgabe stellen
    def __str__(self):
        a = random.randint(10,30)
        b = random.randint(10,30)
        self.ergebnis = a + b
        return "Aufgabe " + str(self.nr) \
            + " von " + str(self.gesamt) + " : " \
            + str(a) + " + " + str(b)
        
    # Aufgabe beantworten
    def beantworten(self):
        try:
            if self.ergebnis == int(input()):
                print(self.nr, ": ***Richtig ***")
                return 1
            else:
                raise
        except:
            print(self.nr, ": *** Falsch ***")
            return 0

# Hauptprogramm
s = Spiel()
s.messen(True)
s.spielen()
s.messen(False)
print(s)
