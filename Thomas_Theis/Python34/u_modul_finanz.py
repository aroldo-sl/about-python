# Funktion
def steuer(bb):
    # Umrechnung
    if bb > 2500:
        sb = bb * 0.22
    else:
        sb = bb * 0.18

    # Ergebnis senden
    return sb
