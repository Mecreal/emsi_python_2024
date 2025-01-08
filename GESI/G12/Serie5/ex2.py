print("Avant import")

from ex1 import fruits

print("Apres import")
fruits.sort() # tri de la liste
print("Ma liste trier",fruits)

# Q2
fruits.reverse() # renversement de la liste
print("Ma liste renverser",fruits)

# Q3
print("Est ce que cerise est présente\
 dans ma liste ?", " cerise ".strip() in fruits)