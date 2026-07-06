"""
persona.py
==========

Define la clase Persona, utilizada como clase base para
las personas registradas en el sistema.
"""

from utils.validaciones import Validaciones

def __init__(self, nombre, telefono, correo):
    """
    Inicializa una persona.
    """

    if Validaciones.campo_vacio(nombre):
        raise ValueError("El nombre no puede estar vacío.")

    Validaciones.validar_telefono(telefono)
    Validaciones.validar_correo(correo)

    self._nombre = nombre
    self._telefono = telefono
    self._correo = correo

@property
def nombre(self):
    """
    Devuelve el nombre de la persona.
    """
    return self._nombre

@property
def telefono(self):
    """
    Devuelve el teléfono de la persona.
    """
    return self._telefono

@property
def correo(self):
    """
    Devuelve el correo electrónico de la persona.
    """
    return self._correo

def __str__(self):
    ""
    Devuelve una representación en texto del objeto.
    """

    return (
        f"Nombre: {self.nombre}\n"
        f"Teléfono: {self.telefono}\n"
        f"Correo: {self.correo}"
    )




Natalia Liceth Muñoz Cabezas
Inetrfaz
import tkinter as tk
from tkinter import messagebox
from persona import Persona  # Importa tu clase desde persona.py

# Lista para almacenar los objetos Persona 
personas_registradas = []

def registrar_usuario():
    # Obtener los datos de los campos de texto
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()
    
    try:
        # Se intenta instanciar la clase Persona (ejecuta tus validaciones)
        nueva_persona = Persona(nombre, telefono, correo)
        personas_registradas.append(nueva_persona)
        
        # Insertar el resultado formateado por tu __str__ en el componente de texto
        txt_registros.config(state="normal")
        txt_registros.insert(tk.END, str(nueva_persona) + "\n" + "-"*40 + "\n")
        txt_registros.config(state="disabled")
        
        # Limpiar los campos del formulario
        entry_nombre.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
        
        messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
        
    except ValueError as error:
        # Si ocurre un error en tus validaciones, lo muestra en una alerta
        messagebox.showerror("Error de Validación", str(error))

# Configuración de la Ventana Principal
ventana = tk.Tk()
ventana.title("Registro de Usuarios")
ventana.geometry("400x500")
ventana.config(padx=15, pady=15)

# Componentes Visuales Formulario
tk.Label(ventana, text="Nombre Completo:", font=("Arial", 10, "bold")).pack(anchor="w", pady=2)
entry_nombre = tk.Entry(ventana, font=("Arial", 11))
entry_nombre.pack(fill="x", pady=5)

tk.Label(ventana, text="Teléfono:", font=("Arial", 10, "bold")).pack(anchor="w", pady=2)
entry_telefono = tk.Entry(ventana, font=("Arial", 11))
entry_telefono.pack(fill="x", pady=5)

tk.Label(ventana, text="Correo Electrónico:", font=("Arial", 10, "bold")).pack(anchor="w", pady=2)
entry_correo = tk.Entry(ventana, font=("Arial", 11))
entry_correo.pack(fill="x", pady=5)

# Botón de Acción
btn_registrar = tk.Button(ventana, text="Registrar", command=registrar_usuario, bg="#28a745", fg="white", font=("Arial", 11, "bold"))
btn_registrar.pack(fill="x", pady=15)

# área de Texto para Mostrar Resultados
tk.Label(ventana, text="Usuarios Registrados:", font=("Arial", 10, "bold")).pack(anchor="w", pady=2)
txt_registros = tk.Text(ventana, font=("Arial", 10), height=12, state="disabled")
txt_registros.pack(fill="both", expand=True, pady=5)

# Iniciar la aplicación
ventana.mainloop()
