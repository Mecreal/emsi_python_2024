
prix = 23.45
produit = "OMo"
en_stock =True
rien = None
nombre =  int(input(f" Donner ne nomre de {produit} en stock: "))


print(
    f"""Le produit {produit},
exist = {en_stock},
Qt : {nombre},
Prx : {prix},
{rien}
""")


print(f"le type de nombre est {type(nombre)}") # Type de variable