# Modul time
import time

# Zeit in Sekunden
print("Zeit in Sekunden:", time.time())

# Aktuelle, lokale Zeit als Tupel
lt = time.localtime()

# Entpacken des Tupels
# Datum
jahr, monat, tag = lt[0:3]
print("Es ist der {0:02d}.{1:02d}.{2:4d}".
      format(tag, monat, jahr))

# Uhrzeit
stunde, minute, sekunde = lt[3:6]
print("genau {0:02d}:{1:02d}:{2:02d}".
      format(stunde, minute, sekunde))

# Wochentag
wtage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag",
         "Freitag", "Samstag", "Sonntag"]
wtagnr = lt[6]
print("Das ist ein", wtage[wtagnr])

# Tag des Jahres
tag_des_jahres = lt[7]
print("Der {0:d}. Tag des Jahres".
      format(tag_des_jahres))

# Sommerzeit
dst = lt[8]
if dst == 1:
    print("Die Sommerzeit ist aktiv")
elif dst == 0:
    print("Die Sommerzeit ist nicht aktiv")
else:
    print("Keine Sommerzeitinformation vorhanden")
