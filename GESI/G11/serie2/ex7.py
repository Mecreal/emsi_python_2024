# Calcule factorielle


print("Bienvenue au programme de calcul de factorielle")

n = int(input("entrez un nombre entier positif: "))
fact = 1

if n < 0:
    print("erreur: nombre négatif")
else:
    for i in range(1, n + 1):
        fact = fact * i
    print(f"{n}! = {fact}")
