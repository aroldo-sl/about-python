# Funktion
def steuer(bb):
    # Umrechnung
    if bb > 2500:
        sb = bb * 0.22
    else:
        sb = bb * 0.18

    # Ausgabe
    print("Bruttobetrag:", bb,
          "Euro, Steuerbetrag:", sb, "Euro")
    
# Verschiedene Werte
steuer(1800)
steuer(2200)
steuer(2500)
steuer(2900)
