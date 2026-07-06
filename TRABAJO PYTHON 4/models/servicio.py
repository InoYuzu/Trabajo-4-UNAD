"""
servicio.py
===========

Define la clase Servicio.
"""
from utils.validaciones import Validaciones

class Servicio:
    """
    Representa un servicio ofrecido por la empresa.
    """

    def __init__(self, codigo, nombre, precio, duracion):
        """
        Inicializa un servicio.
        """
        if Validaciones.campo_vacio(codigo):
            raise ValueError("El código no puede estar vacío.")

        if Validaciones.campo_vacio(nombre):
            raise ValueError("El nombre no puede estar vacío.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        if duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero.")

        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._duracion = duracion

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def duracion(self):
        return self._duracion

    def __str__(self):
        return (
        
            f"Código: {self.codigo}\n"
            f"Nombre: {self.nombre}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Duración: {self.duracion} minutos"
        )

Natalia Liceth Muñoz Cabezas
interfaz import tkinter as tk
from tkinter import messagebox
from models.servicio import Servicio  # Importa tu clase desde tu estructura

# Lista para almacenar los objetos Servicio 
servicios_registrados = []

def registrar_servicio():
    codigo = entry_codigo.get()
    nombre = entry_nombre.get()
    
    try:
        # Convertir entradas de texto a tipos numéricos para las validaciones
        precio = float(entry_precio.get()) if entry_precio.get() else 0.0
        duracion = int(entry_duracion.get()) if entry_duracion.get() else 0
    except ValueError:
        messagebox.showerror("Error de Formato", "El precio debe ser un número decimal y la duración un número entero.")
        return

    try:
        # Se instancia la clase Servicio detonando tus validaciones nativas
        nuevo_servicio = Servicio(codigo, nombre, precio, duracion)
        servicios_registrados.append(nuevo_servicio)
        
        # Insertar el resultado formateado por tu __str__ en el componente de texto
        txt_registros.config(state="normal")
        txt_registros.insert(tk.END, str(nuevo_servicio) + "\n" + "-"*40 + "\n")
        txt_registros.config(state="disabled")
        
        # Limpiar los campos del formulario
        limpiar_campos()
        messagebox.showinfo("Éxito", "Servicio registrado correctamente.")
        
    except ValueError as error:
        # Captura tus mensajes: "El precio debe ser mayor que cero", etc.
        messagebox.showerror("Error de Validación", str(error))

def limpiar_campos():
    entry_codigo.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_duracion.delete(0, tk.END)

# Configuración de la Ventana Principal
ventana = tk.Tk()
ventana.title("Registro de Servicios")
ventana.geometry("400x550")
ventana.config(padx=15, pady=15)

# Componentes Visuales (Formulario)
tk.Label(ventana, text="Código del Servicio:", font=("Arial", 10, "bold")).pack(anchor="w", pady=2)
entry_codigo = tk.Entry(ventana, font=("Arial", 11))
entry_codigo.pack(fill="x", pady=4)

tk.Label(ventana, text="Nombre del Servicio:", font=("Arial", 10, "bold")).pack(anchor="w", pady=2)
entry_nombre = tk.Entry(ventana, font=("Arial", 11))
entry_nombre.pack(fill="x", pady=4)

tk.Label(ventana, text="Precio ($):", font=("Arial", 10, "bold")).pack(anchor="w", pady=2)
entry_precio = tk.Entry(ventana, font=("Arial", 11))
entry_precio.pack(fill="x", pady=4)

tk.Label(ventana, text="Duración (minutos):", font=("Arial", 10, "bold")).pack(anchor="w", pady=2)
entry_duracion = tk.Entry(ventana, font=("Arial", 11))
entry_duracion.pack(fill="x", pady=4)

# Botón de Acción
btn_registrar = tk.Button(ventana, text="Registrar Servicio", command=registrar_servicio, bg="#28a745", fg="white", font=("Arial", 11, "bold"))
btn_registrar.pack(fill="x", pady=15)

# Área de Texto para Mostrar Resultados
tk.Label(ventana, text="Servicios Ofrecidos:", font=("Arial", 10, "bold")).pack(anchor="w", pady=2)
txt_registros = tk.Text(ventana, font=("Arial", 10), height=12, state="disabled")
txt_registros.pack(fill="both", expand=True, pady=5)

# Iniciar la aplicación
ventana.mainloop()
