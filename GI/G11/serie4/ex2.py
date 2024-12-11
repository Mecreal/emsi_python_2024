# définition des fonctions

# Energie cinetique
def energie_cinetique(masse, vitesse):
    return 0.5 * masse * vitesse ** 2

# Energie potentielle
def energie_potentielle(masse, hauteur, g=9.81):
    return masse * g * hauteur

m = 10 # kg
v = 15 # m/s
h = 10 # m

ec = energie_cinetique(m, v)
ep = energie_potentielle(m, h)

print(f"L'objet de masse {m}kg, de vitesse {v} m/s et de hauteur {h} m a:")
print(f"Energie cinetique de {ec} Joules")
print(f"Energie potentielle de {ep:0.2f} Joules")
print(f"Energie mecanique de {ec + ep} Joules")

