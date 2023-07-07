# Eingabe
print("Geben Sie Ihr Bruttogehalt in Euro ein:")
bruttobetrag = float(input())

# Umrechnung
if bruttobetrag > 2500:
    steuerbetrag = bruttobetrag * 0.22
else:
    steuerbetrag = bruttobetrag * 0.18

# Ausgabe
print("Es ergibt sich ein Steuerbetrag von",
      steuerbetrag, "Euro")
