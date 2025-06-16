import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# archivo con los discursos válidos y con puntuación
ruta_entrada = '/Users/carcerezo/Desktop/TFG/discursos_texto_con_puntuacion.csv'
df = pd.read_csv(ruta_entrada)

# sentimiento VADER
analyzer = SentimentIntensityAnalyzer()

# Aplicar VADER 
df["sentimiento_compound"] = df["texto_completo_con_puntuacion"].apply(
    lambda x: analyzer.polarity_scores(str(x))["compound"]
)

# Guardar el resultado
ruta_salida = '/Users/carcerezo/Desktop/TFG/discursos_con_sentimiento.csv'
df.to_csv(ruta_salida, index=False)

print("✔️ Análisis de sentimiento aplicado correctamente y archivo guardado en:")
print(ruta_salida)
