# Salutation pour chaque langue

def saluer3(nom, lang = "fr", salutation = "Bonjour"):
    if lang == "fr":
        print(f"{salutation} {nom}!")
    elif lang == "ar":
        print(f"السلام عليكم {nom}!")
    elif lang == "en":
        print(f"Hello {nom}") 
    else:
        print("Langue inconnue")

saluer3("Charlie",'fr','Salut')
saluer3("John",'en')
saluer3("Charlie",'fr')
saluer3("Charlie",'ar')
saluer3("Charlie",'it')
