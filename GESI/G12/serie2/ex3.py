# Annee bisexestile 

annee = int(input("Entre l'annee: "))

# message = "anee besexestille"
if annee % 4 == 0:
    if not(annee % 100 == 0):
        print("annee est bissextile")
    else:
        if annee % 400 == 0:
            print("annee bissextile")
        else:
            print("annee non bissextile")
else:
    print("l'annee n'est apas bissextile")


# Une seule condition

if annee % 4 == 0 and ( annee% 100  or annee % 400 == 0):
    print("L'année est bissextile")
else:
    print("L'année n'est pas bissextile")