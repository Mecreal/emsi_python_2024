# Calcule de IMC

print("Bienvenue au programme de calcul de l'IMC")

poids = float(input("entrez votre poids en kg :"))
taille = float(input("entrez votre taille en m :"))

imc = poids / taille ** 2

if imc < 18.5:
    print(f"Votre IMC est {imc:.2f}: Maigreur")
elif 18.5 <= imc < 25:
    print(f"Votre IMC est {imc:.2f}: Normal")
elif 25 <= imc < 30:
    print(f"Votre IMC est {imc:.2f}: Surpoids")
else:
    print(f"Votre IMC est {imc:.2f}: Obésité")

