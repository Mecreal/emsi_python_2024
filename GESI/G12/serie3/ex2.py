# labyrinthe

from random import randint
from time import sleep


print(" Bienvenue")

score = 0

while 1:
    dice = randint(1, 6)
    print(f"Vous avez obtenu {dice}")
    score += dice

    if score % 7 ==0:
        score -= 3
        print("Vous avez recule 3 points")
        print(f"Votre score est de {score}")
    elif score % 13 == 0 and score < 50:
        continue
    elif score == 50:
        print(f"Vous avez obtenu gagner!")
        break
    elif score > 50:
        print(f"votre score est de {score}")
        score -= dice
    else:
        print(f"Votre score est de {score}")
        continue
    sleep(5)
print("Merci pour le jeu!")
