import json

def print_dict(eleve:dict):
    print("Information sur l'eleve:")
    for k, v in eleve.items():
            print(f"{k} : {v}")


def affiche_tous(list_elev):
    print("Liste de tous les eleves")
    print(f"Nombre d'eleves: {len(list_elev)}")
    if len(list_elev) == 0:
        print("Aucun eleve")
    else:
        for eleve in list_elev:
            print_dict(eleve)
            print("#"*40)



def affiche_par_ID(list_elev:list, ID:int):
    for eleve in list_elev:
        if ID == eleve["ID"]:
            print_dict(eleve)
        else:
            print("Eleve non trouve")


def add_eleve(list_eleve = []):
    ID = list_eleve[-1]["ID"] + 1 if len(list_eleve) else 1
    Nom = input("Entrez Nom: ").strip()
    prenom = input("Entrez prenom: ").strip()
    age = int(input("Entrez age:"))
    email = Nom+prenom+"@emsi-edu.ma"
    email = email.strip()

    eleve = {
         "ID": ID,
         "Nom": Nom,
         "Prenom": prenom,
         "Age": age,
         "email": email
    }
    list_eleve.append(eleve)


def delete(list_eleve, ID):
    for eleve in list_eleve:
        if ID == eleve["ID"]:
            list_eleve.remove(eleve)
            print("Eleve supprime")
            return True
    print("Eleve non trouve")
    return False

def stockage(list_eleve, path = "eleves.json"):
    with open (path, "w") as f:
        json.dump(list_eleve, f, indent=4)

def load_eleves(path = "eleves.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []