import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# cargar CSV snt anual
df_sent = pd.read_csv('/Users/carcerezo/Desktop/TFG/sentimiento_anual.csv')  # Asegúrate de que contiene 'año' y 'sentimiento_medio_anual'

# cargar CSV de PIB 
df_gdp = pd.read_csv('/Users/carcerezo/Desktop/TFG/DATASET/GDPC1_Historical_Data.csv')
df_gdp['observation_date'] = pd.to_datetime(df_gdp['observation_date'])
df_gdp['año'] = df_gdp['observation_date'].dt.year
df_gdp_anual = df_gdp.groupby('año')['GDPC1'].mean().reset_index()

# unir x año
df_merge = pd.merge(df_sent, df_gdp_anual, on='año')

# normalizar
scaler = MinMaxScaler()
df_merge[['sentimiento_normalizado', 'pib_normalizado']] = scaler.fit_transform(
    df_merge[['sentimiento_medio_anual', 'GDPC1']]
)

# grafica
plt.figure(figsize=(12, 6))
plt.plot(df_merge['año'], df_merge['sentimiento_normalizado'], marker='o', label='Sentimiento (normalizado)')
plt.plot(df_merge['año'], df_merge['pib_normalizado'], marker='o', label='PIB real (normalizado)', color='darkorange')
plt.title('Evolución anual: Sentimiento vs PIB real')
plt.xlabel('Año')
plt.ylabel('Valores normalizados')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Guardar 
plt.savefig('/Users/carcerezo/Desktop/TFG/DATASET/gráficos_finales/sentimiento_vs_pib_anual.png')
plt.close()
