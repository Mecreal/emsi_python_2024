# Calucler l'energie Cinétique d'un objet en mouvement

def energie_cinetique(masse, vitesse):
    ec = 0.5 * masse * vitesse ** 2
    return ec

m = 10 # kg
v = 15 # m/s
ec = energie_cinetique(m, v)

print(f"L'énergie cinétique de masse m = {m}kg et vitesse v = 15m/s \
l'objet est de {ec} J")


# 1. Ajouter une fonction qui calcule l'énergie potentielle d'un objet en mouvement

def energie_potentielle(masse, hauteur, g = 9.81):
    ep = masse * g * hauteur
    return ep

h = 10 # m

ep = energie_potentielle(m, h)

print(f"L'énergie potentielle de masse m = {m}kg et hauteur h = {h}m \
l'objet est de {ep:0.2f} J")

# 2. Energie mécanique

et = ec + ep

print(f"L'énergie mécanique de l'objet est de {et} J")