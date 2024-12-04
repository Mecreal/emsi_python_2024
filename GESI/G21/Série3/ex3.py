# tableau de multiplication

# 1. Écrivez un programme qui affiche le tableau de multiplication d'un nombre donné par l'utilisateur.

nbr = int(input("Entrez un nombre: "))

for i in range(1, 11):
    print(f"{nbr} x {i} = {nbr * i}")

