# définition de fonction 

def saluer():
    print("Bonjour tout le monde !")

# Appel de la fonction saluer

saluer()

# 3. fonction avec parametre

def saluer2(nom):
    print("Bonjour", nom, "!")

# Appel de la fonction saluer2

saluer2("Alice")
saluer2("Bob")
saluer2("Charlie")


# 4. fonction avec plusieurs parametres

def saluer3(nom, lang = "fr", salutation = "Bonjour"):
    if lang == "fr":
        print(salutation, nom, "!")
    elif lang == "en":
        print("Hello", nom, "!")
    elif lang == "es":
        print("Hola", nom, "!")
    elif lang == "de":
        print("Guten Tag", nom, "!")
    elif lang == "it":
        print("Ciao", nom, "!")
    elif lang == "ar":
        print("السلام عليكم", nom, "!")
    else:
        print("Langue inconnue")


# Appel de la fonction saluer3

saluer3("Alice")
saluer3("Bob", "en")
saluer3("Charlie", "es")
saluer3("David", "de")
saluer3("Eve", "it")
saluer3("فاطمة", "ar")
saluer3("Gérard", "fr", "Salut")
saluer3("Hélène", "df", "Coucou")