# Q1

frequence =  [2400,1800,2100,1900,2300,2000]

frequence.sort() # tri de la liste des frequences

print("Ma liste de frequences",frequence) # affichage de la liste des frequences pour visualisation

# Q2

if 2200 not in frequence: # si 2200 n'est pas dans la liste des frequences
    # frequence.insert(4,2200) # insertion de 2200 à la position 4
    for i in frequence:
        if i > 2200:
            frequence.insert(frequence.index(i),2200)
            break

print("Ma nouvelle liste de frequences",frequence) # affichage de la liste des frequences pour visualisation

# Q3

moyenne = sum(frequence)/len(frequence) # calcul de la moyenne des frequences

print(f"La moyenne des frequences est: {moyenne:.0f}") # affichage de la moyenne des frequences

# Q4

frequences_sup =[]
for i in frequence:
    if i >= 2000:
        frequences_sup.append(i)

# 2eme methode

frequences_sup = [i for i in frequence if i >= 2000]