
from utils import *
import json


liste_eleves = load_eleves()
while True:
    print("-_"*10,"","Menu","","-_"*10)
    print("1: Afficher tous les eleves")
    print("2: Afficher un eleve par ID")
    print("3: Ajouter un eleve")
    print("4: Supprimer un eleve")
    print("5: Quitter")
    print("-_-_"*10)
    choix = int(input("Entrez votre choix: "))
    if choix == 1:
        affiche_tous(liste_eleves)
    elif choix == 2:
        ID = int(input("Entrez ID: "))
        affiche_par_ID(liste_eleves, ID)
    elif choix == 3:
        add_eleve(liste_eleves)
        stockage(liste_eleves)
    elif choix == 4:
        print("Suppression d'un eleve")
        ID = int(input("Entrez ID: "))
        if delete(liste_eleves, ID):
            print("Eleve supprime")
            stockage(liste_eleves)
        else:
            print("Eleve non trouve")
    elif choix == 5:
        break
    else:
        print("Choix invalide")
print("Merci d'avoir utilise notre programme")