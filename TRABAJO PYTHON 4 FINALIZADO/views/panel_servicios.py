"""
panel_servicios.py
==================

Panel encargado de administrar los servicios.
"""

import tkinter as tk
from tkinter import ttk, messagebox


class PanelServicios(ttk.Frame):
    """
    Panel para la gestión de servicios.
    """

    def __init__(self, parent, controlador):
        super().__init__(parent)

        self.controlador = controlador

        self._crear_componentes()
        self._cargar_tabla()

    # =====================================================
    # INTERFAZ
    # =====================================================

    def _crear_componentes(self):

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        formulario = ttk.LabelFrame(
            self,
            text="Datos del Servicio"
        )

        formulario.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="ew"
        )

        ttk.Label(
            formulario,
            text="Código:"
        ).grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.entry_codigo = ttk.Entry(formulario, width=30)
        self.entry_codigo.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.entry_nombre = ttk.Entry(formulario, width=30)
        self.entry_nombre.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(
            formulario,
            text="Precio:"
        ).grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.entry_precio = ttk.Entry(formulario, width=30)
        self.entry_precio.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(
            formulario,
            text="Duración (min):"
        ).grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.entry_duracion = ttk.Entry(formulario, width=30)
        self.entry_duracion.grid(row=3, column=1, padx=5, pady=5)

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

        # ============================
        # TABLA
        # ============================

        marco = ttk.LabelFrame(
            self,
            text="Servicios Registrados"
        )

        marco.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.tabla = ttk.Treeview(

            marco,

            columns=(

                "Codigo",

                "Nombre",

                "Precio",

                "Duracion"

            ),

            show="headings"

        )

        self.tabla.heading(
            "Codigo",
            text="Código"
        )

        self.tabla.heading(
            "Nombre",
            text="Nombre"
        )

        self.tabla.heading(
            "Precio",
            text="Precio"
        )

        self.tabla.heading(
            "Duracion",
            text="Duración"
        )

        self.tabla.column(
            "Codigo",
            width=90
        )

        self.tabla.column(
            "Nombre",
            width=220
        )

        self.tabla.column(
            "Precio",
            width=120
        )

        self.tabla.column(
            "Duracion",
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

    # =====================================================
    # CRUD
    # =====================================================

    def _registrar(self):

        try:

            self.controlador.registrar_servicio(

                self.entry_codigo.get(),

                self.entry_nombre.get(),

                float(self.entry_precio.get()),

                int(self.entry_duracion.get())

            )

            messagebox.showinfo(
                "Éxito",
                "Servicio registrado."
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

            self.controlador.actualizar_servicio(

               self.entry_codigo.get(),

               self.entry_nombre.get(),

               float(self.entry_precio.get()),

               int(self.entry_duracion.get())

            )
            messagebox.showinfo(
                "Éxito",
                "Servicio actualizado."
            )

            self._cargar_tabla()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def _eliminar(self):

        try:

            self.controlador.eliminar_servicio(
                self.entry_codigo.get()
            )

            self._limpiar()

            self._cargar_tabla()

            messagebox.showinfo(
                "Éxito",
                "Servicio eliminado."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def _limpiar(self):

        self.entry_codigo.delete(0, tk.END)

        self.entry_nombre.delete(0, tk.END)

        self.entry_precio.delete(0, tk.END)

        self.entry_duracion.delete(0, tk.END)

    def _cargar_tabla(self):

        for fila in self.tabla.get_children():

            self.tabla.delete(fila)

        for servicio in self.controlador.listar_servicios():

            self.tabla.insert(

                "",

                tk.END,

                values=(

                    servicio.codigo,

                    servicio.nombre,

                    servicio.precio,

                    servicio.duracion

                )

            )

    def _seleccionar(self, event):

        seleccion = self.tabla.selection()

        if not seleccion:
            return

        datos = self.tabla.item(
            seleccion[0],
            "values"
        )

        self._limpiar()

        self.entry_codigo.insert(0, datos[0])

        self.entry_nombre.insert(0, datos[1])

        self.entry_precio.insert(0, datos[2])

        self.entry_duracion.insert(0, datos[3])