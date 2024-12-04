# Labyrinthe
from random import randint
from time import sleep

print("Bienvenue dans le jeu du labyrinthe")

score = 1

while True:
    dice = randint(1, 6)
    print(f"Vous avez obtenu {dice}")
    score += dice
    print(f"Votre score est de {score}")

    if score == 50:
        print("Bravo! Vous avez gagné")
        break
    elif score > 50:
        score -= dice
        print("Vous avez dépassé 50, vous devez obtenir un nombre exact pour gagner")
    elif score % 7 == 0:
        score -= 3
        print("Vous êtes tombé sur un piège, vous reculez de 3 cases")
    elif score % 13 == 0:
        continue 

    sleep(0.5) # Pause de 0.5 secondes

print("Fin du jeu")