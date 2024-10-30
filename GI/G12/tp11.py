# affichage de nom et date dynamique
# import datetime
from datetime import datetime,date


print("Nom : Hamza",end = " | ")
print("Date", date.today(), sep=" : ",end = " | ") 
print("Date et heure",datetime.now(), sep=" : ")