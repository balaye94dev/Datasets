# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 17:45:15 2024

@author: Dell
"""

import pandas as pd

# Charger les fichiers excel
df_dkr_temps = pd.read_excel('DAKAR_MORPHED.xlsx', sheet_name='DBT')
df_dkr_temps['datetime'] = pd.to_datetime(df_dkr_temps['datetime'])
df_dkr_temps.set_index('datetime', inplace=True)

dkr_design_day = df_dkr_temps['CCDBT_2020'].resample('D')

print(dkr_design_day)