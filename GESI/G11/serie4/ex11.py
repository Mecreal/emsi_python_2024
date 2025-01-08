# Exercice 11 : Recherche Dichotomique (Binary Search)
# Contexte
# — Description : La recherche dichotomique est une méthode efficace pour trouver
# un élément dans une liste triée en divisant l’espace de recherche par deux à chaque
# étape.
# Implémentation
# — Créez une fonction récursive recherche_dichotomique(liste, element, debut,
# fin) qui retourne l’indice de l’élément recherché ou -1 s’il n’est pas trouvé.
# — Testez la fonction avec une liste triée de nombres et différents éléments à rechercher.
# — Réponse attendue :
# L’élément 14 se trouve à l’indice 6.


def recherche_dichotomique(liste, element, debut, fin):
    if fin >= debut:
        mid = debut + (fin - debut) // 2
        if liste[mid] == element:
            return mid
        elif liste[mid] > element:
            return recherche_dichotomique(liste, element, debut, mid - 1)
        else:
            return recherche_dichotomique(liste, element, mid + 1, fin)
    else:
        return -1
    
liste = [1, 2, 3, 4, 5, 6, 14, 15, 16, 17, 18, 19, 20]
element = 14

result = recherche_dichotomique(liste, element, 0, len(liste) - 1)
if result != -1:
    print(f"L’élément {element} se trouve à l’indice {result}")
else:  
    print(f"L’élément {element} n'est pas trouvé")
