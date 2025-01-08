fruits = ["pomme","banane","cerise"] # liste de fruits

fruits.append("orange") # ajoute orange a la liste

fruits.remove("banane") # supprime banane de la liste

print(fruits[2]) # affiche 3 eme element de la liste

print(fruits) # affiche la liste
# Ex 2

print(" Avant le tri: ", fruits)
fruits.sort() # trie la liste
print(" Après le tri: ", fruits) # affiche la liste triée
fruits.reverse() # inverse la liste
print(" Après l'inversion: ", fruits) # affiche la liste inversée

# print("cerise" in fruits) # affiche si cerise est dans la liste
if "cerise" in fruits:
    print("cerise est dans la liste")
else:
    print("cerise n'est pas dans la liste")