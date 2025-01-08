frequences = [2400,1800,2100,1900,2300,2000]

frequences.sort() # trie la liste
print(frequences)
if 2200 not in frequences:
    for i in frequences:
        if i > 2200:
            frequences.insert(frequences.index(i),2200)
            break

# frequences.insert(4,2200)

# Calcul de la moyenne

moyenne = sum(frequences) / len(frequences)

print(f"La fréqunce moyenne est: {moyenne} Hz")

# Création d'une nouvelle liste frequences_sup contenant uniquement les fréquences supérieures ou égales à 2000 Hz.

frequences_sup = [i for i in frequences if i >= 2000]

# meme chose que:
# frequences_sup = []

# for el in frequences:
#     if el >= 2000:
#         frequences_sup.append(el)

print("La nouvelle liste est: ")
print(frequences_sup) # affiche la liste triée