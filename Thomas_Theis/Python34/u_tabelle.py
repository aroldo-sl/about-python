# Umrechnungsfaktor
inch = 2.54

# Tabellenkopf
print("{0:>7}{1:>7}".format("inch","cm"))

# Schleife
for xi in range (15, 41, 5):
    xcm = xi * inch
    print("{0:7.1f}{1:7.1f}".format(xi,xcm))
