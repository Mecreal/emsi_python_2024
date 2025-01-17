import json as js

def affiche_eleve(eleve: dict):
    for cle, valeur in eleve.items():
        print(f"{cle}: {valeur}")


def affiche_by_ID(list_eleves: list, ID: int = 0):
    for eleve in list_eleves:
        if eleve["ID"] == ID:
            affiche_eleve(eleve)
            return
    print("Eleve non trouvé")


def affiche_all(list_eleves: list):
    if len(list_eleves) == 0:
        print("Aucun eleve trouvé")
        return
    print(f"Liste des {len(list_eleves)} eleves")
    print("_"*60)
    for eleve in list_eleves:
        affiche_eleve(eleve)
        print("_-"*30)


def add_eleve(list_eleves: list):
    ID = list_eleves[-1]["ID"] + 1 if len(list_eleves) > 0 else 1
    Nom = input("Nom: ").strip()
    Prenom = input("Prenom: ").strip()
    Age = int(input("Age: "))
    Classe = input("Classe: ")
    Email = Nom + "." + Prenom + "@emsi-edu.ma"
    Email = Email.lower().replace(" ", ".")
    eleve = {
        "ID": ID,
        "Nom": Nom,
        "Prenom": Prenom,
        "Age": Age,
        "Classe": Classe,
        "Email": Email
    }
    list_eleves.append(eleve)
    print("Eleve ajouté avec succès")



def delete_eleve(list_eleves: list, ID: int):
    for eleve in list_eleves:
        if eleve["ID"] == ID:
            list_eleves.remove(eleve)
            print("Eleve supprimé avec succès")
            return
    print("Eleve non trouvé")


def save_eleves(list_eleves: list, path: str="eleves.json"):
    with open(path, "w") as f:
        js.dump(list_eleves, f, indent=4)

def load_eleves(path: str="eleves.json"):
    try:
        with open(path, "r") as f:
            return js.load(f)
    except:
        return []