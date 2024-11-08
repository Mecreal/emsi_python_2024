# Déclaration de variable et afichge de la valeur de la variable

# Déclaration de variable
produit = "Ordinateur"
nombre = 10
prix = 1000.0
en_stock = True

# Affichage de la valeur de la variable
print("Produit: ", produit, "\nNombre: ", nombre, "\nPrix: ", prix, "\nEn stock: ", en_stock)

# Affichage de la valeur de la variable Méthode 2
print("#"*30,"Méthode 2:",sep="\n")
print(f"Produit: {produit}\nNombre: {nombre}\nPrix: {prix}\nEn stock: {en_stock}")

# Affichage de la valeur de la variable Méthode 3
print("#"*30,"Méthode 3:",sep="\n")

print(f"""
Produit: {produit}
Nombre: {nombre}
Prix: {prix}
En stock: {en_stock}
""")

# Affichage de la valeur de la variable Méthode 4
print("#"*30,"Méthode 4:",sep="\n")

print("""
Produit: {:s}
Nombre: {:d}
Prix: {:.1f}
En stock: {:b}
""".format(produit, nombre, prix, en_stock))