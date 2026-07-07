"""
panel_clientes.py
=================

Panel encargado de administrar los clientes.
"""

import tkinter as tk
from tkinter import ttk, messagebox


class PanelClientes(ttk.Frame):
    """
    Panel para la gestión de clientes.
    """

    def __init__(self, parent, controlador):
        super().__init__(parent)

        self.controlador = controlador

        self._crear_componentes()

        self._cargar_tabla()

    # ==================================================
    # CREACIÓN DE LA INTERFAZ
    # ==================================================

    def _crear_componentes(self):

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self._crear_formulario()

        self._crear_tabla()

    def _crear_formulario(self):

        formulario = ttk.LabelFrame(
            self,
            text="Datos del Cliente"
        )

        formulario.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=10,
            pady=10
        )

        # --------------------------
        # Nombre
        # --------------------------

        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.entry_nombre = ttk.Entry(
            formulario,
            width=35
        )

        self.entry_nombre.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        # --------------------------
        # Teléfono
        # --------------------------

        ttk.Label(
            formulario,
            text="Teléfono:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.entry_telefono = ttk.Entry(
            formulario,
            width=35
        )

        self.entry_telefono.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        # --------------------------
        # Correo
        # --------------------------

        ttk.Label(
            formulario,
            text="Correo:"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.entry_correo = ttk.Entry(
            formulario,
            width=35
        )

        self.entry_correo.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )

        # --------------------------
        # Cédula
        # --------------------------

        ttk.Label(
            formulario,
            text="Cédula:"
        ).grid(
            row=3,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.entry_cedula = ttk.Entry(
            formulario,
            width=35
        )

        self.entry_cedula.grid(
            row=3,
            column=1,
            padx=5,
            pady=5
        )

        # --------------------------
        # Botones
        # --------------------------

        botones = ttk.Frame(formulario)

        botones.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=10
        )

        ttk.Button(
            botones,
            text="Registrar",
            command=self._registrar
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            botones,
            text="Actualizar",
            command=self._actualizar
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            botones,
            text="Eliminar",
            command=self._eliminar
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            botones,
            text="Limpiar",
            command=self._limpiar
        ).pack(side=tk.LEFT, padx=5)

    def _crear_tabla(self):

        marco = ttk.LabelFrame(
            self,
            text="Clientes Registrados"
        )

        marco.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.tabla = ttk.Treeview(

            marco,

            columns=(
                "Nombre",
                "Telefono",
                "Correo",
                "Cedula"
            ),

            show="headings"
        )

        self.tabla.heading(
            "Nombre",
            text="Nombre"
        )

        self.tabla.heading(
            "Telefono",
            text="Teléfono"
        )

        self.tabla.heading(
            "Correo",
            text="Correo"
        )

        self.tabla.heading(
            "Cedula",
            text="Cédula"
        )

        self.tabla.column(
            "Nombre",
            width=180
        )

        self.tabla.column(
            "Telefono",
            width=120
        )

        self.tabla.column(
            "Correo",
            width=220
        )

        self.tabla.column(
            "Cedula",
            width=120
        )

        scrollbar = ttk.Scrollbar(

            marco,

            orient="vertical",

            command=self.tabla.yview
        )

        self.tabla.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True
        )

        scrollbar.pack(
            side=tk.RIGHT,
            fill=tk.Y
        )

        self.tabla.bind(
            "<<TreeviewSelect>>",
            self._seleccionar
        )

    # ==================================================
    # FUNCIONES
    # ==================================================

    def _registrar(self):

        try:

            self.controlador.registrar_cliente(

                self.entry_nombre.get(),

                self.entry_telefono.get(),

                self.entry_correo.get(),

                self.entry_cedula.get()

            )

            messagebox.showinfo(
                "Éxito",
                "Cliente registrado."
            )

            self._limpiar()

            self._cargar_tabla()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def _actualizar(self):

        try:

            self.controlador.actualizar_cliente(

                self.entry_cedula.get(),

                self.entry_nombre.get(),

                self.entry_telefono.get(),

                self.entry_correo.get()

            )

            messagebox.showinfo(
                "Éxito",
                "Cliente actualizado."
            )

            self._cargar_tabla()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def _eliminar(self):

        try:

            self.controlador.eliminar_cliente(
                self.entry_cedula.get()
            )

            messagebox.showinfo(
                "Éxito",
                "Cliente eliminado."
            )

            self._limpiar()

            self._cargar_tabla()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def _limpiar(self):

        self.entry_nombre.delete(0, tk.END)

        self.entry_telefono.delete(0, tk.END)

        self.entry_correo.delete(0, tk.END)

        self.entry_cedula.delete(0, tk.END)

    def _cargar_tabla(self):

        for fila in self.tabla.get_children():

            self.tabla.delete(fila)

        for cliente in self.controlador.listar_clientes():

            self.tabla.insert(

                "",

                tk.END,

                values=(

                    cliente.nombre,

                    cliente.telefono,

                    cliente.correo,

                    cliente.cedula

                )
            )

    def _seleccionar(self, event):

        seleccion = self.tabla.selection()

        if not seleccion:
            return

        valores = self.tabla.item(
            seleccion[0],
            "values"
        )

        self._limpiar()

        self.entry_nombre.insert(
            0,
            valores[0]
        )

        self.entry_telefono.insert(
            0,
            valores[1]
        )

        self.entry_correo.insert(
            0,
            valores[2]
        )

        self.entry_cedula.insert(
            0,
            valores[3]
        )