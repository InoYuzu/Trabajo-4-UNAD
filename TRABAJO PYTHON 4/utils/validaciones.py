"""
validaciones.py
===============

Contiene funciones para validar los datos ingresados
por el usuario.
"""

#Importamos re que sirve basicamente para configurar patrones a verificar
import re

from utils.excepciones import (
    CorreoInvalidoError,
    TelefonoInvalidoError
)

class Validaciones:
    """
    Agrupa los métodos de validación del sistema.
    """
    @staticmethod
    def campo_vacio(texto):
        """
        Retorna True si el texto está vacío.
        """
        return texto.strip() == ""
    
    @staticmethod
    def validar_telefono(telefono):
        """
        Verifica que el teléfono tenga exactamente
        diez dígitos.
        """
        patron = r"^\d{10}$"

        if not re.fullmatch(patron, telefono):

            raise TelefonoInvalidoError(
                "El teléfono debe contener exactamente 10 dígitos."
            )
        return True

    @staticmethod
    def validar_correo(correo):
        """
        Verifica el formato del correo electrónico.
        """
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.fullmatch(patron, correo):
            raise CorreoInvalidoError(
                "El correo electrónico no tiene un formato válido."
            )
        return True
    
    @staticmethod
    def validar_cedula(cedula):
        """
        Verifica que la cédula solo contenga números.
        """
        return cedula.isdigit()