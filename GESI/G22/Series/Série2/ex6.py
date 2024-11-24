"""Objectif : Comprendre l’utilisation des boucles infinies et la gestion des entrées utilisateur.
1. Écrivez un programme qui :
— Utilise une boucle ‘while‘ infinie pour répéter indéfiniment.
— À chaque itération, demande à l’utilisateur de saisir deux valeurs entières.
— Calcule la somme, la différence et le produit des deux valeurs.
— Si le deuxième nombre n’est pas zéro, calcule également la division entière, l’expo-
nentiation et le modulo.
— Affiche les résultats des opérations.
— Gère les cas où le deuxième nombre est zéro en affichant un message d’erreur appro-
prié."""

while True:
    nbr1 = int(input("Entrez un nombre: "))
    nbr2 = int(input("Entrez un autre nombre: "))
    
    print(f"{nbr1} + {nbr2} = {nbr1 + nbr2}")
    print(f"{nbr1} - {nbr2} = {nbr1 - nbr2}")
    print(f"{nbr1} * {nbr2} = {nbr1 * nbr2}")

    if nbr2 == 0:
        print("Division par zéro impossible")
    else:
        print(f"{nbr1} / {nbr2} = {nbr1 / nbr2}")
        print(f"{nbr1} % {nbr2} = {nbr1 % nbr2}")
        print(f"{nbr1} ** {nbr2} = {nbr1 ** nbr2}")
    
    print("_-"*10,"Fin de l'opération","_-"*10)
    continuer = input("Voulez-vous continuez? (O/N): ")
    if  continuer == "N" or continuer == "n":
        break

print("#"*15,"Fin du programme","#"*15)