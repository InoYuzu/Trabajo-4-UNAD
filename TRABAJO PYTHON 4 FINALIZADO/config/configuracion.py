"""
configuracion.py
================

Este módulo centraliza toda la configuración del proyecto.

También se encarga de preparar automáticamente el entorno
de trabajo cuando la aplicación se ejecuta por primera vez.

Autor: Jhohan Sebastian Ibarra Sánchez
Curso: Programación
Proyecto: Sistema Integral
"""



#Importo la libreria pathlib para hacer un mejor manejo de las rutas del archivo
#Asi python manejara las rutas no como cadenas de texto si no como objetos facilitando la ejecución
from pathlib import Path
import json

# ==========================================================
# RUTAS PRINCIPALES DEL PROYECTO
# ==========================================================

#Path(__file__) Convierte la ruta del archivo actual en un objeto Path.
#.resolve() obtiene la ruta absoluta, es principalmente para evitar problemas si el archivo se ejecuta desde otra carpeta
#.parents.parents obtiene el directorio raiz del proyecto basicamente desplazandose dos niveles
RAIZ_PROYECTO = Path(__file__).resolve().parent.parent


#Aca le decimos al sistema que la carpeta "Data" existira en la raiz del sistema
DATA_DIR = RAIZ_PROYECTO / "data"

#Aca le decimos al sistema que la carpeta "assets" existira en la raiz del sistema
ASSETS_DIR = RAIZ_PROYECTO / "assets"

#Aca le decimos al sistema que la carpeta "config" existira en la raiz del sistema
CONFIG_DIR = RAIZ_PROYECTO / "config"

#Aca le decimos al sistema que la carpeta "models" existira en la raiz del sistema
MODELS_DIR = RAIZ_PROYECTO / "models"

#Aca le decimos al sistema que la carpeta "views" existira en la raiz del sistema
VIEWS_DIR = RAIZ_PROYECTO / "views"

#Aca le decimos al sistema que la carpeta "controllers" existira en la raiz del sistema
CONTROLLERS_DIR = RAIZ_PROYECTO / "controllers"

#Aca le decimos al sistema que la carpeta "utils" existira en la raiz del sistema
UTILS_DIR = RAIZ_PROYECTO / "utils"

#Aca le decimos al sistema donde deberia estar cada archivo generado por el sistema
CLIENTES_FILE = DATA_DIR / "clientes.json"
SERVICIOS_FILE = DATA_DIR / "servicios.json"
RESERVAS_FILE = DATA_DIR / "reservas.json"
LOG_FILE = DATA_DIR / "logs.txt"

def preparar_entorno():
    """
    Crea automáticamente las carpetas y archivos necesarios
    para que el sistema funcione correctamente.
    """

    # Crear la carpeta data si no existe
    DATA_DIR.mkdir(exist_ok=True)

    # Crear los archivos JSON si no existen
    for archivo in (
        CLIENTES_FILE,
        SERVICIOS_FILE,
        RESERVAS_FILE
    ):

        if not archivo.exists():

            with open(
                archivo,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    [],
                    f,
                    indent=4,
                    ensure_ascii=False
                )

    # Crear el archivo de logs si no existe
    if not LOG_FILE.exists():

        LOG_FILE.touch()

