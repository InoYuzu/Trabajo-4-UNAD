"""
generador_codigos.py
====================

Genera códigos únicos para los registros del sistema.
"""

from config.configuracion import (
    SERVICIOS_FILE,
    RESERVAS_FILE
)

from utils.almacenamiento import Almacenamiento


class GeneradorCodigos:
    """
    Genera códigos consecutivos para el sistema.
    """

    @staticmethod
    def _generar_codigo(archivo, prefijo):
        """
        Genera un código consecutivo.
        """

        datos = Almacenamiento.cargar_json(archivo)

        if not datos:
            return f"{prefijo}001"

        ultimo_codigo = datos[-1]["codigo"]

        numero = int(
            ultimo_codigo.replace(prefijo, "")
        )

        numero += 1

        return f"{prefijo}{numero:03d}"

    @staticmethod
    def generar_servicio():
        """
        Genera un código para un servicio.
        """

        return GeneradorCodigos._generar_codigo(
            SERVICIOS_FILE,
            "S"
        )

    @staticmethod
    def generar_reserva():
        """
        Genera un código para una reserva.
        """

        return GeneradorCodigos._generar_codigo(
            RESERVAS_FILE,
            "R"
        )