import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


# Charger les données
df = pd.read_excel("Dkr_Datas.xlsx", parse_dates=['datetime'])


# Ajouter les colonnes utiles
df['date'] = df['datetime'].dt.date
df['hour'] = df['datetime'].dt.hour
df['month'] = df['datetime'].dt.month
df['week'] = df['datetime'].dt.isocalendar().week
df['year'] = df['datetime'].dt.year


# Définir les mois d'été (juin-juillet-août) et d'hiver (décembre-janvier-février)
ete_mois = [6, 7, 8, 9, 10]
hiver_mois = [12, 1, 2, 3, 4, 5]

# Fonction pour extraire une semaine type par saison
def semaine_type(df, mois_saison, saison):
    df_saison = df[df['month'].isin(mois_saison)]
    
    # Garder uniquement les semaines complètes (7 jours x 24 heures)
    semaines_valides = []
    for (year, week), group in df_saison.groupby(['year', 'week']):
        if len(group) == 7 * 24:
            semaines_valides.append(group)
    
    # Calculer la moyenne horaire par semaine
    profils = []
    for semaine in semaines_valides:
        temp_moyenne_horaire = semaine.sort_values('datetime')['temperature'].values
        profils.append(temp_moyenne_horaire)
    
    profils = np.array(profils)
    profil_moyen = profils.mean(axis=0)
    
    # Trouver la semaine la plus proche de la moyenne
    distances = np.linalg.norm(profils - profil_moyen, axis=1)
    idx_min = np.argmin(distances)
    semaine_type = profils[idx_min]
    
    return semaine_type

# Obtenir les profils de la semaine type d'été et d'hiver
profil_ete = semaine_type(df, ete_mois, "été")
profil_hiver = semaine_type(df, hiver_mois, "hiver")


# Axe horaire de 0 à 167 heures
heures = np.arange(168)

# Points pour chaque jour (0h, 24h, 48h, ..., 144h)
xticks = np.arange(0, 168, 24)
xtick_labels = [f"Jour {i+1}" for i in range(len(xticks))]


# Tracé
plt.figure(figsize=(12, 6))
plt.plot(heures, profil_ete, label="Semaine type - Été", color="orange")
plt.plot(heures, profil_hiver, label="Semaine type - Hiver", color="blue")
plt.xticks(ticks=xticks, labels=xtick_labels)
plt.xlabel("Jour de la semaine")
plt.ylabel("Température (°C)")
plt.title("Profils de température horaire – Semaine type Été vs Hiver")
plt.grid(False)
plt.legend()
plt.tight_layout()
plt.show()
