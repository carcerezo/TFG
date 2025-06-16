import pandas as pd

df = pd.read_csv('/Users/carcerezo/Desktop/TFG/discursos_fomc_limpios.csv')

print("\nEjemplo de textos únicos encontrados en texto_limpio:")
print(df["texto_limpio"].nunique())

print("\n¿Cantidad total de filas en el dataset?")
print(len(df))


df = pd.read_csv('/Users/carcerezo/Desktop/TFG/discursos_fomc_con_sentimiento.csv')

print("\nScores aleatorios:")
print(df["sentimiento_compound"].sample(10))
