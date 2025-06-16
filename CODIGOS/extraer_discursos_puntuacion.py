import os
import fitz  # PyMuPDF
import pandas as pd
import re
from datetime import datetime

# ruta carpetas de años
ruta_raiz = "/Users/carcerezo/Desktop/TFG/DATASET/"


resultados = []

# nombre del archivo
def extraer_fecha(nombre_archivo):
    match = re.search(r'(\d{4})(\d{2})(\d{2})', nombre_archivo)
    if match:
        try:
            return datetime.strptime(match.group(0), '%Y%m%d').date()
        except:
            return None
    return None

# ignorar carpetas de statements
for carpeta_actual, subcarpetas, archivos in os.walk(ruta_raiz):
    if "statements" in carpeta_actual.lower():
        continue

    for archivo in archivos:
        if archivo.lower().endswith(".pdf"):
            ruta_pdf = os.path.join(carpeta_actual, archivo)
            try:
                doc = fitz.open(ruta_pdf)
                texto = ""
                for pagina in doc:
                    texto += pagina.get_text()
                texto = re.sub(r'\s+', ' ', texto).strip()
                fecha = extraer_fecha(archivo)
                resultados.append({
                    "archivo": archivo,
                    "fecha": fecha,
                    "texto_completo_con_puntuacion": texto
                })
            except Exception as e:
                print(f" Error al procesar {archivo}: {e}")

# ordenar por fecha y guardar
df = pd.DataFrame(resultados)
df = df.sort_values(by="fecha")
df.to_csv("/Users/carcerezo/Desktop/TFG/discursos_texto_con_puntuacion.csv", index=False)

print(" Archivo generado correctamente en /TFG, ordenado por fecha.")
