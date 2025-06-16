import pandas as pd
import matplotlib.pyplot as plt

# cargar sentimiento trimestral
df_sent = pd.read_csv('/Users/carcerezo/Desktop/TFG/sentimiento_trimestral.csv')
df_sent['trimestre'] = pd.to_datetime(df_sent['trimestre'])

# cargar PIB 
df_pib = pd.read_csv('/Users/carcerezo/Desktop/TFG/DATASET/GDPC1_Historical_Data.csv')
df_pib.columns = ['fecha', 'pib']
df_pib['fecha'] = pd.to_datetime(df_pib['fecha'])
df_pib['trimestre'] = df_pib['fecha'].dt.to_period('Q').dt.to_timestamp()

# unir x trimestre
df_merge = pd.merge(df_sent, df_pib[['trimestre', 'pib']], on='trimestre', how='inner')

# normalizar
df_merge['sent_norm'] = (df_merge['sentimiento_medio_trimestral'] - df_merge['sentimiento_medio_trimestral'].min()) / (df_merge['sentimiento_medio_trimestral'].max() - df_merge['sentimiento_medio_trimestral'].min())
df_merge['pib_norm'] = (df_merge['pib'] - df_merge['pib'].min()) / (df_merge['pib'].max() - df_merge['pib'].min())

# grafica
plt.figure(figsize=(12, 6))
plt.plot(df_merge['trimestre'], df_merge['sent_norm'], label='Sentimiento (normalizado)', marker='o')
plt.plot(df_merge['trimestre'], df_merge['pib_norm'], label='PIB real (normalizado)', marker='o')
plt.title('Evolución trimestral: Sentimiento vs PIB real')
plt.xlabel('Trimestre')
plt.ylabel('Valores normalizados')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('/Users/carcerezo/Desktop/TFG/DATASET/gráficos_finales/sentimiento_vs_pib_trimestral.png')
plt.close()
