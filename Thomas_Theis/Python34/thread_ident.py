# Module
import time, _thread

# Thread-Funktion
def show():
    id = _thread.get_ident()
    print("Start Thread", id)
    for i in range(5):
        print(i, "Thread", id)
        time.sleep(1.5)
    print("Ende Thread", id)
    return

# Hauptprogramm
id = _thread.get_ident()
print("Start Hauptprogramm", id)
_thread.start_new_thread(show,())
time.sleep(0.5)
_thread.start_new_thread(show,())
time.sleep(10)
print("Ende Hauptprogramm", id)
