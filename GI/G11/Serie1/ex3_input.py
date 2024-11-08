"""
Objectif : Comparer des variables et utiliser des opérateurs logiques.
1. Déclarez deux variables x et y avec des valeurs numériques.
2. Comparez ces variables en utilisant tous les opérateurs de comparaison et affichez les
résultats.
3. Déclarez deux variables booléennes c et d.
4. Utilisez les opérateurs logiques and, or, et not sur ces variables et affichez les résultats.
"""

x = float(input("entrer la première valeur! "))
y = float(input("entrer la deuxième valeur: "))

egalite = (x == y)

print("vérification de l'égalité entre x et y donne:", egalite)

print("diffirence ", x!=y)

print("x est plus grand que y", x>y)

print("x est plus petit que y", x<y)
      
print("x est plus grand ou égal à y", x>=y)

print("x est plus petit ou égal à y", x<=y)

c = True
d = False

print("c et d", c and d)

print("c ou d", c or d)

print("non c", not c)

print("non d", not d)