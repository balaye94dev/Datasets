import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-whitegrid')  # Base sobre et professionnelle
plt.rcParams.update({
    'font.size': 12,
    'font.family': 'consolas',
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.dpi': 300,
    'lines.linewidth': 1.5,
})

# Charger les données
df = pd.read_excel("Dkr_Datas.xlsx", parse_dates=['datetime'])

# Colonnes utiles
df['date'] = df['datetime'].dt.date
df['hour'] = df['datetime'].dt.hour
df['month'] = df['datetime'].dt.month
df['week'] = df['datetime'].dt.isocalendar().week
df['year'] = df['datetime'].dt.year

# Mois été / hiver
ete_mois = [6, 7, 8]
hiver_mois = [12, 1, 2]

# Lissage
def lisser_profil(profil, window=5):
    return np.convolve(profil, np.ones(window)/window, mode='same')

# Extraction générique
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

# Extraction + lissage
def get_profils_lisses(df, saison_mois):
    return {
        "Actuel": lisser_profil(semaine_type(df, saison_mois, "temperature")),
        "2050": lisser_profil(semaine_type(df, saison_mois, "temperature_2050")),
        "2100": lisser_profil(semaine_type(df, saison_mois, "temperature_2100")),
    }

profils_ete = get_profils_lisses(df, ete_mois)
profils_hiver = get_profils_lisses(df, hiver_mois)

# Axes
heures = np.arange(168)
xticks = np.arange(0, 168, 24)
xtick_labels = [f"Jour {i+1}" for i in range(7)]

# 📈 Tracé
fig, ax = plt.subplots(figsize=(6.5, 4.5))  # Dimensions compactes et publication-ready

# Été
#ax.plot(heures, profils_ete["Actuel"], label="Été - Actuel", color="darkorange")
#ax.plot(heures, profils_ete["2050"], label="Été - 2050", color="orangered", linestyle="--")
#ax.plot(heures, profils_ete["2100"], label="Été - 2100", color="firebrick", linestyle=":")

# Hiver
ax.plot(heures, profils_hiver["Actuel"], label="Hiver - Actuel", color="royalblue")
ax.plot(heures, profils_hiver["2050"], label="Hiver - 2050", color="deepskyblue", linestyle="--")
ax.plot(heures, profils_hiver["2100"], label="Hiver - 2100", color="navy", linestyle=":")

# Axe x
ax.set_xticks(xticks)
ax.set_xticklabels(xtick_labels)
ax.set_xlabel("Jour de la semaine")
ax.set_ylabel("Température (°C)")
ax.set_title("Évolution des profils de température horaire en Hiver \n(Actuel, 2050, 2100) ")
ax.legend(loc='upper center', ncol=3, frameon=False)
ax.grid(True, linestyle=':', linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.show()