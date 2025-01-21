# Saisie des nombres
num1 = float(input("Entrez le premier nombre : "))
num2 = float(input("Entrez le second nombre : "))

# Menu des operations
print("Choisissez l'operation :")
print("1. Addition (+)")
print("2. Soustraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulo (%)")
print("6. Exponentiation (**)")
choix = input("Entrez le numero de l'operation : ")
# Calcul et affichage du resultat
if choix == '1':
    resultat = num1 + num2
    operation = "+"
elif choix == '2':
    resultat = num1 - num2
    operation = "-"
elif choix == '3':
    resultat = num1 * num2
    operation = "*"
elif choix == '4':
    if num2 != 0:
        resultat = num1 / num2
        operation = "/"
    else:
        resultat = "Erreur : Division par zero."
        operation = "/"
elif choix == '5':
    if num2 != 0:
        resultat = num1 % num2
        operation = "%"
    else:
        resultat = "Erreur : Modulo par zero."
        operation = "%"
elif choix == '6':
    resultat = num1 ** num2
    operation = "**"
else:
    resultat = "Erreur : Operation invalide."
    operation = ""
# Affichage du resultat
if isinstance(resultat, float) or isinstance(resultat, int):
    print(f"Resultat de {num1} {operation} {num2} = {resultat}")
else:
    print(resultat)