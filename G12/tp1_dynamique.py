# afficher nom et date dynamique

import datetime as dt

print("Nom :", input("Entrez votre nom : "))
print("Date : ", dt.date.today())
print("Heure : ", dt.datetime.now().time())