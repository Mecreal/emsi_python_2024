compteur = 1 # initialisation du compteur

while compteur <= 10: # tant que le compteur est inferieur ou egal a 10
    if compteur % 3 == 0:
        print("Fizz") # affichage de Fizz si le compteur est divisible par 3
    else:
        print(compteur) # affichage du compteur
    compteur += 1 # incrementation du compteur