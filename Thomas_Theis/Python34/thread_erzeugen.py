# Module
import time, _thread

# Thread-Funktion
def show():
    print("Start Thread")
    for i in range(5):
        print(i, time.time())
        time.sleep(1.5)
    print("Ende Thread")
    return

# Hauptprogramm
print("Start Hauptprogramm:", time.time())
_thread.start_new_thread(show,())
time.sleep(10)
print("Ende Hauptprogramm:", time.time())
