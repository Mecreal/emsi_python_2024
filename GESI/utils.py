
import json
def print_dict(eleve):
    for k, v in eleve.items():
            print(f"{k} : {v}")

def affiche_tous(list_elev :list):
    for eleve in list_elev:
        print_dict(eleve)
        print("#"*40)


def affiche_par_ID(list_elev:list, ID:int):
    for eleve in list_elev:
        if ID == eleve["ID"]:
            print_dict(eleve)

def add_eleve(list_eleve):
    ID = len(list_eleve) + 1
    Nom = input("Entrez Nom: ")
    prenom = input("Entrez prenom: ")
    age = int(input("Entrez age:"))

    eleve = {
         "ID": ID,
         "Nom": Nom,
         "Prenom": prenom,
         "Age": age
    }
    list_eleve.append(eleve)


def stockage(list_eleve, path = "eleves.json"):
    with open(path, "w") as f:
        json.dump(list_eleve, f, indent=4)

def load_eleves(path = "eleves.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def delete(list_eleve, ID):
    for eleve in list_eleve:
        if ID == eleve["ID"]:
            list_eleve.remove(eleve)
            return True
    return False



