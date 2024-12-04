#nombre premier entre 1 et 100

for i in range(2,101):
    if i == 2:
        print(i)
    else:
        for j in range(2, int(i**0.5 + 1)):
            if i % j == 0:
                break
        else:
            print(i)