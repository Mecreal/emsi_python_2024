parametres_circuit = (5,12,220,"AC") # tuple de paramètres de circuit

print("Tension: ",parametres_circuit[1],"V") # affiche la tension

courant, tension, frequence, type_courant = parametres_circuit # décomposition de tuple

def description_circuit(parametres_circuit: tuple) -> str:
    """Retourne la description du circuit"""

    courant, tension, frequence, type_courant = parametres_circuit # décomposition de tuple
    return f"Circuit de {courant}A, {tension}V, \
{frequence}Hz en courant {type_courant}"

print(description_circuit(parametres_circuit)) # affiche la description du circuit


print("Circuit 2")

parametres_circuit2 = (10,24,220,"DC") # tuple de paramètres de circuit

print(description_circuit(parametres_circuit2)) # affiche la description du circuit


# EX5

# parametres_circuit.append("DC") # ajoute DC à la liste, Error

parametres_circuit = (5,12,220,"DC") # tuple de paramètres de circuit

parametres_circuit_modifie = list(parametres_circuit) # convertit le tuple en liste

parametres_circuit_modifie[3]= "DC" # ajoute DC à la liste

parametres_circuit_modifie = tuple(parametres_circuit_modifie) # convertit la liste en tuple

print(description_circuit(parametres_circuit_modifie)) # affiche la description du circuit