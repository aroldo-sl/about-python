import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setwarnings(False)
gp.setup(18, gp.OUT)

for i in range(5):
    gp.output(18, gp.HIGH)  # LED anschalten
    time.sleep(0.5)         # Bleibt an
    gp.output(18, gp.LOW)   # LED ausschalten
    time.sleep(0.5)         # Bleibt aus
