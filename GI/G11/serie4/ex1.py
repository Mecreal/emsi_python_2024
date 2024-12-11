# definition de fonction 

def saluer():
    print("Bonjour tout le monde")

# appel de la fonction
saluer()

#3. fonction avec parametre

def saluer2(nom):
    print("Bonjour", nom)

saluer2("Alice")
saluer2("Bob")
saluer2("Charlie")

#4. fonction avec plusieurs parametres 

def saluer3(nom, lang = "fr"):
    if lang == "fr":
        print("Bonjour", nom)
    elif lang == "en":
        print("Hello", nom)
    elif lang == "es":
        print("Hola", nom)
    elif lang == "de":
        print("Guten Tag", nom)
    elif lang =="ar":
        print("مرحبا", nom)
    else:
        print("Langue inconnue")


saluer3("Alice", "fr")
saluer3("Bob", "en")
saluer3("Charlie", "es")
saluer3("David", "de")
saluer3("محماد", "ar")
saluer3("Eve", "it")
saluer3("Frank")