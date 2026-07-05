"""
almacenamiento.py
=================

Gestiona la creación de carpetas y archivos del proyecto, además de la
lectura y escritura de archivos JSON.

Autor: Jhohan Sebastian Ibarra Sánchez
Curso: Programación
Proyecto: Sistema Integral
"""

#Importamos al libreria JSON para la creación de archivos y lectura de archivos JSON que usaremos como remplazo
#De una base de datos.
import json

#Llamamos el archivo configuracion para poder saber donde se encuentra cada archivo o directorio que necesitamos
from config.configuracion import(
    DATA_DIR,
    ASSETS_DIR,
    CLIENTES_FILE,
    SERVICIOS_FILE,
    RESERVAS_FILE,
    LOG_FILE,
)

class Almacenamiento:
    """
    Gestiona todas las operaciones relacionadas con los archivos
    utilizados por el sistema.
    """

    @staticmethod
    def crear_estructura():
        """
        Crea automáticamente la estructura mínima del proyecto
        si no existe.
        """
        
        # Se encarga de crear carpetas principales, si no existen y si existen simplemente no lo hace
        # mkdir crea directorios, y (exist_ok=True) comrpueba si existe, y define que si existe esta bien.
        DATA_DIR.mkdir(exist_ok=True)
        ASSETS_DIR.mkdir(exist_ok=True)
        
        #Creamos una lista o agrupamos los archivos que deberian existir en el sistema
        archivos = (
            CLIENTES_FILE,
            SERVICIOS_FILE,
            RESERVAS_FILE,
        )

        #Con este for evaluamos si cada uno de los archivos existe o no usando como base la lista archivos para tener un codigo
        #mucho mas limpio
        for archivo in archivos:
            if not archivos.exist():
                
                with open(archivo, "w", encoding="utf-8") as f:

                    #Aca el dump creamos una lista vacia 
                    json.dump([], f, indent=4)

        if not LOG_FILE.exists():
            # El metodo que usamos Touch hace parte de un metodo PATH que en resumen hace  que si el archivo no existe lo cree vacio.
            LOG_FILE.touch()

    @staticmethod
    def cargar_json(ruta):
        """
        Lee un archivo JSON y devuelve su contenido.
        Parameters
        """
        if not ruta.exists():
            return []
        
        with open(ruta, "r", encoding="utf-8") as archivo :
            return json.load(archivo)
        
    @staticmethod
    def guardar_json(ruta, datos):
        """
        Guarda los datos en un archivo JSON.
        """

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )
    

        