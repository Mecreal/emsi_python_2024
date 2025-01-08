frequences = [2400, 1800, 2100, 1900, 2300, 2000]

print("Liste des fréquences : ", frequences)

frequences.sort()

print("Liste des fréquences triée : ", frequences)

# 2
if 2200 not in frequences:
    for i in frequences:
        if i > 2200:
            frequences.insert(frequences.index(i), 2200)
            print("Liste des fréquences avec 2200 ajoutée : ", frequences)
            break
else:
    print("La fréquence 2200 est déjà dans la liste")

# 3

moyenne = sum(frequences) / len(frequences)

print(f"La moyenne des fréquences est :  {moyenne:.0f}")

# 4

frequences_sup = []
for i in frequences:
    if i > 2000:
        frequences_sup.append(i)

print("Liste des fréquences supérieures à 2000 : ", frequences_sup)

    
