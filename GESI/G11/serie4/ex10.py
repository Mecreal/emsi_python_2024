# fibunacci

def fib(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(f"fib(5) = {fib(10)}") # 5