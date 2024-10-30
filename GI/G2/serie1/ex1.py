# Serie 1 ex1 : déclaration et utilisation de variable

nombre = 10
prix = 10000.00
produit = "Ordinateur"
en_stock = False

print("Nom de produit :",produit)
print("nombre :",nombre)
print("prix :",prix)
print("en_stock",en_stock)


# Methode d'affichage

print(f"le produit {produit}, la quantité est {nombre} \n en stock : {en_stock} et son prix est : {prix} DHs ")

# 3eme méthode :

print(
    f"""
le produit : {produit} 
la quantité : {nombre}
Est en stock : {en_stock} 
prix est : {prix} DHs
""")



# Utilisation de type ()
print ( " Type de nombre : " , type ( nombre ) )
print ( " Type de prix : " , type ( prix ) )
print ( " Type de produit : " , type ( produit ) )
print ( " Type de en_stock : " , type ( en_stock ) )
# Utilisation de id ()
print ( " ID de produit : " , id ( produit ) )
print ( " ID de prix : " , id ( prix ) )
print ( " ID de produit : " , id ( produit ) )
print ( " ID de en_stock : " , id ( en_stock ) )