# Déterminer si ll'année est bissextile ou non

print("Bienvenue au programme pour vérifier si une année est bissextile ou non")

annee = int(input("entrez une année :"))


if annee % 4 == 0:
    if annee % 100 == 0:
        if annee % 400 == 0:
            print(f"L'année {annee} est bissextile")
        else:
            print(f"L'année {annee} n'est pas bissextile")
    else:
        print(f"L'année {annee} est bissextile")
else:
    print(f"L'année {annee} n'est pas bissextile")
