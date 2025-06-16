import pandas as pd

# cargar datos de sentimiento
df_sent = pd.read_csv('/Users/carcerezo/Desktop/TFG/discursos_con_sentimiento_textblob.csv')
df_sent['fecha'] = pd.to_datetime(df_sent['fecha'])
df_sent = df_sent.sort_values('fecha')

# cuartiles para outliers
q1 = df_sent['sentimiento_textblob'].quantile(0.10)
q3 = df_sent['sentimiento_textblob'].quantile(0.90)
outliers = df_sent[(df_sent['sentimiento_textblob'] < q1) | (df_sent['sentimiento_textblob'] > q3)].copy()

# cargar sp500
df_sp = pd.read_csv('/Users/carcerezo/Desktop/TFG/DATASET/HistoricalData_S&P500.csv', usecols=['Fecha', 'Cerrar/último'])
df_sp.columns = ['fecha', 'cierre']
df_sp['fecha'] = pd.to_datetime(df_sp['fecha'], format='%m/%d/%Y')
df_sp['cierre'] = pd.to_numeric(df_sp['cierre'], errors='coerce')

# unir
df_outliers = pd.merge(outliers, df_sp, on='fecha', how='left')
df_outliers = df_outliers.sort_values('fecha')

# variacion porcentual
df_outliers['variacion_pct'] = df_outliers['cierre'].pct_change() * 100

# columnas
df_outliers_final = df_outliers[['archivo', 'fecha', 'sentimiento_textblob', 'cierre', 'variacion_pct']]

# guardar
df_outliers_final.to_csv('/Users/carcerezo/Desktop/TFG/outliers_eventos.csv', index=False)
print("CSV generado con éxito en /Users/carcerezo/Desktop/TFG/outliers_eventos.csv")
