import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)      # GPIO-Nummern verwenden
gp.setwarnings(False)   # Keine Ausgabe von Warnungen
gp.setup(18, gp.OUT)    # GPIO 18 wird Ausgang

gp.output(18, gp.HIGH)  # LED anschalten
time.sleep(1.5)         # Warten
gp.output(18, gp.LOW)   # LED ausschalten
