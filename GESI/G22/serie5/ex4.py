# Ex 4 

# Q1
parameters_circuit = (5,12,220,"AC") # tuple de paramètres de circuit
# Q2
print("Tension: ",parameters_circuit[1],"V") # affiche la tension
# Q3
courant, tension, frequence, type_courant = parameters_circuit # décomposition de tuple
#Q4
def description_circuit(pram_cir:tuple) -> str:
    """Retourne la description du circuit"""
    
    courant, tension, frequence, type_courant = pram_cir # décomposition de tuple
    return f"Circuit de {courant}A, {tension}V, \
{frequence}Hz en courant {type_courant}"

# Supplémentaire
print(description_circuit(parameters_circuit)) # affiche la description du circuit

p_c2 = (3,5,220,"DC") # tuple de paramètres de circuit

print(description_circuit(p_c2)) # affiche la description du circuit


# Ex 5

# Q1

# parameters_circuit.append("DC") # ajoute "DC" : Erreur, tuple est immuable
# parameters_circuit.add("DC") # ajoute "DC" : Erreur, tuple n'a pas de méthode add

# Q2
# Methode directe
# parameters_circuit_modifie = (5,12,220,"DC") # tuple de paramètres de circuit
# parameters_circuit_modifie = parameters_circuit[:3] + ("DC",) # tuple de paramètres de circuit
parameters_circuit_modifie = list(parameters_circuit) # convertir tuple en liste
parameters_circuit_modifie[-1] = "DC" # modifier le dernier élément
parameters_circuit_modifie = tuple(parameters_circuit_modifie) # convertir liste en tuple
print(description_circuit(parameters_circuit_modifie)) # affiche la description du circuit