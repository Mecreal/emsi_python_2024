# ex4

def externe():
    def interne():
        print("Je suis à l'intérieur.")
    
    interne()

externe()