import pandas as pd

# Lire le fichier Excel
file_path = 'CLIM_ZIGUINCHOR(2009-2023).xlsx'
df = pd.read_excel(file_path)

# Assurez-vous que votre fichier Excel a une colonne 'datetime' pour les dates et heures
# et une colonne 'temperature' pour les températures horaires.

# Convertir la colonne 'datetime' en type datetime
df['datetime'] = pd.to_datetime(df['datetime'])

# Définir la colonne 'datetime' comme index
df.set_index('datetime', inplace=True)

# Calculer les maximums de températures journalières
daily_max_temps = df['TEMP'].resample('D').max()/10

# Afficher les résultats
print(daily_max_temps)

# Sauvegarder les résultats dans un nouveau fichier Excel
output_file_path = 'Max_Daily_Temps_Ziguinchor.xlsx'
daily_max_temps.to_excel(output_file_path, sheet_name='Max_Temperatures')
