def extern():
    print("Je suis dans la fonction extern")
    def intern():
        print("Je suis dans la fonction intern")

    print("Je vais appeler la fonction intern")
    intern()

print("Je vais appeler la fonction extern")
extern()
print("Je suis de retour dans le programme principal")