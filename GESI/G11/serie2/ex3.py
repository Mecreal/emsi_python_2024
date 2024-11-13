# Année Bissextile

annee = int(input("Entrez l'année: "))

if annee % 4 == 0:
    if not (annee % 100 == 0):
        print(f"L'année {annee} est bissextile")
    else:
        if annee % 400 == 0:
            print(f"L'année {annee} est bissextile")
        else:
            print(f"L'année {annee} n'est pas bissextile")
else:
    print(f"L'année {annee} n'est pas bissextile")

