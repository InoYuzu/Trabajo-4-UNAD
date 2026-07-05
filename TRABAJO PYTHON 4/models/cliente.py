"""
cliente.py
==========

Define la clase Cliente.
"""

from models.persona import Persona
from utils.validaciones import Validaciones


class Cliente(Persona):
    """
    Representa un cliente del sistema.
    """

    def __init__(self, nombre, telefono, correo, cedula):
        """
        Inicializa un cliente.
        """

        super().__init__(nombre, telefono, correo)

        if not Validaciones.validar_cedula(cedula):
            raise ValueError("La cédula solo puede contener números.")

        self._cedula = cedula

    @property
    def cedula(self):
        """
        Devuelve la cédula del cliente.
        """
        return self._cedula

    def __str__(self):
        """
        Devuelve la información del cliente.
        """

        return (
            f"{super().__str__()}\n"
            f"Cédula: {self.cedula}"
        )