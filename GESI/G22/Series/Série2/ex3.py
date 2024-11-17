# Année Bissextile

print("Bienvenue au programme qui vérifie si une année est bissextile")

annee = int(input("Entrez l'année: "))

affichage_vrais = f"L'année {annee} est bissextile"
affichage_faux = f"L'année {annee} n'est pas bissextile"

if annee % 4 == 0:
    if not (annee % 100 == 0):
        print(affichage_vrais)
    else:
        if annee % 400 == 0:
            print(affichage_vrais)
        else:
            print(affichage_faux)
else:
    print(affichage_faux)


# Méthode deux

if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
    print(affichage_vrais)
else:
    print(affichage_faux)

