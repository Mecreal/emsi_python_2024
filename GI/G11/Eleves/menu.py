from utils import *

def menu():
    list_eleves = load_eleves()

    while True:
        print("="*20, " ", "Menu", " ", "="*20)
        print("===============================================")
        print("1- Afficher tous les élèves")
        print("2- Afficher un élève par ID")
        print("3- Ajouter un élève")
        print("4- Supprimer un élève")
        print("5- Quitter")
        print("===============================================")
        choix = int(input("Votre choix: "))
        if choix == 1:
            affiche_all(list_eleves)
        elif choix == 2:
            ID = int(input("Donner l'ID de l'élève: "))
            affiche_by_ID(list_eleves, ID)
        elif choix == 3:
            add_eleve(list_eleves)
            save_eleves(list_eleves)
        elif choix == 4:
            ID = int(input("Donner l'ID de l'élève à supprimer: "))
            affiche_by_ID(list_eleves, ID)
            ouinon = input("Voulez-vous vraiment supprimer cet élève? (O/N): ")
            if ouinon.upper() == "O":
                delete_eleve(list_eleves, ID)
                save_eleves(list_eleves)
            elif ouinon.upper() == "N":
                print("Suppression annulée")
            else:
                print("Choix invalide")
        elif choix == 5:
            break
        else:
            print("Choix invalide")