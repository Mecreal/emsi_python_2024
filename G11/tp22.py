# declaration de variable 

nombre = 23
prix = 23.45
produit = "OMo"
en_stock =True
rien = None

# print(
#     " Le produit",produit,
#     "exist =", en_stock,
#     "Qt :", nombre,
#     "prx :", prix,
#     rien
#     )
print(
    f"""Le produit {produit},
exist = {en_stock},
Qt : {nombre},
Prx : {prix},
{rien}
""")


print(f"le type de nombre est {type(nombre)}") # Type de variable