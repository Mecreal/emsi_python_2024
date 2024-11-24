# calculatrice avec boucle infinie

while True:
    nbr1 = int(input("Entrez un nombre: "))
    nbr2 = int(input("Entrez un autre nombre: "))

    somme = nbr1 + nbr2
    diff = nbr1 - nbr2 
    produit = nbr1 * nbr2

    if nbr2 !=0:
        div =nbr1 /nbr2 
        modulo = nbr1%nbr2
    else :
        print("Error: division par zero")
        continue
    print(f"""{nbr1}+{nbr2} = {somme}
{nbr1}-{nbr2} = {diff}
{nbr1}*{nbr2} = {produit}
{nbr1}/{nbr2} = {div}
{nbr1}%{nbr2} = {modulo}
""")
    print("-_"*15,"Fin","-_"*15)

    continuer = input("Voulez-vous continuez? (o/n): ")
    if continuer.lower() != "o":
        break

print("Merci d'avoir utilisé notre calculatrice") 