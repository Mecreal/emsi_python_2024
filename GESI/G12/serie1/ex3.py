# Opérateur de comparaison et logiques

x = 5
y = 3

# Opérateur de comparaison
egalite = x == y
difference = x != y
superieur = x > y
inferieur = x < y
superieur_ou_egal = x >= y
inferieur_ou_egal = x <= y

print(f" {x} == {y} = {egalite}")
print(f" {x} != {y} = {difference}")
print(f" {x} > {y} = {superieur}")
print(f" {x} < {y} = {inferieur}")
print(f" {x} >= {y} = {superieur_ou_egal}")
print(f" {x} <= {y} = {inferieur_ou_egal}")
print("-"*20," Fin de comparaison ","-"*20)


# Opérateur logique

a = True
b = False

et = a and b
ou = a or b
non_a = not a
non_b = not b

print(f" {a} and {b} = {et}")
print(f" {a} or {b} = {ou}")
print(f" not {a} = {non_a}")
print(f" not {b} = {non_b}")
print("-"*20," Fin de programme ","-"*20)

# combine comparaison et logique

x = 5
y = 3
z = 7

resultat = x > y and z > x
print(resultat)

resultat = x > y or z < x
print(resultat)

resultat = x > y and z < x
print(resultat)

resultat = x > y or z > x
print(resultat)