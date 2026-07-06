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
    
    Natalia Liceth Muñoz Cabezas 
        interfaz
        import tkinter as tk
from tkinter import messagebox, ttk
import json
from models.almacenamiento import Almacenamiento 
from config.configuracion import CLIENTES_FILE, SERVICIOS_FILE, RESERVAS_FILE

# Asegurar que existan las carpetas y archivos 
try:
    Almacenamiento.crear_estructura()
except Exception as e:
    print(f"Error al inicializar carpetas: {e}")

def mostrar_contenido_archivo():
    # Obtener el archivo seleccionado en el desplegable
    opcion = combo_archivos.get()
    
    if opcion == "Clientes":
        ruta = CLIENTES_FILE
    elif opcion == "Servicios":
        ruta = SERVICIOS_FILE
    elif opcion == "Reservas":
        ruta = RESERVAS_FILE
    else:
        messagebox.showwarning("Atención", "Por favor seleccione un archivo válido.")
        return

    try:
        # Utiliza tu método estático para leer el JSON
        datos = Almacenamiento.cargar_json(ruta)
        
        # Limpiar el visor de texto e insertar los datos formateados
        txt_visor.config(state="normal")
        txt_visor.delete("1.0", tk.END)
        txt_visor.insert(tk.END, json.dumps(datos, indent=4, ensure_ascii=False))
        txt_visor.config(state="disabled")
        
        lbl_estado.config(text=f"Archivo cargado: {opcion}", fg="#28a745")
        
    except Exception as error:
        messagebox.showerror("Error de lectura", f"No se pudo leer el archivo: {str(error)}")

def limpiar_visor():
    txt_visor.config(state="normal")
    txt_visor.delete("1.0", tk.END)
    txt_visor.config(state="disabled")
    lbl_estado.config(text="Visor limpio", fg="#6c757d")

# Configuración de la Ventana Principal
ventana = tk.Tk()
ventana.title("Admin de Almacenamiento JSON")
ventana.geometry("500x550")
ventana.config(padx=15, pady=15)

# Sección de Control (Selector de Archivos)
frame_control = tk.LabelFrame(ventana, text=" Selector de Base de Datos (JSON) ", font=("Arial", 10, "bold"), padx=10, pady=10)
frame_control.pack(fill="x", pady=5)

tk.Label(frame_control, text="Seleccione Archivo:", font=("Arial", 10)).pack(side="left", padx=5)

combo_archivos = ttk.Combobox(frame_control, values=["Clientes", "Servicios", "Reservas"], font=("Arial", 10), state="readonly")
combo_archivos.set("Clientes")
combo_archivos.pack(side="left", fill="x", expand=True, padx=5)

btn_cargar = tk.Button(frame_control, text="Cargar Datos", command=mostrar_contenido_archivo, bg="#007bff", fg="white", font=("Arial", 10, "bold"))
btn_cargar.pack(side="left", padx=5)

# Barra de Estado Corta
lbl_estado = tk.Label(ventana, text="Estructura de archivos validada.", font=("Arial", 9, "italic"), fg="#6c757d")
lbl_estado.pack(anchor="w", pady=5)

# Visor de Texto para Datos JSON
tk.Label(ventana, text="Contenido del archivo seleccionado:", font=("Arial", 10, "bold")).pack(anchor="w", pady=5)

# Frame contenedor para agregar barra de desplazamiento al cuadro de texto
frame_texto = tk.Frame(ventana)
frame_texto.pack(fill="both", expand=True, pady=5)

scroll_y = tk.Scrollbar(frame_texto)
scroll_y.pack(side="right", fill="y")

txt_visor = tk.Text(frame_texto, font=("Consolas", 10), state="disabled", yscrollcommand=scroll_y.set, bg="#f8f9fa")
txt_visor.pack(side="left", fill="both", expand=True)
scroll_y.config(command=txt_visor.yview)

# Botón de limpieza inferior
btn_limpiar = tk.Button(ventana, text="Limpiar Visor", command=limpiar_visor, bg="#dc3545", fg="white", font=("Arial", 10, "bold"))
btn_limpiar.pack(fill="x", pady=5)

ventana.mainloop()

        
