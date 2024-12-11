# fonction lambda pour calculer la la puissance P = U * I
puissance = lambda x, y: x * y

U = 230 # tension V

I = 5 # courant A 

P = puissance(U, I) # puissance en W

print("La puissance est de", P, "Watt")