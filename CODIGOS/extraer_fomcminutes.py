import os
import fitz  # PyMuPDF
import re
import pandas as pd

ruta_base = "/Users/carcerezo/Desktop/TFG/DATASET"
ruta_salida = "/Users/carcerezo/Desktop/TFG/discursos_fomc_limpios.csv"
data = []

for raiz, carpetas, archivos in os.walk(ruta_base):
    for archivo in archivos:
        if archivo.lower().startswith("fomcminutes") and archivo.lower().endswith(".pdf"):
            ruta_archivo = os.path.join(raiz, archivo)
            try:
                texto_total = ""
                with fitz.open(ruta_archivo) as doc:
                    for pagina in doc:
                        texto_total += pagina.get_text()

                texto_limpio = texto_total.lower()
                texto_limpio = re.sub(r'\n+', ' ', texto_limpio)
                texto_limpio = re.sub(r'[^a-zA-Z\s]', '', texto_limpio)
                texto_limpio = re.sub(r'\s+', ' ', texto_limpio).strip()

                año = archivo[11:15] if archivo[11:15].isdigit() else "desconocido"

                data.append({
                    "año": año,
                    "archivo": archivo,
                    "texto_limpio": texto_limpio
                })

                print(f" Procesado: {archivo} ({año})")

            except Exception as e:
                print(f" Error leyendo {archivo}: {e}")

df = pd.DataFrame(data)
df = df.sort_values(by=["año", "archivo"])
df.to_csv(ruta_salida, index=False)

print(f"\n TOTAL DISCURSOS GUARDADOS: {len(df)} en: {ruta_salida}")
