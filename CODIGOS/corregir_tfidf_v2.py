import pandas as pd

# Ruta
ruta_original = "/Users/carcerezo/Desktop/TFG/DATASET/bigrama_tfidf.csv"

# CSV
df = pd.read_csv(ruta_original)
df["tfidf"] = pd.to_numeric(df["tfidf"], errors="coerce")
df["tfidf"] = df["tfidf"].apply(lambda x: x / 1000 if x > 1 else x)

# 4 decimales
df["tfidf"] = df["tfidf"].round(4)

# guardar
ruta_salida = "/Users/carcerezo/Desktop/TFG/DATASET/bigrama_tfidf_corregido.csv"
df.to_csv(ruta_salida, index=False)

print(f"CSV corregido guardado en: {ruta_salida}")
