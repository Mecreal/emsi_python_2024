# Calcule d'energie cinétique

def energie_cinetique(masse: float, vitesse: float) -> float:
    """
    Calcule l'énergie cinétique d'un objet
    Args:
     - masse: float, masse de l'objet en kg
     - vitesse: float, vitesse de l'objet en m/s
    Returns:
     - float, l'énergie cinétique de l'objet en J
    """
    return 0.5 * masse * vitesse ** 2

m = 10 # kg
v = 15 # m/s

ec = energie_cinetique(m, v)

print(f"L'énergie cinétique d'un objet de masse \
{m} kg et de vitesse {v} m/s est de {ec} J")

# Calcule d'energie potentielle

def energie_potentielle(masse: float, hauteur: float, g: float=9.81) -> float:
    """
    Calcule l'énergie potentielle d'un objet
    Args:
     - masse: float, masse de l'objet en kg
     - hauteur: float, hauteur de l'objet en m
     - g: float, accélération de la pesanteur en m/s^2
    Returns:
     - float, l'énergie potentielle de l'objet en J
    """
    return masse * g * hauteur

h = 5 # m

ep = energie_potentielle(m, h)

print(f"L'énergie potentielle d'un objet de masse \
{m} kg et de hauteur {h} m est de {ep} J")

# Calcule d'energie mécanique

em = ec + ep

print(f"L'énergie mécanique d'un objet de masse \
{m} kg, de vitesse {v} m/s et de hauteur {h} m est de {em} J")