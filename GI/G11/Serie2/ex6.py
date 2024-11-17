# Calculatrice infinie

while 1:
    print("Bienvenue au programme de calculatrice")
    nbr_1 = float(input("entrez le premier nombre :"))
    nbr_2 = float(input("entrez le deuxieme nombre :"))

    somme = nbr_1 + nbr_2
    difference = nbr_1 - nbr_2
    produit = nbr_1 * nbr_2

    if not (nbr_2 == 0):
        division = nbr_1 / nbr_2
        modulo = nbr_1 % nbr_2
        expo = nbr_1 ** nbr_2

        print(f"""{nbr_1} + {nbr_2} = {somme:.0f}
{nbr_1} - {nbr_2} = {difference}
{nbr_1} * {nbr_2} = {produit}
{nbr_1} / {nbr_2} = {division:.2f}
{nbr_1} % {nbr_2} = {modulo}
{nbr_1} ** {nbr_2} = {expo}""")
    else:
        print(f"""{nbr_1} + {nbr_2} = {somme:.0f}
{nbr_1} - {nbr_2} = {difference}
{nbr_1} * {nbr_2} = {produit}
erreur: division par Zero""")
    print("-_"*30)
    input("Appuyez sur entrée pour continuer")
