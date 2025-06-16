import pandas as pd
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import os


nltk.download("stopwords")

# ruta
ruta_csv = "/Users/carcerezo/Desktop/TFG/discursos_fomc_limpios.csv"
ruta_guardado = "/Users/carcerezo/Desktop/TFG/DATASET"
os.makedirs(ruta_guardado, exist_ok=True)

# carga
df = pd.read_csv(ruta_csv)
df["año"] = df["archivo"].str.extract(r'(20\d{2})')

# Agrupar texto por año
textos_por_año = df.groupby("año")["texto_limpio"].apply(lambda textos: " ".join(textos)).to_dict()

# preproc
stopwords_ingles = set(stopwords.words("english"))

def limpiar_y_filtrar(texto):
    tokens = texto.lower().split()
    tokens_filtrados = [t for t in tokens if t.isalpha() and t not in stopwords_ingles and len(t) > 3]
    return " ".join(tokens_filtrados)

textos_filtrados = {año: limpiar_y_filtrar(texto) for año, texto in textos_por_año.items()}

# tdidf
vectorizer = TfidfVectorizer(ngram_range=(2, 2), stop_words="english")
documentos = [textos_filtrados[año] for año in sorted(textos_filtrados)]
anios_ordenados = sorted(textos_filtrados)

tfidf_matrix = vectorizer.fit_transform(documentos)
feature_names = vectorizer.get_feature_names_out()

# bigramas x año
resultados = []

for idx, año in enumerate(anios_ordenados):
    fila = tfidf_matrix[idx].toarray()[0]
    indices_top = fila.argsort()[::-1][:10]
    top_bigrams = [(feature_names[i], fila[i]) for i in indices_top]
    for bigrama, score in top_bigrams:
        resultados.append({"año": año, "bigrama": bigrama, "tfidf": round(score, 4)})

# guardar
df_resultados = pd.DataFrame(resultados)
df_resultados.to_csv(f"{ruta_guardado}/bigrama_tfidf.csv", index=False)

print(" Bigrams TF-IDF por año calculados y guardados en:")
print(f"{ruta_guardado}/bigrama_tfidf.csv")

