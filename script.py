import os

# Carpeta que contiene los archivos
carpeta = r"C:\Users\joeln\Desktop\IACC\Segundo Año\Ciclo 4\SEM3_PROIF1301-19\Tarea3"

# Obtener solamente los archivos con extensión .log
archivos_log = [
    archivo for archivo in os.listdir(carpeta)
    if archivo.lower().endswith(".log")
]

# Ordenar los archivos para mantener un orden definido
archivos_log.sort()

# Renombrar los archivos encontrados
for numero, archivo in enumerate(archivos_log, start=1):
    ruta_original = os.path.join(carpeta, archivo)
    nuevo_nombre = f"Joel_Zuniga_{numero}.log"
    nueva_ruta = os.path.join(carpeta, nuevo_nombre)

    os.rename(ruta_original, nueva_ruta)

    print(f"{archivo} -> {nuevo_nombre}")

print(f"\nProceso finalizado. Se renombraron {len(archivos_log)} archivos.")