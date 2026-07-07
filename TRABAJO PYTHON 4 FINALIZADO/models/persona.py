"""
persona.py
==========

Define la clase Persona, utilizada como clase base para
las personas registradas en el sistema.
"""

from utils.validaciones import Validaciones


class Persona:
    """
    Clase base para representar una persona.
    """

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
        """
        Devuelve una representación en texto del objeto.
        """

        return (
            f"Nombre: {self.nombre}\n"
            f"Teléfono: {self.telefono}\n"
            f"Correo: {self.correo}"
        )