from utils import *

def menu():
    list_eleves = load_eleves()
    while True:
        print("#"*15," ","Menu"," ","#"*15)
        print("1. Afficher tous les élèves")
        print("2. Afficher un élève par ID")
        print("3. Ajouter un élève")
        print("4. Supprimer un élève")
        print("5. Quitter")
        choix = input("Votre choix: ")
        if choix == '1':
            affiche_all(list_eleves)
        elif choix == '2':
            id = input("ID de l'élève: ")
            affiche_by_ID(list_eleves, id)
        elif choix == '3':
            add_eleve(list_eleves)
            save_eleves(list_eleves)
        elif choix == '4':
            delete_eleve(list_eleves, int(input("ID de l'élève: ")))
            save_eleves(list_eleves)
        elif choix == '5':
            break
        else:
            print("Choix invalide")
        print("="*45)
        