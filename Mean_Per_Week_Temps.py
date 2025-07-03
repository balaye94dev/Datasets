import pandas as pd
import numpy as np

# Générer des données horaires pour une année
date_rng = pd.date_range(start='1/1/2023', end='31/12/2023', freq='H')
data = np.random.randint(0, 100, size=(len(date_rng)))
df = pd.DataFrame(data, index=date_rng, columns=['value'])

# Resampler les données pour obtenir des moyennes hebdomadaires
weekly_data = df.resample('W').mean()

# Reconstituer les journées types
daily_profiles = df.groupby(df.index.time).mean()

# Afficher les résultats
print("Données hebdomadaires moyennes :")
print(weekly_data.head())

print("\nProfils journaliers moyens :")
print(daily_profiles.head())