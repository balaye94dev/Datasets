import pandas as pd
import numpy as np

# Charger les données
df = pd.read_excel("ZIGUINCHOR_MORPHED.xlsx", sheet_name='DBT')  # Assurez-vous que le fichier contient des colonnes : 'datetime' et 'temperature'
df['datetime'] = pd.to_datetime(df['datetime'])
df['hour'] = df['datetime'].dt.hour

# Calculer les moyennes horaires
hourly_means = df.groupby('hour')['CCDBT_2080'].mean()

# Trouver le jour le plus proche du profil moyen
df['date'] = df['datetime'].dt.date
daily_profiles = df.groupby(['date', 'hour'])['CCDBT_2080'].mean().unstack()
distances = daily_profiles.apply(lambda x: np.linalg.norm(x - hourly_means), axis=1)
closest_day = distances.idxmin()

# Résultats
print(f"Jour type identifié : {closest_day}")
print("Profil moyen horaire :", hourly_means)

filepath = ("ziguinchor_jours_2080.xlsx")
daily_profiles.to_excel(filepath, sheet_name="jours 2080")