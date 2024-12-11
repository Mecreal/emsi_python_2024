# Définition de fonction

def saluer():
    print("Bonjour le monde!")

# Appel de la fonction
# saluer()

# fonction avec des parameters

def saluer2(nom):
    print(f"Bonjour, {nom}!")

# saluer2("Alice")
# saluer2("Bob")
# saluer2("Charlie")


# fonction avec des parameters par défaut

def saluer3(
        nom: str,
        lang: str="fr",
        salutation: str="Bonjour") -> None:
    if lang == "fr":
        print(f"{salutation}, {nom}!")
    elif lang == "en":
        print(f"Hello, {nom}!")
    elif lang == "de":
        print(f"Hallo, {nom}!")
    elif lang == "es":
        print(f"Hola, {nom}!")
    elif lang == "it":
        print(f"Ciao, {nom}!")
    elif lang == "ar":
        print(f"السلام عليكم, {nom}!")
    elif lang == "ja":
        print(f"こんにちは, {nom}!")
    else:
        print(f"Language {lang} not supported")
    
saluer3("Alice")
saluer3("Bob", "en")
saluer3("Charlie", "de")
saluer3("David", "es")
saluer3("Eve", "it")
saluer3("المعطي", "ar")
saluer3("Fumi", "ja")
saluer3("Grace", "fr", "Salut")
