# nombre premiers entre 2 et 100
for i in range(1, 100001):
    if(i == 1):
        continue
    elif(i == 2):
        print(i)
        continue
    for j in range(2, int(i**0.5 + 1)):
        if i % j == 0:
            break
    else:
        print(i)