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