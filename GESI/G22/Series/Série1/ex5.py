"""
Objectif : Utiliser les opérateurs spéciaux is, is not, in, et not in.
1. Déclarez deux variables a et b avec la même valeur entière.
2. Utilisez l’opérateur is pour vérifier si a et b référencent le même objet.
3. Déclarez deux variables c et d avec la même chaîne de caractères.
4. Utilisez l’opérateur is not pour vérifier si c et d ne référencent pas le même objet.
5. Utilisez les opérateurs in et not in avec des chaînes de caractères pour vérifier la présence
ou l’absence de sous-chaînes.
"""

a = 25
b = 25
c = "Bouchta"
d = "chta"
print(a is b)         # True
print(c is d)         # True
print("A" in "Alice") # True
print("Bob" not in "Alice") # True