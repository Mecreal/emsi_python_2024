# Calculatriuice simple 

print("Programme de calculatrice Simple")

nbr_1 = float(input("Entrez le premier nombre: "))
nbr_2 = float(input("Entrez le deuxieme nombre: "))

op = int(input("""entrez le nombre de l'opération:
1 : addition
2 : soustraction
3 : multiplication
4 : division
5 : modulo
6 : puissance
opération : """))

if op == 1 : 
    result = nbr_1 + nbr_2
    print(f"{nbr_1} + {nbr_2} = {result}")
elif op == 2: print(f"{nbr_1} - {nbr_2} = {nbr_1 - nbr_2}")
elif op == 3: print(f"{nbr_1} * {nbr_2} = {nbr_1 * nbr_2}")
elif op == 4: print(f"{nbr_1} / {nbr_2} = {nbr_1 / nbr_2}")
elif op == 5: print(f"{nbr_1} % {nbr_2} = {nbr_1 % nbr_2}")
elif op == 6: print(f"{nbr_1} ** {nbr_2} = {nbr_1 ** nbr_2}")
else: print("Erreur: opération invalide")