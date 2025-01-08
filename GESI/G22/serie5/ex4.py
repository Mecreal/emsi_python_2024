# Ex 4 

parameters_circuit = (5,12,220,"AC") # tuple de paramètres de circuit

print("Tension: ",parameters_circuit[1],"V") # affiche la tension

courant, tension, frequence, type_courant = parameters_circuit # décomposition de tuple

def description_circuit(parameters_circuit: tuple) -> str:
    """Retourne la description du circuit"""
    
    courant, tension, frequence, type_courant = parameters_circuit # décomposition de tuple
    return f"Circuit de {courant}A, {tension}V, \
{frequence}Hz en courant {type_courant}"


print(description_circuit(parameters_circuit)) # affiche la description du circuit