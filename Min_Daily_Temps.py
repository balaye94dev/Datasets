import pandas as pd

# Lire le fichier Excel
file_path = 'CLIM_MATAM(2009-2023).xlsx'
df = pd.read_excel(file_path)

# Assurez-vous que votre fichier Excel a une colonne 'datetime' pour les dates et heures
# et une colonne 'temperature' pour les températures horaires.

# Convertir la colonne 'datetime' en type datetime
df['datetime'] = pd.to_datetime(df['datetime'])

# Définir la colonne 'datetime' comme index
df.set_index('datetime', inplace=True)

# Calculer les maximums de températures journalières
daily_min_temps = df['TEMP'].resample('D').min()/10

# Afficher les résultats
print(daily_min_temps)

# Sauvegarder les résultats dans un nouveau fichier Excel
output_file_path = 'Min_Daily_Temps_Matam.xlsx'
daily_min_temps.to_excel(output_file_path, sheet_name='Min_Temperatures')
