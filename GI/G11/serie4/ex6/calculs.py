def addition(a: float, b: float) -> float:
    """ 
    Add two numbers
    args:
    - a: float
    - b: float
    return: float : sum of a and b
    """
    return a + b
def soustraction(a: float, b: float) -> float:
        """
        Subtract two numbers
        args:
        - a: float
        - b: float
        return: float : difference of a and b
        """
        return a - b 

def multiplication(a: float, b: float) -> float:
        """
        Multiply two numbers
        args:
        - a: float
        - b: float
        return: float : product of a and b
        """
        return a * b

def division(a: float, b: float) -> float:
        """
        Divide two numbers
        args:
        - a: float
        - b: float
        return: float : quotient of a and b or raises ValueError if b is zero
        """
        if b == 0:
            return None
        return a / b


# Méthode 2

# addition = lambda a, b: a + b
# soustraction = lambda a, b: a - b
# multiplication = lambda a, b: a * b
# division = lambda a, b: a / b if b != 0 else "Division by zero is not allowed"
