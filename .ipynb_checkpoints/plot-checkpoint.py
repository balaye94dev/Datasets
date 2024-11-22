# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 17:35:46 2024

@author: Dell
"""
#
import pandas as pd
import matplotlib.pyplot as plt

df_dak = pd.read_excel("CLIM_DAKAR(2009-2023).xlsx")
df_zig = pd.read_excel("CLIM_ZIGUINCHOR(2009-2023).xlsx")
df_mtm = pd.read_excel("CLIM_MATAM(2009-2023).xlsx")

df_temp = pd.DataFrame()

df_temp['WINDDIR_dak'] = df_dak['WINDDIR']
df_temp['WINDDIR_zig'] = df_zig['WINDDIR']
df_temp['WINDDIR_mtm'] = df_mtm['WINDDIR']

outpout_file_path = 'WINDDIR_dak_zig_mtm.xlsx'

df_temp.to_excel(outpout_file_path, sheet_name  = 'WINDDIR')

# Lire le fichier Excel
file_path = 'WINDSPEED_dak_zig_mtm.xlsx'
df = pd.read_excel(file_path)

WINDSPEED_dak = df['WINDSPEED_dak (m/s)']
WINDSPEED_zig = df['WINDSPEED_zig (m/s)']
WINDSPEED_mtm = df['WINDSPEED_mtm (m/s)']

plt.plot(WINDSPEED_dak, 'Blue')
plt.plot(WINDSPEED_zig, 'Green')
plt.plot(WINDSPEED_mtm, 'Red')


plt.xlabel('8760 Heures du TMY')
plt.ylabel('VITESSE DU VENT (m/s)')
plt.legend(['DAKAR', 'ZIGUINCHOR', 'MATAM'])
