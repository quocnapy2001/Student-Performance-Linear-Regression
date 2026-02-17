import pandas as pd
import seaborn as sns


### Data Import and Inspect
directory = "/Users\\Owner\\Documents\\GitHub\\Student-Performance-Linear-Regression\\student performance.xlsx"

df = pd.read_excel(directory, index_col = 0)


df_info = df.info()
# all data are non-nulL
# Extracurricular Activities is object

df_T = df.describe()


### Seaborn
sns.pairplot(df, hue="Extracurricular Activities", diag_kind='hist')


### Convert Extracurricular Activities to numeric
df['Extracurricular Activities'] = df['Extracurricular Activities'].astype('category')
df['Extracurricular Activities'] = df['Extracurricular Activities'].map({
    "Yes": 1,
    "No" : 0
    })