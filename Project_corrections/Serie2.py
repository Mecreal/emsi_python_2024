import random
def jeu_devine():
    secret = random.randint(1, 100)
    tentatives = 10
    print("Bienvenue dans le jeu de Devine le Nombre!")
    print("Je pense à un nombre entre 1 et 100.")
    print(f"Vous avez {tentatives} tentatives pour le deviner.\n")
  
    while tentatives > 0:
        devine = int(input("Entrez votre tentative : "))
        if devine == secret:
            print(f"Felicitations! Vous avez trouve le nombre {secret}.\n")
            break
        elif devine < secret:
            print("Le nombre secret est plus grand.\n")
        else:
            print("Le nombre secret est plus petit.\n")
      
        tentatives -= 1
        print(f"Il vous reste {tentatives} tentatives.\n")
  
    if tentatives == 0:
        print(f"Dommage! Le nombre secret etait {secret}.\n")
  
    rejouer = input("Voulez-vous rejouer? (oui/non) : ").lower()
    if rejouer == "oui":
        print("\n--- Nouveau Jeu ---\n")
        jeu_devine()
    else:
        print("Merci d'avoir joue! A bientot.")
# Lancer le jeu
jeu_devine()