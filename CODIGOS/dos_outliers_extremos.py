import pandas as pd

# cargar csv
ruta = "/Users/carcerezo/Desktop/TFG/outliers_eventos.csv"
df = pd.read_csv(ruta)

# columna sentimiento_textblob es numérica
df["sentimiento_textblob"] = pd.to_numeric(df["sentimiento_textblob"], errors="coerce")

# discursos más positivo y más negativo
outlier_positivo = df.loc[df["sentimiento_textblob"].idxmax()]
outlier_negativo = df.loc[df["sentimiento_textblob"].idxmin()]

# resultados
print("Discurso con sentimiento más positivo:")
print(outlier_positivo)
print("\nDiscurso con sentimiento más negativo:")
print(outlier_negativo)
