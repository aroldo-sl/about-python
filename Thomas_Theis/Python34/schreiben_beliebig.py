import sys, os

# Zugriffsversuch
try:
    d = open("obst.txt", "r+")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Lesen des Einzelpreises
d.seek(68)
ep_str = d.read(8)
ep = float(ep_str)

# Schreiben des Einzelpreises
d.seek(68)
ep = ep + 0.2
d.write("{0:8.2f}".format(ep))

# Lesen des Gesamtpreises
d.seek(81)
gp_str = d.read(8)
gp = float(gp_str)

# Schreiben des Gesamtpreises
d.seek(81)
gp = gp + 0.2
d.write("{0:8.2f}".format(gp))

# Schliessen der Datei
d.close()
