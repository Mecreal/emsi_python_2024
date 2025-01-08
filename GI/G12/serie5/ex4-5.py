#Ex 4 

parameters_circuit = (5,12,220,"AC") # Tuple de paramètres de circuit

print(parameters_circuit) # Affiche le tuple de paramètres de circuit

# Q2

print("La tension est de : ",parameters_circuit[1],"V") # Affiche la tension


# Q3

I, V, f, type_c = parameters_circuit # Décomposition du tuple


def description_circuit(parameters_circuit: tuple) -> str:
    I, V, f, type_c = parameters_circuit
    return f"Le courant est de {I} A, la tension est de {V} V, la fréquence est de {f} Hz et le type de courant est {type_c}"

print(description_circuit(parameters_circuit)) # Affiche la description du circuit


# sup :

p_c = (5,9,220,"DC") # Tuple de paramètres de circuit

print(description_circuit(p_c)) # Affiche la description du circuit

#Ex5

# Q1

# parameters_circuit[3] = "DC" # Error : Tuple is immutable

# Q2

parameters_circuit = (5,12,220,"DC") # Tuple de paramètres de circuit