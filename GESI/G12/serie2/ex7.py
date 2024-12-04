# factorielle

nbr = int(input("Entrez un nombre: "))

fact = 1
if nbr < 0:
    print("Entrez un nombre positif")
else:

    for i in range(1, nbr+1):
        fact *= i
    print(f"{nbr}! = {fact}")
