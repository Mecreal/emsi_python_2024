# declaration de variables
produit = input("Entrez le nom du produit : ")
prix = float(input("Entrez le prix du produit : "))
quantite = int(input("Entrez la quantité du produit : "))
en_stock = True
rien = None


# affichage des variables
print(f" Produit : {produit}, Prix : {prix}, Quantite : {quantite}, En stock : {en_stock}")

# Compare this snippet from ex2.py:

# type de variables

print(f"Type de produit : {type(produit)}")
print(f"Type de prix : {type(prix)}")
print(f"Type de quantite : {type(quantite)}")
print(f"Type de en_stock : {type(en_stock)}")
print(f"Type de rien : {type(rien)}")

# adresse memoire des variables

print(f"Adresse memoire de produit : {id(produit)}")
print(f"Adresse memoire de prix : {id(prix)}")
print(f"Adresse memoire de quantite : {id(quantite)}")
print(f"Adresse memoire de en_stock : {id(en_stock)}")
print(f"Adresse memoire de rien : {id(rien)}")