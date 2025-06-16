import pandas as pd

# cargar csv sent trimestral
df = pd.read_csv('/Users/carcerezo/Desktop/TFG/sentimiento_mensual.csv')

# fecha en formato datetime
df['fecha'] = pd.to_datetime(df['fecha'])

# columna de trimestre 
df['trimestre'] = df['fecha'].dt.to_period('Q').dt.to_timestamp()

# agrupar x trimestre 
df_trimestral = df.groupby('trimestre')['sentimiento_textblob'].mean().reset_index()
df_trimestral.rename(columns={'sentimiento_textblob': 'sentimiento_medio_trimestral'}, inplace=True)

# guardar 
df_trimestral.to_csv('/Users/carcerezo/Desktop/TFG/sentimiento_trimestral.csv', index=False)
