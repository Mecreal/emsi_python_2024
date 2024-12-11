# definir une fonction sans parametre
def saluer():
    print("Bonjour tout le monde!")

#2 appeler la fonction
saluer()

#3 definir une fonction avec un parametre
def saluer2(nom):
    print(f"Bonjour {nom} !")

#4 appeler la fonction
saluer2("Dawya")
saluer2("Bouchta")
saluer2("Rkiya")


#5 definir une fonction avec plusieurs parametres
def saluer3(nom, lang = "fr", salutation="Bonjour"):
    if lang == "fr":
        print(f"{salutation} {nom} !")
    elif lang == "ar":
        print(f"مرحبا {nom} !")
    elif lang == "en":
        print(f"Hello {nom} !")
    elif lang == "es":
        print(f"Hola {nom} !")
    elif lang == "de":
        print(f"Hallo {nom} !")
    else:
        print(f"Langue non supportée")

#6 appeler la fonction
saluer3("Dawya")
saluer3("محمد", "ar")
saluer3("Rkiya", "en")
saluer3("Asmaa", "es")
saluer3("Mohamed", "de")
saluer3("Mohamed", "it", "Ciao")
saluer3("Mohamed", "jp", "こんにちは")
