# Calcule de factorielle

print("Bienvenue au programme de calcule factorielle")


nbr = int(input("entrez un nombre :"))

fact = 1

if nbr < 0:
    print("erreur: factorielle d'un nombre negatif n'existe pas")
elif nbr == 0:
    print(f"factorielle de {nbr} est {fact}")
else:
    for i in range(1, nbr + 1,1):
        fact *= i
    print(f"factorielle de {nbr} est {fact}")
