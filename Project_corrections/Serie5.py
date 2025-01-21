import csv

# 1. Collecte des Données
produits = ["Moteur Électrique", "Variateur de Fréquence", "Capteur de Température", "Automate Programmable"]

# 2. Enregistrement des Statistiques de Production
statistiques_production = {
    "Moteur Électrique": (500, 2.5),
    "Variateur de Fréquence": (300, 1.8),
    "Capteur de Température": (800, 0.5),
    "Automate Programmable": (200, 3.0)
}

# 3. Mise à Jour des Données
statistiques_production["Convertisseur DC-DC"] = (150, 2.2)

# 4. Analyse des Données
print("Produits avec un taux de défaut supérieur à 2% :")
for produit, (quantite, taux_defaut) in statistiques_production.items():
    if taux_defaut > 2:
        print(f"- {produit} : {taux_defaut}%")

# 5. Calcul des Totaux
total_unites = sum(quantite for quantite, _ in statistiques_production.values())
moyenne_defauts = sum(taux_defaut for _, taux_defaut in statistiques_production.values()) / len(statistiques_production)

print(f"\nTotal des unités produites ce mois-ci : {total_unites}")
print(f"Taux de défaut moyen : {moyenne_defauts:.2f}%")

# 6. Visualisation des Données
taux_defaut = [taux for _, taux in statistiques_production.values()]
produit_le_plus_fiable = min(statistiques_production, key=lambda p: statistiques_production[p][1])

print(f"\nProduit le plus fiable : {produit_le_plus_fiable} avec un taux de défaut de {statistiques_production[produit_le_plus_fiable][1]}%")

# 7. Export des Résultats
fichier_csv = "production_janvier.csv"
with open(fichier_csv, mode="w", newline="", encoding="utf-8") as fichier:
    writer = csv.writer(fichier)
    writer.writerow(["Produit", "Unités Produites", "Taux de Défaut (%)"])
    for produit, (quantite, taux_defaut) in statistiques_production.items():
        writer.writerow([produit, quantite, taux_defaut])

print(f"\nLes données ont été exportées dans le fichier {fichier_csv}.")
