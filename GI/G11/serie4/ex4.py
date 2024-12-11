#fonction imbriquee

def extern():
    def interne():
        print("interne")
    interne()

extern()
