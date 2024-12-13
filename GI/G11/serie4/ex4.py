#fonction imbriquee

def extern():
    print("1/Je suis à l'exterieur de la fonction interne")
    def interne():
        print("Je suis à l'interieur de la fonction interne")
    
    print("2/Je suis à l'exterieur de la fonction interne")
    interne()

print("début")
extern()
print("fin")