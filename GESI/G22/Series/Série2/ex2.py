# IMC calculator

taille = float(input("entrez votre taille "))
poids = float(input("entrez votre poid"))

imc = poids / taille**2

if imc < 18.5:
    print("Maigreur")
elif 18.5 <= imc < 25:
    print("Normal")
elif 25 <= imc < 30:
    print("surpoids")
else:
    print("Obésité")