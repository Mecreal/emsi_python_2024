x = 5

def afficher():
    global x
    x = 10
    print("Dans la fonction, x =", x)

afficher()
print("En dehors de la fonction, x =", x)