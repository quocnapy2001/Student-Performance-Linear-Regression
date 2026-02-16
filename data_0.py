# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 12:54:03 2026

@author: Owner
"""
#

import pandas as pd
import seaborn as sns

url = "https://raw.githubusercontent.com/msh209/INT3625/main/data/Student_Performance.csv"

df = pd.read_csv(url, index_col = 0)

df_info = df.info()

df_T = df.describe().T