# Kopie einer Zahl
print("Zahl:")
x = 12.5
y = x
print("gleiches Objekt:", x is y)
y = 15.8
print("gleiches Objekt:", x is y)
print("gleicher Inhalt:", x == y)
print()

# Kopie eines Strings
print("String:")
x = "Robinson"
y = x
print("gleiches Objekt:", x is y)
y = "Freitag"
print("gleiches Objekt:", x is y)
print("gleicher Inhalt:", x == y)
print()

# Zweite Referenz auf eine Liste
print("Liste:")
x = [23,"hallo",-7.5]
y = x
print("gleiches Objekt:", x is y)
y[1] = "welt"
print("gleiches Objekt:", x is y)

