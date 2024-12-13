def fact(n: int) -> int:
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return n * fact(n-1) 
    

print(fact(5) == 120)
print(fact(0) == 1)
print(fact(-1) is None)

print(f"5! = {fact(5)}")