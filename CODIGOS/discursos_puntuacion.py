import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

# archivo
ruta = '/Users/carcerezo/Desktop/TFG/DATASET/discursos_fomc_con_puntuacion.csv'  # Tu archivo bueno con comas, puntos, etc.
df = pd.read_csv(ruta)

# limpieza
def limpiar_minimamente(texto):
    texto = re.sub(r'\s+', ' ', texto)
    return texto.strip()

df["texto_limpio_con_puntuacion"] = df["texto_limpio"].apply(limpiar_minimamente)

#  VADER
analyzer = SentimentIntensityAnalyzer()
df["sentimiento_compound"] = df["texto_limpio_con_puntuacion"].apply(lambda x: analyzer.polarity_scores(str(x))["compound"])

# guardar
df.to_csv('/Users/carcerezo/Desktop/TFG/DATASET/discursos_fomc_sentimiento_v2.csv', index=False)

print("✔️ Análisis de sentimiento aplicado correctamente con puntuación preservada.")
