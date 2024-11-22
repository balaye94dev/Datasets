# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:12:35 2024

@author: Dell
"""

import pandas as pd

df_dak = pd.read_excel("CLIM_DAKAR(2009-2023).xlsx")
df_zig = pd.read_excel("CLIM_ZIGUINCHOR(2009-2023).xlsx")
df_mtm = pd.read_excel("CLIM_MATAM(2009-2023).xlsx")

df_temp = pd.DataFrame()

df_temp['WINDDIR_dak'] = df_dak['WINDDIR']
df_temp['WINDDIR_zig'] = df_zig['WINDDIR']
df_temp['WINDDIR_mtm'] = df_mtm['WINDDIR']

outpout_file_path = 'WINDDIR_dak_zig_mtm.xlsx'

df_temp.to_excel(outpout_file_path, sheet_name  = 'WINDDIR')
