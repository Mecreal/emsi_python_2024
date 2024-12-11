# fonction imbriquée

def extern():
    def intern():
        print("Dans la fonction interne")
    intern()

extern()