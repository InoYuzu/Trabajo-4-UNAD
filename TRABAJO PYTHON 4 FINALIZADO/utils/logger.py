"""
logger.py
=========

Gestiona el registro de eventos del sistema.
"""

#Importamos la libreria datatime para almacenar los errores con fecha y hora
from datetime import datetime
from config.configuracion import LOG_FILE



class Logger:
    """
    Registra eventos y errores del sistema.
    """

    @staticmethod
    def registrar(tipo, mensaje):
        """
        Escribe un evento en el archivo de logs.

        Parameters
        ----------
        tipo : str
            Tipo de evento (INFO, ERROR, WARNING).

        mensaje : str
            Descripción del evento.
        """

        #Aca tomamos la fecha del instante cuando se produsca el evento, en un formato personalizado
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a", encoding="utf-8") as archivo:

            archivo.write(
                f"[{fecha}] [{tipo}] {mensaje}\n"
            )