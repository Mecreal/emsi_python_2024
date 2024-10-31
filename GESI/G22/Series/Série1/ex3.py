# Opérateur de comparaison 

# Q1 : Déclaration de variable numérique
x = 12
y =17.3

# Q2 Opérateur de comparaison et printing

egale = (x == y)
different = (x != y)
greater = (x > y)
less = (x < y)
greater_or_equal = (x >= y)
less_or_equal = (x <= y)

# printing

print(f"""Voir si {x} égale à {y} : {egale}
Voir si {x} différent de {y} : {different}
Voir si {x} est plus grand que {y} : {greater}
Voir si {x} est plus petit que {y} : {less}
Voir si {x} est plus grand ou égal à {y} : {greater_or_equal}
Voir si {x} est plus petit ou égal à {y} : {less_or_equal}
""")

# Q3 déclaratuin de variable c et d booléan 
print("-_"*10," Séparation ","_-"*10)

c = True
d = False

et = c and d
ou = c or d
non_c = not c
non_d = not d

# printing 

print(f"""
{c} et {d} donne : {et}
{c} ou {d} donne : {ou}
non {c} donne : {non_c}
non {d} donne : {non_d}
""")