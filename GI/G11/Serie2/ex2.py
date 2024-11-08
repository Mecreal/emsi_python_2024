# Calculateur de IMC

print("Bienvenue au programme de calculateur de IMC")

poids = float(input("entrez votre poids en kg :"))
taille = float(input("entrez votre taille en m :"))

if taille <= 0 or poids <= 0:
    print("Erreur: Taille et poids doivent être positive")
    exit()

imc = poids / taille ** 2

if imc < 18.5:
    print(f"Votre IMC est {imc} : maigreur")
elif 18.5 <= imc < 25:
    print(f"Votre IMC est {imc} : corpulence normale")
elif 25 <= imc < 30:
    print(f"Votre IMC est {imc} : surpoids")
else:
    print(f"Votre IMC est {imc} : obésité")