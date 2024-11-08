"""
Objectif : Utiliser les opérateurs spéciaux is, is not, in, et not in.
1. Déclarez deux variables a et b avec la même valeur entière.
2. Utilisez l’opérateur is pour vérifier si a et b référencent le même objet.
3. Déclarez deux variables c et d avec la même chaîne de caractères.
4. Utilisez l’opérateur is not pour vérifier si c et d ne référencent pas le même objet.
5. Utilisez les opérateurs in et not in avec des chaînes de caractères pour vérifier la présence
ou l’absence de sous-chaînes.
"""

a = 10
b = 10

print("a is b : ", a is b)

print("a is not None : ", a is not None)

c = "Hello"
d = "Hello World"

print("c is d : ", c is d)

print("c is not d : ", c is not d)

print(c in d)

