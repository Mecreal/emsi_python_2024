import math
from itertools import permutations

# Calcul de la distance entre deux points
def calcul_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Lecture des coordonnées depuis un fichier
def lire_coordonnees(fichier):
    points = []
    if not fichier:
        with open(fichier, 'w') as temp: # si le fichier n'existe creer fichier vide
            temp.close()
    with open(fichier, "r") as f:
        for ligne in f:
            valeurs = ligne.strip().split(",")
            x = float(valeurs[0])
            y = float(valeurs[1])
            points.append((x, y))
    f.close()
    return points

# Algorithme du voyageur de commerce (TSP)
def tsp(points):
    chemins = permutations(points)
    meilleur_chemin = None
    distance_min = float("inf")

    for chemin in chemins:
        distance_totale = sum(calcul_distance(chemin[i], chemin[i + 1]) for i in range(len(chemin) - 1))
        if distance_totale < distance_min:
            distance_min = distance_totale
            meilleur_chemin = chemin

    return meilleur_chemin, distance_min
