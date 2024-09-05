import pandas as pd
import matplotlib.pyplot as plt

# Lire les données à partir d'un fichier exel
data = pd.read_excel('CLIM_DAKAR(2009-2023).xlsx')
print(data)

# Créer un graphique
plt.figure(figsize=(10, 5))
plt.plot(data, marker='o')
plt.title('Température Moyenne par Année')
plt.xlabel('Année')
plt.ylabel('Température Moyenne (°C)')
plt.grid(True)
plt.show()

