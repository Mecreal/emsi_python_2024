def somme(x,y):
    return x+y

def produit(x,y):
    return x*y

def division(x,y):
    if y==0:
        return None
    else:
        return x/y

def soustraction(x,y):
    return x-y

def puissance(x,y):
    return x**y

def factorielle(n):
    if n < 0:
        return None
    else:
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return fact
    
def sqrt(x):
    if x < 0:
        return None
    else:
        return x**0.5
