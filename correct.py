print("exercise de devinette")

print("Pensee a un nombre entre 0 et 100")

min = 0
max = 100
i = 1
mid = 50
while i<8:

    if min == max:
        print("Le nombre est", mid)
        break
    print("Est-ce que le nombre est plus grand que", mid, "?", end="")
    ouinon = input("oui ou non")
    if ouinon == "oui":
        min = mid
    elif ouinon == "non":
        max = mid
    else:
        break
    mid = (min + max) // 2


    i += 1
