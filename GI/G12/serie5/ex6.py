composants_stock = {
    "Résistance": 150,
    "Condensateur": 80,
    "Inductance": 60,
    "Transistor": 45
}

#Q 2

print(f"Stock de condensateur :  {composants_stock["Condensateur"]}")

#Q 3

composants_stock["Résistance"] += 50

#Q 4

composants_stock.update({"Diode": 30, "Microcontrôleur": 20})

#Q 5

composants_stock.pop("Inductance")

# Autres Methodes

# del(composants_stock["Inductance"])


## Ex 7

print("Clefs du dictionnaire : ", composants_stock.keys())
print("Valeurs du dictionnaire : ", composants_stock.values())

#Q 2

print("Stock de transisteur : ", composants_stock.get("Transistor",0))
print("Stock de Capteur : ", composants_stock.get("Capteur",0))


#Q 3

for k, v in composants_stock.items():
    print(f"Composant : {k} | Stock : {v}")


#Q 4

composants_additionnels = {"Capteur": 25, "Relay": 15}

composants_stock.update(composants_additionnels)

print("#"*30)
# additionnel
def description_stock_composants(c_S: dict) -> str:
    description = ""
    for k, v in c_S.items():
        description += f"Composant : {k} | Stock : {v}\n"
    return description

print(description_stock_composants(composants_stock))