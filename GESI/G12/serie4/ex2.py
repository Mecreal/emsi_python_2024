# calculer l'energie cinétique


def energie_cinetique(masse, vitesse):
    """
    Calculer l'energie cinétique
    :param masse: float : masse de l'objet en kg
    :param vitesse: float : vitesse de l'objet en m/s
    :return: float : energie cinétique de l'objet en J
    """
    return 1/2 * masse * vitesse**2

m = 10
v = 15
en_cin = energie_cinetique(m, v)

print(f" l'energie cinétique d'un object de masse 10 kg et vitesse 15 m/s est :\
 {en_cin:0.2f} J")


def energie_potentiel(masse, hauteur):
    """
    Calculer l'energie potentielle
    :param masse: float : masse de l'objet en kg
    :param hauteur: float : hauteur de l'objet en m
    :param g: float : acceleration de la gravité en m/s^2
    :return: float : energie potentielle de l'objet en J
    """
    g = 9.81
    return masse * g * hauteur

h = 10

en_pot = energie_potentiel(m, h)

print(f" l'energie potentielle d'un object de masse 10 kg et hauteur 10 m est :\
 {en_pot:0.2f} J")

print(f" l'energie totale d'un object de masse 10 kg et hauteur 10 m est :\
{en_cin + en_pot:0.2f} J")