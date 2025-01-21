from logistique import lire_coordonnees, tsp

# Fichier contenant les coordonnées des points
fichier = "coordonnees.txt"

# Lecture des coordonnées
points = lire_coordonnees(fichier)

# Résolution du TSP
chemin_optimal, distance_totale = tsp(points)

print(f"Chemin optimal : {chemin_optimal}")
print(f"Distance totale : {distance_totale}")
