import pandas as pd

# Ruta original del CSV
ruta_original = "/Users/carcerezo/Desktop/TFG/DATASET/bigrama_tfidf.csv"
ruta_corregida = "/Users/carcerezo/Desktop/TFG/DATASET/bigrama_tfidf_corregido.csv"

# Leer CSV
df = pd.read_csv(ruta_original)

# Convertir a numérico y forzar errores como NaN
df["tfidf"] = pd.to_numeric(df["tfidf"], errors="coerce")

# Eliminar filas donde tfidf sea NaN (los que fallaron)
df_limpio = df.dropna(subset=["tfidf"])

# Redondear por estética si lo necesitas
df_limpio["tfidf"] = df_limpio["tfidf"].round(4)

# Guardar CSV corregido
df_limpio.to_csv(ruta_corregida, index=False)

print("✅ Archivo corregido guardado como:")
print(ruta_corregida)
