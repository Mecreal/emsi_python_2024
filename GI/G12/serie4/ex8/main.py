from outils_maths.calculs import *

x = 5
y = 2

print("Addition de", x, "et", y, ":", addition(x, y))
print("Soustraction de", x, "et", y, ":", soustraction(x, y))
print("Multiplication de", x, "et", y, ":", multiplication(x, y))
print("Division de", x, "par", y, ":", division(x, y))
print("Division de", x, "par 0 :", division(x, 0))
print(f"{x}! = {factorielle(x)}")
print(f"{y}! = {factorielle(y)}")