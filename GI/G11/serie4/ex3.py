x = 5

def afficher():
    global x
    x = 10
    print("Dans la fonction afficher, x =", x)

afficher()
print("Dans le programme principal, x =", x)