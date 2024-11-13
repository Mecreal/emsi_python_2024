# Vérification nombre pair ou impair

nombre = int(input("Entrez un nombre : "))

if nombre % 2 == 0:
    print(f"{nombre} est un nombre pair")
else:
    print(f"{nombre} est un nombre impair")
# Compare nombre négative ou positive ou nulle

if nombre > 0:
    print(f"{nombre} est un nombre positif")
elif nombre < 0:
    print(f"{nombre} est un nombre négatif")
else:
    print(f"{nombre} est nulle")