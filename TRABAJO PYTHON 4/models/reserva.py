"""
reserva.py
==========

Define la clase Reserva.
"""

from models.cliente import Cliente
from models.servicio import Servicio


class Reserva:
    """
    Representa una reserva realizada por un cliente.
    """

    def __init__(self, codigo, cliente, servicio, fecha, estado="Activa"):

        if not isinstance(cliente, Cliente):
            raise TypeError("cliente debe ser un objeto Cliente.")

        if not isinstance(servicio, Servicio):
            raise TypeError("servicio debe ser un objeto Servicio.")

        self._codigo = codigo
        self._cliente = cliente
        self._servicio = servicio
        self._fecha = fecha
        self._estado = estado

    @property
    def codigo(self):
        return self._codigo

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def fecha(self):
        return self._fecha

    @property
    def estado(self):
        return self._estado

    def cancelar(self):
        """
        Cancela la reserva.
        """
        self._estado = "Cancelada"

    def __str__(self):
        return (
            f"Código: {self.codigo}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Fecha: {self.fecha}\n"
            f"Estado: {self.estado}"
        )

Natalia Liceth Muñoz Cabezas 
Interfaz 
import tkinter as tk
from tkinter import messagebox, ttk
from models.reserva import Reserva
from models.cliente import Cliente
from models.servicio import Servicio

lista_clientes = obtener_clientes_de_la_base_de_datos() 
lista_servicios = obtener_servicios_de_la_base_de_datos()


def registrar_reserva():
    codigo = entry_codigo.get()
    fecha = entry_fecha.get()
    
    # Obtener el índice seleccionado en los desplegables
    idx_cliente = combo_cliente.current()
    idx_servicio = combo_servicio.current()
    
    if idx_cliente == -1 or idx_servicio == -1:
        messagebox.showerror("Error", "Debe seleccionar un Cliente y un Servicio válido.")
        return

    # Extraer los objetos reales de las listas
    cliente_obj = lista_clientes[idx_cliente]
    servicio_obj = lista_servicios[idx_servicio]
    
    try:
        # Instanciar la clase Reserva detonando tus validaciones isinstance
        nueva_reserva = Reserva(codigo, cliente_obj, servicio_obj, fecha)
        lista_reservas.append(nueva_reserva)
        
        actualizar_lista_visual()
        limpiar_campos()
        messagebox.showinfo("Éxito", "Reserva registrada correctamente.")
        
    except (TypeError, ValueError) as error:
        messagebox.showerror("Error de Validación", str(error))

def cancelar_reserva_seleccionada():
    # Obtener la reserva seleccionada en la lista visual
    seleccion = listbox_reservas.curselection()
    if not seleccion:
        messagebox.showwarning("Atención", "Seleccione una reserva de la lista para cancelarla.")
        return
    
    indice = seleccion[0]
    reserva_obj = lista_reservas[indice]
    reserva_obj.cancelar() # Llama a tu método nativo de la clase
    
    actualizar_lista_visual()
    messagebox.showinfo("Cancelada", f"La reserva {reserva_obj.codigo} ha sido cancelada.")

def actualizar_lista_visual():
    listbox_reservas.delete(0, tk.END)
    for res in lista_reservas:
        # Muestra una línea compacta en la lista
        listbox_reservas.insert(tk.END, f"[{res.codigo}] {res.cliente.nombre} - {res.servicio.nombre} ({res.estado})")

def limpiar_campos():
    entry_codigo.delete(0, tk.END)
    entry_fecha.delete(0, tk.END)
    combo_cliente.set('')
    combo_servicio.set('')

# Configuración Ventana Principal
ventana = tk.Tk()
ventana.title("Gestor de Reservas")
ventana.geometry("450x600")
ventana.config(padx=15, pady=15)

# Formulario de Entrada
tk.Label(ventana, text="Código de Reserva:", font=("Arial", 10, "bold")).pack(anchor="w", pady=2)
entry_codigo = tk.Entry(ventana, font=("Arial", 11))
entry_codigo.pack(fill="x", pady=4)

tk.Label(ventana, text="Seleccionar Cliente:", font=("Arial", 10, "bold")).pack(anchor="w", pady=2)
combo_cliente = ttk.Combobox(ventana, font=("Arial", 11), state="readonly")
combo_cliente['values'] = [c.nombre for c in lista_clientes] # Muestra solo nombres en la interfaz
combo_cliente.pack(fill="x", pady=4)

tk.Label(ventana, text="Seleccionar Servicio:", font=("Arial", 10, "bold")).pack(anchor="w", pady=2)
combo_servicio = ttk.Combobox(ventana, font=("Arial", 11), state="readonly")
combo_servicio['values'] = [s.nombre for s in lista_servicios]
combo_servicio.pack(fill="x", pady=4)

tk.Label(ventana, text="Fecha (DD/MM/AAAA):", font=("Arial", 10, "bold")).pack(anchor="w", pady=2)
entry_fecha = tk.Entry(ventana, font=("Arial", 11))
entry_fecha.pack(fill="x", pady=4)

# Botón Guardar
btn_guardar = tk.Button(ventana, text="Crear Reserva", command=registrar_reserva, bg="#007bff", fg="white", font=("Arial", 11, "bold"))
btn_guardar.pack(fill="x", pady=10)

# Lista Visual y Acción de Cancelación
tk.Label(ventana, text="Control de Reservas Existentes:", font=("Arial", 10, "bold")).pack(anchor="w", pady=5)
listbox_reservas = tk.Listbox(ventana, font=("Arial", 10), height=10)
listbox_reservas.pack(fill="both", expand=True, pady=2)

btn_cancelar = tk.Button(ventana, text="Cancelar Reserva Seleccionada", command=cancelar_reserva_seleccionada, bg="#dc3545", fg="white", font=("Arial", 10, "bold"))
btn_cancelar.pack(fill="x", pady=5)

ventana.mainloop()
