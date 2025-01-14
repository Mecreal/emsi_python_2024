composants_stock = {
    "Résistances": 150,
    "Condensateurs": 80,
    "Inductances": 60,
    "Transistors": 45
}

#Q2

print("La quantité Condensateurs: ",composants_stock["Condensateurs"])

#Q3

composants_stock["Résistances"] += 50
print("La valeur Résistances: ",composants_stock["Résistances"])

#Q4
composants_stock["Diodes"] = 30
composants_stock["Microcontrôleurs"] = 20

del(composants_stock["Inductances"])

print(composants_stock)


# EX7 

#Q1
print("Les clés du dictionnaire sont: ",composants_stock.keys())
print("Les valeurs du dictionnaire sont: ",composants_stock.values())

#Q2
print("La valeur de Transistors: ",composants_stock.get("Transistors",0))
print("La valeur de Capteurs: ",composants_stock.get("Capteurs",0))

#Q3
print("#"*40)
for k,v in composants_stock.items():
    print(f"Composant: {k}, Quantité: {v}")

#Q4

composants_supp = {"Capteur" : 25, "Relay": 15}

composants_stock.update(composants_supp)


print("#"*40)

def afficher_stock_composants(stock:dict) -> None:
    """Affiche le stock de composants"""
    
    for k,v in stock.items():
        print(f"Composant: {k}, Quantité: {v}")


afficher_stock_composants(composants_stock)

