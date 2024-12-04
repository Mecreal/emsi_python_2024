# Labyrinthe 

# 1. Importation des modules
from random import randint
from time import sleep

# 2. Initialisation des variables
score = 1
tour = 1
# boucle pour rejouer
while True:
    print()
    print(f"Tour {tour}:")
    tour += 1
    dice = randint(1, 6)
    print(f"Vous avez obtenu {dice} points")
    score += dice
    print(f"Votre score est de {score} points")
    if score == 50:
        print("Bravo! Vous avez gagné")
        break
    elif score > 50:
        print("Vous avez dépassé 50 points.\
reculez à la case précédente")
        score -= dice
        print(f"Votre score est de {score} points")
    elif score % 7 == 0:
        print("Vous avez obtenu un multiple de 7.\
Reculez 3 cases")
        score -= 3
        print(f"Votre score est de {score} points")
    elif score % 13 == 0:
        print("Vous avez obtenu un multiple de 13.")
        tour += 1
        sleep(1)
        print("Vous avez sauté un tour")
        continue
    sleep(1)



            