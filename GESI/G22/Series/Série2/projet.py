"""
Projet Final - Jeu de Devine le Nombre
Objectif : Appliquer les connaissances sur les conditions et les boucles pour développer un
petit jeu interactif en Python.
1.8.1
Description du Projet
Créez un jeu où l’utilisateur doit deviner un nombre généré aléatoirement par le programme.
Le jeu doit inclure les fonctionnalités suivantes :
— Le programme génère un nombre secret entre 1 et 100.
— L’utilisateur a un nombre limité de tentatives (par exemple, 10).
— Après chaque tentative, le programme indique si le nombre secret est plus grand ou plus
petit que la tentative de l’utilisateur.
— Si l’utilisateur trouve le nombre avant d’épuiser les tentatives, il gagne. Sinon, il perd et
le programme révèle le nombre secret.
— À la fin du jeu, proposez à l’utilisateur de rejouer.
"""
from random import randint

print("Bienvenue dans le jeu de devine le nombre")



nbr_tentatives = 10
while 1:
    nbr_secret = randint(1,100)
    while nbr_tentatives > 0:
        nbr_tentatives -= 1
        print("Le jeu consiste à deviner un nombre secret entre 1 et 100")
        nbr = int(input("Entrez un nombre: "))
        if nbr == nbr_secret:
            print("Bravo! Vous avez trouvé le nombre secret")
            break
        elif nbr < nbr_secret:
            print("Le nombre secret est plus grand")
        else:
            print("Le nombre secret est plus petit")
        if nbr_tentatives == 0:
            print(f"Vous avez épuisé toutes vos tentatives. Le nombre secret était {nbr_secret}")
    continuee = input("Voulez-vous rejouer? (O/N): ")
    if continuee == "N" or continuee == "n":
        break
print("Fin du jeu")