# Jeu de dévinete

from random import randint

while 1:
    nbr = randint(1, 100)

    max_essais = 10

    while(max_essais > 0):
        essai = int(input("Entrez un nombre: "))
        if essai == nbr:
            print("Bravo! Vous avez deviné le nombre")
            break
        elif essai < nbr:
            print("Le nombre est plus grand")
        else:
            print("Le nombre est plus petit")
        max_essais -= 1
        print(f"Il vous reste {max_essais} essais")
    else:
        print(f"Vous avez perdu! Le nombre était {nbr}")
    
    print('-_'*10,"Fin du tour", '-_'*10)
    continuer = input("Voulez-vous continuez? (o/n): ")
    
    if continuer == "n" or continuer == "N":
        break
print("Merci pour le jeu!")


