# Fonction imbriquer: ex4

def externe():
    def interne():
        print("Je suis a l'interieur de la fonction interne")
    interne()

    print("Je suis a l'exterieur de la fonction interne")

externe()
