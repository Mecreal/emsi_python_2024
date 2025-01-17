# exercice 6 et 7

# Q 1
composants : dict = {"Resistance": 150,
                    "Condensateur": 80,
                    "Inductance": 60,
                    "Transistor": 45
                    }
# Q 2
print(f"J'ai {composants['Condensateur']} condensateurs")
# Q 3
composants["Resistance"] += 50

# Q 4
composants.update({"Diode": 30, "Microcontroleur": 20})

print(composants)

# Q 5
composants.pop("Inductance")

# Methode deux 

# del(composants["Inductance"])


# Exercice 7

# Q 1

print(" les composants disponible sont ",list(composants.keys()))
print(" les quantites des composants sont ",list(composants.values()))


# Q 2

print("J'ai ",composants.get("Transistor", 0)," Transistor")
print("J'ai ",composants.get("Capteur", 0)," capteurs")

# Q 3

def description_composants(composants):

    description = ""
    for composant, quantite in composants.items():
        description += f"{composant}: {quantite}\n"
    return description

print(description_composants(composants))

# Q 4

composant_sup= {
    "Capteur": 25,
    "Relay": 15
}


composants.update(composant_sup)
print("#"*50)
print(description_composants(composants))