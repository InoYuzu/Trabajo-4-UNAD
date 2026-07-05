"""
controlador_servicios.py
========================

Gestiona todas las operaciones relacionadas con los servicios.
"""

from config.configuracion import SERVICIOS_FILE
from models.servicio import Servicio
from utils.almacenamiento import Almacenamiento
from utils.logger import Logger


class ControladorServicios:
    """
    Controlador encargado de administrar los servicios.
    """

    def __init__(self):
        """
        Inicializa el controlador cargando los servicios
        almacenados en el archivo JSON.
        """

        self._servicios = []

        self.cargar()

    def cargar(self):
        """
        Carga los servicios desde el archivo JSON.
        """

        datos = Almacenamiento.cargar_json(SERVICIOS_FILE)

        self._servicios.clear()

        for servicio in datos:

            nuevo_servicio = Servicio(
                servicio["codigo"],
                servicio["nombre"],
                servicio["precio"],
                servicio["duracion"]
            )

            self._servicios.append(nuevo_servicio)

    def convertir_a_diccionario(self, servicio):
        """
        Convierte un objeto Servicio en un diccionario.
        """

        return {
            "codigo": servicio.codigo,
            "nombre": servicio.nombre,
            "precio": servicio.precio,
            "duracion": servicio.duracion
        }

    def guardar(self):
        """
        Guarda todos los servicios en el archivo JSON.
        """

        datos = []

        for servicio in self._servicios:

            datos.append(
                self.convertir_a_diccionario(servicio)
            )

        Almacenamiento.guardar_json(
            SERVICIOS_FILE,
            datos
        )

    def registrar_servicio(
        self,
        codigo,
        nombre,
        precio,
        duracion
    ):
        """
        Registra un nuevo servicio.
        """

        if self.buscar_servicio(codigo) is not None:
            raise ValueError(
                "Ya existe un servicio con ese código."
            )

        servicio = Servicio(
            codigo,
            nombre,
            precio,
            duracion
        )

        self._servicios.append(servicio)

        self.guardar()

        Logger.registrar(
            "INFO",
            f"Servicio registrado: {codigo}"
        )

    def buscar_servicio(self, codigo):
        """
        Busca un servicio por su código.
        """

        for servicio in self._servicios:

            if servicio.codigo == codigo:

                return servicio

        return None

    def listar_servicios(self):
        """
        Devuelve la lista de servicios.
        """

        return self._servicios

    def actualizar_servicio(
        self,
        codigo,
        nombre,
        precio,
        duracion
    ):
        """
        Actualiza la información de un servicio.
        """

        servicio = self.buscar_servicio(codigo)

        if servicio is None:
            raise ValueError(
                "Servicio no encontrado."
            )

        servicio._nombre = nombre
        servicio._precio = precio
        servicio._duracion = duracion

        self.guardar()

        Logger.registrar(
            "INFO",
            f"Servicio actualizado: {codigo}"
        )

    def eliminar_servicio(self, codigo):
        """
        Elimina un servicio.
        """

        servicio = self.buscar_servicio(codigo)

        if servicio is None:
            raise ValueError(
                "Servicio no encontrado."
            )

        self._servicios.remove(servicio)

        self.guardar()

        Logger.registrar(
            "INFO",
            f"Servicio eliminado: {codigo}"
        )