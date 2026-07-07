"""
panel_reservas.py
=================

Panel para la gestión de reservas.
"""

import tkinter as tk
from tkinter import ttk, messagebox


class PanelReservas(ttk.Frame):
    """
    Panel para administrar las reservas.
    """

    def __init__(
        self,
        parent,
        controlador_reservas,
        controlador_clientes,
        controlador_servicios
    ):

        super().__init__(parent)

        self.controlador = controlador_reservas
        self.controlador_clientes = controlador_clientes
        self.controlador_servicios = controlador_servicios

        self._crear_componentes()
        self._cargar_combobox()
        self._cargar_tabla()

    # =====================================================
    # INTERFAZ
    # =====================================================

    def _crear_componentes(self):

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        formulario = ttk.LabelFrame(
            self,
            text="Datos de la Reserva"
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
        ).grid(row=0, column=0, padx=5, pady=5)

        self.entry_codigo = ttk.Entry(formulario, width=30)
        self.entry_codigo.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(
            formulario,
            text="Cliente:"
        ).grid(row=1, column=0, padx=5, pady=5)

        self.combo_cliente = ttk.Combobox(
            formulario,
            width=40,
            state="readonly"
        )

        self.combo_cliente.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Servicio:"
        ).grid(row=2, column=0, padx=5, pady=5)

        self.combo_servicio = ttk.Combobox(
            formulario,
            width=40,
            state="readonly"
        )

        self.combo_servicio.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Fecha:"
        ).grid(row=3, column=0, padx=5, pady=5)

        self.entry_fecha = ttk.Entry(
            formulario,
            width=30
        )

        self.entry_fecha.grid(
            row=3,
            column=1,
            padx=5,
            pady=5
        )

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
            text="Cancelar",
            command=self._cancelar
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

        # ==============================
        # TABLA
        # ==============================

        self.tabla = ttk.Treeview(

            self,

            columns=(

                "Codigo",

                "Cliente",

                "Servicio",

                "Fecha",

                "Estado"

            ),

            show="headings"

        )

        for columna in (
            "Codigo",
            "Cliente",
            "Servicio",
            "Fecha",
            "Estado"
        ):

            self.tabla.heading(
                columna,
                text=columna
            )

        self.tabla.column("Codigo", width=100)
        self.tabla.column("Cliente", width=220)
        self.tabla.column("Servicio", width=220)
        self.tabla.column("Fecha", width=120)
        self.tabla.column("Estado", width=120)

        self.tabla.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.tabla.bind(
            "<<TreeviewSelect>>",
            self._seleccionar
        )

    # =====================================================
    # CARGA DE DATOS
    # =====================================================

    def _cargar_combobox(self):
        """
        Recarga clientes y servicios.
        """

        clientes = [
            f"{cliente.cedula} - {cliente.nombre}"
            for cliente in self.controlador_clientes.listar_clientes()
        ]

        self.combo_cliente["values"] = clientes

        servicios = [
            f"{servicio.codigo} - {servicio.nombre}"
            for servicio in self.controlador_servicios.listar_servicios()
        ]

        self.combo_servicio["values"] = servicios

    def _cargar_tabla(self):
        """
        Carga las reservas.
        """

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for reserva in self.controlador.listar_reservas():

            self.tabla.insert(

                "",

                tk.END,

                values=(

                    reserva.codigo,

                    reserva.cliente.nombre,

                    reserva.servicio.nombre,

                    reserva.fecha,

                    reserva.estado

                )

            )

    # =====================================================
    # CRUD
    # =====================================================

    def _registrar(self):

        try:

            if not self.combo_cliente.get():
                raise ValueError("Seleccione un cliente.")

            if not self.combo_servicio.get():
                raise ValueError("Seleccione un servicio.")

            cedula = self.combo_cliente.get().split(" - ")[0]

            codigo_servicio = self.combo_servicio.get().split(" - ")[0]

            self.controlador.registrar_reserva(

                self.entry_codigo.get().strip(),

                cedula,

                codigo_servicio,

                self.entry_fecha.get().strip()

            )

            messagebox.showinfo(
                "Éxito",
                "Reserva registrada correctamente."
            )

            self._limpiar()
            self.actualizar_datos()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def _cancelar(self):

        try:

            codigo = self.entry_codigo.get().strip()

            if not codigo:
                raise ValueError("Seleccione una reserva.")

            self.controlador.cancelar_reserva(codigo)

            messagebox.showinfo(
                "Éxito",
                "Reserva cancelada correctamente."
            )

            self.actualizar_datos()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def _eliminar(self):

        try:

            codigo = self.entry_codigo.get().strip()

            if not codigo:
                raise ValueError("Seleccione una reserva.")

            if not messagebox.askyesno(
                "Confirmar",
                "¿Desea eliminar esta reserva?"
            ):
                return

            self.controlador.eliminar_reserva(codigo)

            messagebox.showinfo(
                "Éxito",
                "Reserva eliminada correctamente."
            )

            self._limpiar()
            self.actualizar_datos()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =====================================================
    # UTILIDADES
    # =====================================================

    def _limpiar(self):

        self.entry_codigo.delete(0, tk.END)
        self.combo_cliente.set("")
        self.combo_servicio.set("")
        self.entry_fecha.delete(0, tk.END)

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

        for indice, cliente in enumerate(self.combo_cliente["values"]):

            if datos[1] in cliente:

                self.combo_cliente.current(indice)

                break

        for indice, servicio in enumerate(self.combo_servicio["values"]):

            if datos[2] in servicio:

                self.combo_servicio.current(indice)

                break

        self.entry_fecha.insert(0, datos[3])

    def actualizar_datos(self):
        """
        Actualiza toda la información del panel.
        """

        self._cargar_combobox()
        self._cargar_tabla()