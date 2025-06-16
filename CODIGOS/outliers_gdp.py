import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore
import os

# Leer sentimiento trimestral
df_sent = pd.read_csv('/Users/carcerezo/Desktop/TFG/sentimiento_trimestral.csv')
df_sent['trimestre'] = pd.to_datetime(df_sent['trimestre'])

# Calcular z-score y detectar outliers (z > 1 o z < -1)
df_sent["z_score"] = zscore(df_sent["sentimiento_medio_trimestral"])
outliers = df_sent[(df_sent["z_score"] > 1) | (df_sent["z_score"] < -1)]

# Leer PIB real trimestral
df_gdp = pd.read_csv('/Users/carcerezo/Desktop/TFG/DATASET/GDPC1_Historical_Data.csv')
df_gdp['observation_date'] = pd.to_datetime(df_gdp['observation_date'])
df_gdp = df_gdp.rename(columns={'observation_date': 'trimestre', 'GDPC1': 'pib'})

# Calcular variación porcentual del PIB
df_gdp['variacion_pct'] = df_gdp['pib'].pct_change() * 100

# Cruce por trimestre
df_outliers = pd.merge(outliers, df_gdp, on='trimestre', how='left')

# Guardar CSV con los outliers
df_outliers.to_csv('/Users/carcerezo/Desktop/TFG/outliers_trimestrales_pib.csv', index=False)

# Crear gráfico
plt.figure(figsize=(12, 6))
plt.scatter(df_sent["trimestre"], df_sent["sentimiento_medio_trimestral"], color="skyblue", label="Todos los trimestres")
plt.scatter(df_outliers["trimestre"], df_outliers["sentimiento_medio_trimestral"], color="red", label="Outliers")
plt.title("Outliers: Sentimiento extremo trimestral (TextBlob)")
plt.xlabel("Trimestre")
plt.ylabel("Sentimiento TextBlob")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Guardar gráfico
output_dir = '/Users/carcerezo/Desktop/TFG/DATASET/gráficos_finales'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, "outliers_trimestrales_pib.png"), dpi=300)
plt.show()
