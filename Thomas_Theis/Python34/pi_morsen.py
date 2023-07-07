import sys, morsen, time
import RPi.GPIO as gp

# Beispieltext codieren
def lichtCode(text, code):
    # Einstellungen fuer GPIO
    gp.setmode(gp.BCM)
    gp.setwarnings(False)
    gp.setup(18, gp.OUT)

    # Zeitschema, Dauer eines Signals in sec.
    signalDauer = {".":0.2, "-":0.6}

    # Zeitschema, Dauer einer Pause in sec.
    signalPause = 0.2
    zeichenPause = 0.6
    wortPause = 1.4

    # Text in Worte zerlegen
    alleWorte = text.split()

    # Jedes Wort im Text
    for w in range(len(alleWorte)):
        # Uebernahme eines Worts
        wort = alleWorte[w]
        # Jedes Zeichen im Wort
        for z in range(len(wort)):
            # Uebernahme eines Zeichens
            zeichen = wort[z]
            # Kontrollausgabe des Zeichens
            print(zeichen, end="")
            # Versuch, ein Zeichen auszugeben
            try:
                # Uebernahme des Morsezeichens für das Zeichen
                # Falls kein Eintrag im Dictionary: KeyError
                alleSignale = code[zeichen]
                # Jedes Signal des Morsezeichens
                for s in range(len(alleSignale)):
                    # Uebernahme eines Symbols
                    signal = alleSignale[s]
                    # Ausgabe des Symbols, kurz oder lang
                    gp.output(18, gp.HIGH)
                    time.sleep(signalDauer[signal])
                    gp.output(18, gp.LOW)
                    # Nach jedem Signal eine Signalpause,
                    # ausser nach dem letzten Signal
                    if s < len(alleSignale)-1:
                        time.sleep(signalPause)
                # Nach jedem Zeichen eine Zeichenpause,
                # ausser nach dem letzten Zeichen
                if z < len(wort)-1:
                    time.sleep(zeichenPause)
            # Falls kein Eintrag im Dictionary: ignorieren
            except KeyError:
                pass
        # Nach jedem Wort eine Wortpause,
        # ausser nach dem letzten Wort
        if w < len(alleWorte)-1:
            print(" ", end="")
            time.sleep(wortPause)

# Lesefunktion aufrufen
code = morsen.leseCode()

# Ausgabefunktion aufrufen
lichtCode("Hallo Welt", code)
