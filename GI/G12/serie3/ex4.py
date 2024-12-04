# Somme des N premiers nombres entiers

somme = 0
N = int(input("Entrez un nombre: "))

for i in range(1, N + 1):
    somme += i

print(f"La somme des {N} premiers nombres entiers est {somme}")