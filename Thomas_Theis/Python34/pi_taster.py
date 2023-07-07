import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)      # GPIO-Nummern verwenden
gp.setwarnings(False)   # Keine Ausgabe von Warnungen
gp.setup(18, gp.IN)     # GPIO 18 wird Eingang

zeitAktuell = time.time()       # Zeiten setzen
zeitEnde = zeitAktuell + 5

while zeitAktuell < zeitEnde:   # Ende erreicht?
    if gp.input(18) == True:    # GPIO abfragen
        print(time.time())
    zeitAktuell = time.time()
