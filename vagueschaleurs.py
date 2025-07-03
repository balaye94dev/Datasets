import pandas as pd

# Charger les fichiers excel
df_dkr_temps = pd.read_excel('DAKAR_MORPHED.xlsx', sheet_name='DBT')
df_dkr_temps['datetime'] = pd.to_datetime(df_dkr_temps['datetime'])
df_dkr_temps.set_index('datetime', inplace=True)

def detecter_vagues_chaleur(temperatures, seuil, duree_min):
    """
    Détecte les vagues de chaleur dans une série de températures horaires.

    Args:
        temperatures: Une liste de températures horaires.
        seuil: La température seuil pour définir une vague de chaleur.
        duree_min: La durée minimale (en heures) d'une vague de chaleur.

    Returns:
        Une liste de tuples (début, fin) indiquant les périodes de vagues de chaleur.
    """

    vagues_chaleur = []
    debut_vague = None

    for i, temperature in enumerate(temperatures):
        if temperature > seuil:
            if debut_vague is None:
                debut_vague = i
        else:
            if debut_vague is not None:
                if i - debut_vague >= duree_min:
                    vagues_chaleur.append((debut_vague, i - 1))
                debut_vague = None

    # Vérifier si la dernière période est une vague de chaleur
    if debut_vague is not None and len(temperatures) - debut_vague >= duree_min:
        vagues_chaleur.append((debut_vague, len(temperatures) - 1))

    return vagues_chaleur

# Exemple d'utilisation
temperatures = df_dkr_temps['CCDBT_2080'].resample('D').max()  # Données d'exemple
seuil = 30  # Température seuil
duree_min = 3  # Durée minimale d'une vague de chaleur

resultats = detecter_vagues_chaleur(temperatures, seuil, duree_min)
print(resultats)  # Par exemple, [(3, 5), (8, 11)]