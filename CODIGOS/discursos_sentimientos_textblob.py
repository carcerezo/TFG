import pandas as pd
from textblob import TextBlob

# cargar discursos
ruta = '/Users/carcerezo/Desktop/TFG/discursos_texto_con_puntuacion.csv'
df = pd.read_csv(ruta)

#  TextBlob 
def obtener_polaridad(texto):
    blob = TextBlob(str(texto))
    return blob.sentiment.polarity  # Valor entre -1 y +1

df["sentimiento_textblob"] = df["texto_completo_con_puntuacion"].apply(obtener_polaridad)

# guardar
df.to_csv('/Users/carcerezo/Desktop/TFG/discursos_con_sentimiento_textblob.csv', index=False)

print(" Análisis con TextBlob completado. Archivo guardado como:")
print("/Users/carcerezo/Desktop/TFG/discursos_con_sentimiento_textblob.csv")
