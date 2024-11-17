# 

while 1:
    print("Bienvenue au programme de calculatrice")
    nbr_1 = float(input("entrez le premier nombre :"))
    nbr_2 = float(input("entrez le deuxieme nombre :"))

    somme  = nbr_1 + nbr_2
    diff   = nbr_1 - nbr_2
    prod   = nbr_1 * nbr_2

    if nbr_2 == 0:
        print("erreur: division par Zero")
    else:
        div = nbr_1 / nbr_2
        modulo = nbr_1 % nbr_2
        exp = nbr_1 ** nbr_2
        print(f"""{nbr_1} + {nbr_2} = {somme:.0f}
{nbr_1} - {nbr_2} = {diff:.0f}
{nbr_1} * {nbr_2} = {prod:.0f}
{nbr_1} / {nbr_2} = {div:.2f}
{nbr_1} % {nbr_2} = {modulo:.0f}
{nbr_1} ** {nbr_2} = {exp:.0f}""")
