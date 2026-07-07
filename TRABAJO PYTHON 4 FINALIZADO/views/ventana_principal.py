"""
ventana_principal.py
====================

Ventana principal del sistema.
"""

import tkinter as tk
from tkinter import ttk

from views.panel_clientes import PanelClientes
from views.panel_servicios import PanelServicios
from views.panel_reservas import PanelReservas


class VentanaPrincipal(tk.Tk):
    """
    Ventana principal de la aplicación.
    """

    def __init__(
        self,
        controlador_clientes,
        controlador_servicios,
        controlador_reservas
    ):

        super().__init__()

        self.title("Software FJ")
        self.geometry("1100x700")
        self.minsize(1000, 650)

        # ==========================
        # Estilo
        # ==========================

        style = ttk.Style()
        style.theme_use("clam")
        style.configure(".", font=("Segoe UI", 10))

        # ==========================
        # Título
        # ==========================

        titulo = ttk.Label(
            self,
            text="SOFTWARE FJ\nSistema de Gestión de Reservas",
            font=("Segoe UI", 16, "bold")
        )

        titulo.pack(pady=10)

        # ==========================
        # Notebook
        # ==========================

        self.notebook = ttk.Notebook(self)

        self.notebook.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # ==========================
        # Paneles
        # ==========================

        self.panel_clientes = PanelClientes(
            self.notebook,
            controlador_clientes
        )

        self.panel_servicios = PanelServicios(
            self.notebook,
            controlador_servicios
        )

        self.panel_reservas = PanelReservas(
            self.notebook,
            controlador_reservas,
            controlador_clientes,
            controlador_servicios
        )

        # ==========================
        # Agregar pestañas
        # ==========================

        self.notebook.add(
            self.panel_clientes,
            text="Clientes"
        )

        self.notebook.add(
            self.panel_servicios,
            text="Servicios"
        )

        self.notebook.add(
            self.panel_reservas,
            text="Reservas"
        )

        # ==========================
        # Detectar cambio de pestaña
        # ==========================

        self.notebook.bind(
            "<<NotebookTabChanged>>",
            self._cambio_pestana
        )

        # ==========================
        # Barra de estado
        # ==========================

        self.estado = ttk.Label(
            self,
            text="Sistema listo.",
            relief="sunken",
            anchor="w"
        )

        self.estado.pack(fill="x")

    # =====================================================
    # EVENTOS
    # =====================================================

    def _cambio_pestana(self, event):
        """
        Se ejecuta cuando el usuario cambia de pestaña.
        """

        pestaña_actual = event.widget.select()

        widget = event.widget.nametowidget(pestaña_actual)

        if widget == self.panel_reservas:

            self.panel_reservas.actualizar_datos()