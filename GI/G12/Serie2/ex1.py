# vérifier pair ou impair

print("Bienvenue au programme pour vérifier si un nombre est pair ou impair")

nbr = int(input("entrez un nombre :"))

if nbr % 2 == 0:
    print(f"Le nombre {nbr} est pair")
else:
    print(f"Le nombre {nbr} est impair")