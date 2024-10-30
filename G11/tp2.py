# Afficher nom et date dynamique
import datetime as dt

nom = input("Veuillez entrer votre nom :")
print("Nom", nom,sep=" : ",end=" | ")
print("date : ",dt.date.today(),sep=" : ",end=" | ")
print("date et heure : ",dt.datetime.now(),sep=" : ")
