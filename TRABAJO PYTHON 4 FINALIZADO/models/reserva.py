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