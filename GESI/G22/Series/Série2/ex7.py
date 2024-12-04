# factorial 

nombre = int(input("Entrez un nombre: "))
fact = 1
if nombre < 0:
    print("Le factoriel d'un nombre négatif n'existe pas")
    exit()

for i in range(1, nombre + 1):
    fact *= i
print(f"{nombre}! = {fact}")