# while infinie 


while True:
    nombre1 = int(input("Saisir un nombre positive entier:"))
    nombre2 = int(input("Saisir un nombre positive entier:"))

    somme = nombre1 + nombre2
    diff = nombre1 - nombre2
    mult = nombre1 * nombre2

    if nombre2 == 0:
        print("Division par zero impossible")
        continue
    else:
        div = nombre1 / nombre2
        mod = nombre1 % nombre2


    print(f"""la somme: {somme}
    soustraction : {diff}..""")
        