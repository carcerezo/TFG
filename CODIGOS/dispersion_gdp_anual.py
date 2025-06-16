import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# cargar sent anual y PIB
df_sent = pd.read_csv('/Users/carcerezo/Desktop/TFG/sentimiento_anual.csv')
df_gdp = pd.read_csv('/Users/carcerezo/Desktop/TFG/DATASET/GDPC1_Historical_Data.csv')

# agrupar PIB x año
df_gdp['observation_date'] = pd.to_datetime(df_gdp['observation_date'])
df_gdp['año'] = df_gdp['observation_date'].dt.year
df_gdp_anual = df_gdp.groupby('año')['GDPC1'].mean().reset_index()

# unir sent pib con año
df_merge = pd.merge(df_sent, df_gdp_anual, on='año')

# grafico de dispersion con regresion
plt.figure(figsize=(10, 6))
sns.regplot(data=df_merge, x='sentimiento_medio_anual', y='GDPC1', color='mediumseagreen', line_kws={'color': 'darkgreen'})
plt.title('Dispersión anual: Sentimiento vs PIB real')
plt.xlabel('Sentimiento Medio Anual (TextBlob)')
plt.ylabel('PIB Real (Media Anual)')
plt.grid(True)

# guardar 
output_path = '/Users/carcerezo/Desktop/TFG/DATASET/gráficos_finales/dispersion_sentimiento_vs_pib_anual.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.tight_layout()
plt.savefig(output_path, dpi=300)
plt.close()
