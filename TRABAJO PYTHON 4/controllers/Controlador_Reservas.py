"""
controlador_reservas.py
=======================

Gestiona todas las operaciones relacionadas con las reservas.
"""

from config.configuracion import RESERVAS_FILE
from models.reserva import Reserva
from utils.almacenamiento import Almacenamiento
from utils.logger import Logger


class ControladorReservas:
    """
    Controlador encargado de administrar las reservas.
    """

    def __init__(
        self,
        controlador_clientes,
        controlador_servicios
    ):
        """
        Inicializa el controlador de reservas.

        Parameters
        ----------
        controlador_clientes: Controlador encargado de administrar clientes.
        controlador_servicios: Controlador encargado de administrar servicios.
        """

        self._reservas = []

        self._controlador_clientes = controlador_clientes
        self._controlador_servicios = controlador_servicios

        self.cargar()

    def cargar(self):
        """
        Carga las reservas desde el archivo JSON.
        """

        datos = Almacenamiento.cargar_json(
            RESERVAS_FILE
        )

        self._reservas.clear()

        for reserva in datos:

            cliente = self._controlador_clientes.buscar_cliente(
                reserva["cliente"]
            )

            servicio = self._controlador_servicios.buscar_servicio(
                reserva["servicio"]
            )

            if cliente is None or servicio is None:
                continue

            nueva_reserva = Reserva(
                reserva["codigo"],
                cliente,
                servicio,
                reserva["fecha"],
                reserva.get("estado", "Activa")
            )

            self._reservas.append(
                nueva_reserva
            )

    def convertir_a_diccionario(self, reserva):
        """
        Convierte una reserva en un diccionario.
        """

        return {

            "codigo": reserva.codigo,

            "cliente": reserva.cliente.cedula,

            "servicio": reserva.servicio.codigo,

            "fecha": reserva.fecha,

            "estado": reserva.estado
        }

    def guardar(self):
        """
        Guarda todas las reservas en el archivo JSON.
        """

        datos = []

        for reserva in self._reservas:

            datos.append(
                self.convertir_a_diccionario(reserva)
            )

        Almacenamiento.guardar_json(
            RESERVAS_FILE,
            datos
        )

    def registrar_reserva(
        self,
        codigo,
        cedula_cliente,
        codigo_servicio,
        fecha
    ):
        """
        Registra una nueva reserva.
        """

        if self.buscar_reserva(codigo):

            raise ValueError(
                "Ya existe una reserva con ese código."
            )

        cliente = self._controlador_clientes.buscar_cliente(
            cedula_cliente
        )

        if cliente is None:

            raise ValueError(
                "Cliente no encontrado."
            )

        servicio = self._controlador_servicios.buscar_servicio(
            codigo_servicio
        )

        if servicio is None:

            raise ValueError(
                "Servicio no encontrado."
            )

        reserva = Reserva(
            codigo,
            cliente,
            servicio,
            fecha
        )

        self._reservas.append(
            reserva
        )

        self.guardar()

        Logger.registrar(
            "INFO",
            f"Reserva registrada: {codigo}"
        )

    def buscar_reserva(self, codigo):
        """
        Busca una reserva por su código.
        """

        for reserva in self._reservas:

            if reserva.codigo == codigo:

                return reserva

        return None

    def listar_reservas(self):
        """
        Devuelve todas las reservas.
        """

        return self._reservas

    def cancelar_reserva(self, codigo):
        """
        Cancela una reserva.
        """

        reserva = self.buscar_reserva(
            codigo
        )

        if reserva is None:

            raise ValueError(
                "Reserva no encontrada."
            )

        reserva.cancelar()

        self.guardar()

        Logger.registrar(
            "INFO",
            f"Reserva cancelada: {codigo}"
        )

    def eliminar_reserva(self, codigo):
        """
        Elimina una reserva.
        """

        reserva = self.buscar_reserva(
            codigo
        )

        if reserva is None:

            raise ValueError(
                "Reserva no encontrada."
            )

        self._reservas.remove(
            reserva
        )

        self.guardar()

        Logger.registrar(
            "INFO",
            f"Reserva eliminada: {codigo}"
        )