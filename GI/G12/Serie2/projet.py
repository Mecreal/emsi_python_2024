# Jeu de Devine de nombre

from random import randint

print("Bienvenue au jeu de devine de nombre")

tentative_limite = 10

while 1:
    nombre_a_deviner = randint(1, 100)

    while tentative_limite > 0:
        tentative = int(input("Entrez un nombre: "))
        if tentative == nombre_a_deviner:
            print("Bravo! Vous avez deviné le nombre")
            break
        elif tentative < nombre_a_deviner:
            print("Le nombre est plus grand")
        else:
            print("Le nombre est plus petit")
        tentative_limite -= 1
        print(f"Il vous reste {tentative_limite} tentatives")
    else:
        print(f"Vous avez perdu! Le nombre était {nombre_a_deviner}")

    rejouer = input("Voulez-vous rejouer? (o/n): ")

    if rejouer == 'n' or 'N':
        break