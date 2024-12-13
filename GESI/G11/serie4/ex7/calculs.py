addition = lambda x, y: x + y
soustraction = lambda x, y: x - y
multiplication = lambda x, y: x * y
def division(x, y):
    if y == 0:
        return "Division par zéro impossible"
    return x / y