def addition(a: float, b: float) -> float:
    """ 
    Add two numbers
    args:
    - a: float
    - b: float
    return: float : sum of a and b
    """
    return a + b

soustraction = lambda a, b: a - b
def multiplication(a, b):
    return a * b

def division(a, b):
    div = a / b if b != 0 else "Division par zéro impossible"
    return div

