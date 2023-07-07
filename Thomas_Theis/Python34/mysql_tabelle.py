# Connector importieren
import sys, mysql.connector

# Verbindung zur Datenbank auf dem Datenbankserver erstellen
try:
    connection = mysql.connector.connect(host = "localhost", \
        user = "root", passwd = "", db = "firma")
except:
    print("Keine Verbindung zum Server")
    sys.exit(0)

# Execution-Objekt erzeugen
cursor = connection.cursor()

# Tabelle erzeugen
cursor.execute("CREATE TABLE IF NOT EXISTS personen ("
    "name varchar(30), vorname varchar(25),"
    "personalnummer int(11), gehalt double, geburtstag date,"
    "PRIMARY KEY (personalnummer))")
connection.commit()

# Execution-Objekt schliessen
cursor.close()

# Verbindung schliessen
connection.close()
