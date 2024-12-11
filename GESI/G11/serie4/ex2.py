# Energie Cinétique

def energie_cinetique(masse: float, vitesse: float) -> float:
    """
    Calcul de l'énergie cinétique
    
    Args:
    :masse (float): masse de l'objet en kg
    :vitesse (float): vitesse de l'objet en m/s

    Returns:
    float: énergie cinétique en Joules
    """
    return 0.5 * masse * vitesse ** 2

masse = 10 # kg
vitesse = 15 # m/s

ec = energie_cinetique(masse, vitesse)

print(f"L'énergie cinétique d'un obj de m= {masse}kg \
et v = {vitesse}  m/s est de {ec} J")

# 2. Energie Potentielle

def energie_potentielle(masse: float, hauteur: float) -> float:
    """
    Calcul de l'énergie potentielle

    Args:
    :masse (float): masse de l'objet en kg
    :hauteur (float): hauteur de l'objet en m
    
    Returns:
    float: énergie potentielle en Joules
    """
    g = 9.81
    return masse * g * hauteur

h = 10 # m

ep = energie_potentielle(masse, h)

print(f"L'énergie potentielle d'un obj de m= {masse}kg \
et h = {h} m est de {ep} J")

# 3. Energie Mécanique

et = ec + ep

print(f"L'énergie mécanique d'un obj de m= {masse}kg, v = {vitesse} m/s \
et h = {h} m est de {et} J")