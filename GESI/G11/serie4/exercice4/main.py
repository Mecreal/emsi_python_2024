import utils

print(" Bienvenue au programme de calculatrice")


nbr_1 = float(input("entrez le premier nombre :"))
nbr_2 = float(input("entrez le deuxieme nombre :"))

op = int(input("""entrez le nombre de l'opération:
1 : addition
2 : soustraction
3 : multiplication
4 : division
5 : modulo
6 : puissance
"""))

if op == 1:
    print(f"{nbr_1} + {nbr_2} = {utils.somme(nbr_1, nbr_2)}")
elif op == 2:
    print(f"{nbr_1} - {nbr_2} = {utils.soustraction(nbr_1, nbr_2)}")
elif op == 3: 
    print(f"{nbr_1} * {nbr_2} = {utils.produit(nbr_1, nbr_2)}")
elif op == 4:
    print(f"{nbr_1} / {nbr_2} = {utils.division(nbr_1, nbr_2)}")
