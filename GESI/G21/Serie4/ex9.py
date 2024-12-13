# factorielle 

def factorielle(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return n * factorielle(n-1)
    
print(f" 5! = {factorielle(5)}") # 120