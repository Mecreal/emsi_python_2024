frequences = [2400,1800,2100,1900,2300,2000]

frequences.sort() # trie la liste

if 2200 not in frequences:
    frequences.insert(4,2200)

print(frequences) # affiche la liste triée


# 3) Calcule de moyenne

moyenne = sum(frequences) / len(frequences)

print(f"La fréqunce moyenne est: {moyenne} Hz")

# M = 0
# S = 0

# for i in frequences:
#     S += i
# M = S / len(frequences)

# 4) Créez une nouvelle liste frequences_sup contenant uniquement les fréquences supérieures ou égales à 2000 Hz.

frequences_sup = [i for i in frequences if i >= 2000]

# Même chose que:
# frequences_sup = []
# for el in frequences:
#     if el >= 2000:
#         frequences_sup.append(el)

print(frequences_sup) # affiche la liste triée