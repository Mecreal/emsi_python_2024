# def des fonctions
def saluer():
    print("Bonjour tout le monde !")

# 2. Appel de la fonction

saluer()

# 3. fonction avec paramètre

def saluer2(nom):
    print(f"Bonjour, {nom} !")

# 4. Appel de la fonction avec paramètre

saluer2("Alice")
saluer2("Bob")
saluer2("Charlie")


# 5. Fonction avec plusieurs paramètres


def saluer3(nom, langue = "fr", salutation = "Bonjour"):
    if langue == "fr":
        print(f"{salutation}, {nom} !")
    elif langue == "en":
        print(f"Hello, {nom} !")
    elif langue == "es":
        print(f"Hola, {nom} !")
    elif langue == "de":
        print(f"Hallo, {nom} !")
    elif langue == "ar":
        print(f"السلام عليكم, {nom} !")
    else:
        print(f"Langue inconnue: {langue}")

# 6. Appel de la fonction avec plusieurs paramètres

saluer3("Alice")
saluer3("Bob", "en")
saluer3("Charlie", "es", "Hola")
saluer3("David", "de")
saluer3("علي", "ar")
saluer3("Eve", "it")
saluer3("Frank", "fr", "Salut")