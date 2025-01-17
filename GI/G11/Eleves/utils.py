import json as js


def affiche_eleve(eleve: dict= None):
    if eleve is None:
        print("Eleve non trouvé")
        return
    print("-"*20, " ", f"Eleve d'ID : {eleve["ID"]}", " ", "-"*20)
    for cle, valeur in eleve.items():
        if cle == "ID":
            continue
        print(f"{cle}: {valeur}")
    print("_"*60)


def affiche_all(liste_eleves: list):
    if len(liste_eleves) == 0:
        print("Aucun eleve trouvé")
        return
    print("-"*15,f"Liste des {len(liste_eleves)} eleves","-"*15)
    print("_-"*30)
    for eleve in liste_eleves:
        affiche_eleve(eleve)
    print("_+"*30)


def affiche_by_ID(liste_eleves: list, ID: int = 0):
    for eleve in liste_eleves:
        if eleve["ID"] == ID:
            affiche_eleve(eleve)
            return
    affiche_eleve(None)


def add_eleve(liste_eleves: list):
    ID = liste_eleves[-1]["ID"] + 1 if len(liste_eleves) > 0 else 1
    print("Ajout d'un nouvel eleve, veuillez remplir les informations suivantes:")
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
    liste_eleves.append(eleve)
    print("Eleve ajouté avec succès")

def delete_eleve(liste_eleves: list, ID: int):
    for eleve in liste_eleves:
        if eleve["ID"] == ID:
            liste_eleves.remove(eleve)
            print("Eleve supprimé avec succès")
            return
    print("Eleve non trouvé")



def load_eleves(path: str="eleves.json"):
    try:
        with open(path, "r") as f:
            return js.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        print("Erreur lors du chargement des données")
        print(e)
        return []

    
def save_eleves(liste_eleves: list, path: str="eleves.json"):
    with open(path, "w") as f:
        js.dump(liste_eleves, f, indent=4)

