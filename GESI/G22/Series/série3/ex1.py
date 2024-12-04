# Fizz   Buzz

for _ in range(1, 101):
    if _ % 3 == 0 and _ % 5 == 0:
        print("Fizz Buzz")
    elif _ % 3 == 0:
        print("Fizz")
    elif _ % 5 == 0:
        print("Buzz")
    else:
        print(_)