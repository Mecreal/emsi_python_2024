# Calcule de l'energie cinetique

# 1. Définir une fonction qui prend en paramètre la masse et la vitesse d'un objet et qui retourne l'énergie cinétique de cet objet.

def energie_cinetique(masse, vitesse):
    return 0.5 * masse * vitesse ** 2

m = 10 # kg
v = 15 # m/s
Ec = energie_cinetique(m, v)

print(f"L'énergie cinétique de l'objet \
de m = {m}kg et v = {v} m/s \
est {Ec} J")

# Additionnel

# Energie potentielle gravitationnelle

def energie_potentielle_gravitationnelle(masse, hauteur, g = 9.81):
    return masse * g * hauteur

h = 10 # m
Ep = energie_potentielle_gravitationnelle(m, h)

print(f"L'énergie potentielle gravitationnelle de l'objet \
de m = {m}kg et h = {h} m est {Ep:.2f} J")

# Energie mécanique

Em = Ec + Ep

print(f"L'énergie mécanique de l'objet \
de m = {m}kg, v = {v} m/s et h = {h} m est {Em:.2f} J")