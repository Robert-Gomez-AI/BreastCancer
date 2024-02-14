import zipfile

import os


# Ruta del archivo ZIP que deseas extraer
ruta_archivo_zip = './archive.zip'
# Directorio de destino para la extracción    
directorio_destino = 'images'

def extract(ruta_archivo_zip,directorio_destino):
    # Abrir el archivo ZIP
    with zipfile.ZipFile(ruta_archivo_zip, 'r') as archivo_zip:
        # Extraer todos los archivos en el directorio de destino
        archivo_zip.extractall(directorio_destino)

    print("Archivo ZIP extraído exitosamente.")



# Directorio de la carpeta que deseas revisar
directorio = 'images/Dataset_BUSI_with_GT'
folders=['benign','malignant','normal']

# Cadena de texto a buscar en los nombres de archivo
cadena_a_buscar = 'mask'

def filtrar(directorio,cadena):
    # Recorrer todos los archivos en el directorio
    for nombre_archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, nombre_archivo)
        if os.path.isfile(ruta_archivo):
            # Verificar si el nombre de archivo incluye la cadena de texto
            if cadena in nombre_archivo:
                # Eliminar el archivo
                os.remove(ruta_archivo)
                print(f"Archivo eliminado: {nombre_archivo}")

    print("Proceso completo.")

extract(ruta_archivo_zip,directorio_destino)

for folder in folders:
    filtrar(directorio+'/'+folder,cadena_a_buscar)