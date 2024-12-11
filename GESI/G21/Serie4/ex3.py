x = 5

def affichage():
    global x
    x = 10
    print("Dans la fonction: x=", x)

affichage()
print("Hors de la fonction: x=", x)
