import pandas as pd

# Ruta al archivo con el texto limpio
ruta = '/Users/carcerezo/Desktop/TFG/discursos_fomc_limpios.csv'

# Cargar el dataset
df = pd.read_csv(ruta)

# Mostrar 5 discursos completos de la columna 'texto_limpio'
print("\nPrimeras 5 entradas del campo texto_limpio:\n")
for i, texto in enumerate(df["texto_limpio"].head()):
    print(f"\n--- Discurso {i+1} ---")
    print(texto)
