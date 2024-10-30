# affichage dynamique de date

import datetime
import time

print("Nom : Hamza abouabid",end=" | ")
print("date",datetime.date.today(),sep=": ")
print("heure",time.strftime("%H:%M:%S", time.localtime()))