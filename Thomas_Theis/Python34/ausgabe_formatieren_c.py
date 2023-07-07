# 1: Zahl mit Nachkommastellen
x = 100/7
y = 2/7
print("Zahlen:")
print(x, y)
print()

2# 2: Format f
print("Format f")
print("%f %f %f" % (x, x, y))
print("%15.10f %.25f" % (x, y))
print()

# 3: Format e
print("Format e")
print("%e" % (x))
print("%12.3e" % (x))
print("%.3e" % (x))
print()

# 4: Format %
print("Format %")
print("%f%%" % (y*100))
print("%12.3f%%" % (y*100))
print("%.3f%%" % (y*100))
