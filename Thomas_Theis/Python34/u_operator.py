# Eingabe
print("Geben Sie Ihr Bruttogehalt in Euro ein:")
gehalt = float(input())
print("Geben Sie Ihren Familienstand ein"
      + " (1=ledig, 2=verheiratet):")
fs = int(input())

# Umrechnung
if gehalt > 4000 and fs == 1:
    sb = gehalt * 0.26
elif gehalt <= 4000 and fs == 2:
    sb = gehalt * 0.18
else:
    sb = gehalt * 0.22

# Ausgabe
print("Es ergibt sich ein Steuerbetrag von", sb, "Euro")
