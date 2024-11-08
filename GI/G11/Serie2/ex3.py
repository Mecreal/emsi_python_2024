# Utiliser les condition imbriquer pour savoir si l'annee esrt bissextile


annee = int(input("entrez l'année :"))

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