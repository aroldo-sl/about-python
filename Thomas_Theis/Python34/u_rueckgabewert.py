# Funktion
def steuer(bb):
    # Umrechnung
    if bb > 2500:
        sb = bb * 0.22
    else:
        sb = bb * 0.18

    # Ergebnis senden
    return sb
    
# Verschiedene Werte
print("Bruttobetrag: 1800 Euro, Steuerbetrag:",
      steuer(1800), "Euro")
print("Bruttobetrag: 2200 Euro, Steuerbetrag:",
      steuer(2200), "Euro")
print("Bruttobetrag: 2500 Euro, Steuerbetrag:",
      steuer(2500), "Euro")
print("Bruttobetrag: 2900 Euro, Steuerbetrag:",
      steuer(2900), "Euro")
