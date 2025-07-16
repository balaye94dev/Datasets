import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger les données
df = pd.read_excel("Dkr_Datas.xlsx", parse_dates=['datetime'])

# Ajouter les colonnes utiles
df['date'] = df['datetime'].dt.date
df['hour'] = df['datetime'].dt.hour
df['month'] = df['datetime'].dt.month
df['week'] = df['datetime'].dt.isocalendar().week
df['year'] = df['datetime'].dt.year

# Mois d'été et d'hiver
ete_mois = [6, 7, 8]
hiver_mois = [12, 1, 2]

# Lissage simple
def lisser_profil(profil, window=5):
    return np.convolve(profil, np.ones(window)/window, mode='same')

# Fonction générique pour extraire une semaine type à partir d'une colonne
def semaine_type(df, mois_saison, colonne_temp):
    df_saison = df[df['month'].isin(mois_saison)]
    semaines_valides = []
    for (year, week), group in df_saison.groupby(['year', 'week']):
        if len(group) == 168:
            semaines_valides.append(group.sort_values('datetime'))
    profils = np.array([semaine[colonne_temp].values for semaine in semaines_valides])
    profil_moyen = profils.mean(axis=0)
    distances = np.linalg.norm(profils - profil_moyen, axis=1)
    idx_min = np.argmin(distances)
    return profils[idx_min]

# Extraire les profils et lisser
def get_profils_lisses(df, saison_mois):
    return {
        "Actuel": lisser_profil(semaine_type(df, saison_mois, "temperature")),
        "2050": lisser_profil(semaine_type(df, saison_mois, "temperature_2050")),
        "2100": lisser_profil(semaine_type(df, saison_mois, "temperature_2100")),
    }

profils_ete = get_profils_lisses(df, ete_mois)
profils_hiver = get_profils_lisses(df, hiver_mois)

# Axe x et ticks journaliers
heures = np.arange(168)
xticks = np.arange(0, 168, 24)
xtick_labels = [f"Jour {i+1}" for i in range(len(xticks))]

# 🎨 Tracé
plt.figure(figsize=(7, 5))

# Été
#plt.plot(heures, profils_ete["Actuel"], label="Été - Actuel", color="orange")
#plt.plot(heures, profils_ete["2050"], label="Été - 2050", color="darkorange", linestyle="--")
#plt.plot(heures, profils_ete["2100"], label="Été - 2100", color="red")

# Hiver
plt.plot(heures, profils_hiver["Actuel"], label="Hiver - Actuel", color="blue")
plt.plot(heures, profils_hiver["2050"], label="Hiver - 2050", color="dodgerblue", linestyle="--")
plt.plot(heures, profils_hiver["2100"], label="Hiver - 2100", color="navy")

# Personnalisation
plt.xticks(ticks=xticks, labels=xtick_labels)
plt.xlabel("Jour de la semaine")
plt.ylabel("Température de la semaine type (°C)")
plt.title("Comparaison des profils horaires - Hiver (Actuel, 2050, 2100)")
plt.grid(False)
plt.legend()
plt.tight_layout()
plt.show()
