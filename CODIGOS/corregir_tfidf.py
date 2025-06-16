import pandas as pd

# Ruta CSV
ruta_original = "/Users/carcerezo/Desktop/TFG/DATASET/bigrama_tfidf.csv"
ruta_corregida = "/Users/carcerezo/Desktop/TFG/DATASET/bigrama_tfidf_corregido.csv"

# Leer CSV
df = pd.read_csv(ruta_original)

# convertir a numérico 
df["tfidf"] = pd.to_numeric(df["tfidf"], errors="coerce")

# eliminar filas 
df_limpio = df.dropna(subset=["tfidf"])

# redondear 
df_limpio["tfidf"] = df_limpio["tfidf"].round(4)

# guardar csv 
df_limpio.to_csv(ruta_corregida, index=False)

print(" Archivo corregido guardado como:")
print(ruta_corregida)
