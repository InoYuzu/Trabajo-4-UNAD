"""
excepciones.py
==============

Contiene todas las excepciones que podrian ocurrir en el sistema
Este manejo permitira identificar mas facilmente donde se encuentran los errores en el sistema

Autor: Jhohan Sebastian Ibarra Sánchez
Curso: Programación
Proyecto: Sistema Integral
"""

class SistemaError(Exception):
    """
    Excepción base del sistema.
    """

    def __init__(self, mensaje, operacion=None):
        """
        Inicializa la excepción.

        Parameters
        ----------
        mensaje : str
            Descripción del error.

        operacion : str, optional
            Operación donde ocurrió el error.
        """

        self.mensaje = mensaje
        self.operacion = operacion

        super().__init__(mensaje)

#----------------------------------------
#Cliente
#----------------------------------------

class ClienteError(SistemaError):
    """
    Excepción para todos los errores.
    relacionados con clientes
    """
    pass

class ClienteDuplicadoError(ClienteError):
    """
    Se produce cuando se intenta registrar
    un cliente cuya cedula ya existe
    """
    pass

class CorreoInvalidoError(ClienteError):
    """
    Se produce cuando el correo tiene
    un formato invalido
    """
    pass

class TelefonoInvalidoError(ClienteError):
    """
    Se produce cuando el telefono
    contiene caracteres invalidos
    """
    pass


#----------------------------------------
#Servicio
#----------------------------------------
class ServicioError(SistemaError):
    """
    Excepción base para los servicios.
    """
    pass

class ServicioNoDisponibleError(ServicioError):
    """
    El servicio solicitado
    no se encuentra disponible.
    """
    pass


#----------------------------------------
#Reserva
#----------------------------------------
class ReservaError(SistemaError):
    """
    Excepción base para las reservas.
    """
    pass

class DuracionInvalidaError(ReservaError):
    """
    La duración ingresada
    no es válida.
    """
    pass

class ReservaCanceladaError(ReservaError):
    """
    La reserva ya fue cancelada.
    """
    pass

