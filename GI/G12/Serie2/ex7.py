# factorial 

fact = 1

nombre = int(input("Entrez un nombre: "))

if nombre < 0:
    print("Désolé, le factoriel ne peut pas être calculé pour des nombres négatifs")
elif nombre == 0:
    print(f"{nombre}! = 1")
else:
    for i in range(1, nombre + 1):
        fact = fact * i
    print(f"{nombre}! = {fact}")