# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:45:03 2024

@author: Dell
"""

import pandas as pd
import matplotlib.pyplot as plt

# Importer les fichiers excel sous forme de Dataframe
df_mtm_temps =pd.read_excel('MATAM_MORPHED.xlsx', sheet_name='Temps')
df_dkr_temps =pd.read_excel('DAKAR_MORPHED.xlsx', sheet_name='DBT')
df_zig_temps =pd.read_excel('ZIGUINCHOR_MORPHED.xlsx', sheet_name='Temps')

# Définir la colonne datetime comme index
df_mtm_temps['datetime'] = pd.to_datetime(df_mtm_temps['datetime'])
df_mtm_temps.set_index('datetime', inplace=True)
df_dkr_temps['datetime'] = pd.to_datetime(df_dkr_temps['datetime'])
df_dkr_temps.set_index('datetime', inplace=True)
df_zig_temps['datetime'] = pd.to_datetime(df_zig_temps['datetime'])
df_zig_temps.set_index('datetime', inplace=True)

# Calculer les maximums de températures journalières - Matam
mtm_daily_max_temps = df_mtm_temps['CCDBT_2020'].resample('ME').max()
mtm_daily_max_temps_2050 = df_mtm_temps['CCDBT_2050'].resample('ME').max()
mtm_daily_max_temps_2080 = df_mtm_temps['CCDBT_2080'].resample('ME').max()

# Calculer les maximums de températures journalières - Dakar
dkr_daily_max_temps = df_dkr_temps['CCDBT_2020'].resample('ME').max()
dkr_daily_max_temps_2050 = df_dkr_temps['CCDBT_2050'].resample('ME').max()
dkr_daily_max_temps_2080 = df_dkr_temps['CCDBT_2080'].resample('ME').max()

# Calculer les maximums de températures journalières - Ziguinchor
zig_daily_max_temps = df_zig_temps['CCDBT_2020'].resample('ME').max()
zig_daily_max_temps_2050 = df_zig_temps['CCDBT_2050'].resample('ME').max()
zig_daily_max_temps_2080 = df_zig_temps['CCDBT_2080'].resample('ME').max()

mois = ["Jan", "Fev", "Mars", "Avr", "Mai", "Juin", "Juil", "Aout", "Sept", "Oct", "Nov", "Dec"]

plt.plot(mois, dkr_daily_max_temps, color = "Blue", linewidth = 1.5)
plt.plot(mois, dkr_daily_max_temps_2050, color = "Green", linewidth = 1.5, linestyle = "dotted")
plt.plot(mois, dkr_daily_max_temps_2080, color = "Red", linewidth = 1.5, linestyle = "dotted")
plt.grid(visible = True, linestyle = '-.', linewidth = 1)
plt.axis(xlim = ("jan", "dec") , ylim = (0,50))