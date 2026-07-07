"""
controlador_clientes.py
=======================

Gestiona todas las operaciones relacionadas con los clientes.
"""

from config.configuracion import CLIENTES_FILE
from models.cliente import Cliente
from utils.almacenamiento import Almacenamiento
from utils.logger import Logger


class ControladorClientes:
    """
    Controlador encargado de administrar los clientes.
    """

    def __init__(self):
        """
        Inicializa el controlador cargando los clientes
        almacenados en el archivo JSON.
        """

        self._clientes = []

        self.cargar()

    def cargar(self):
        """
        Carga los clientes desde el archivo JSON.
        """

        datos = Almacenamiento.cargar_json(CLIENTES_FILE)

        self._clientes.clear()

        for cliente in datos:

            nuevo_cliente = Cliente(
                cliente["nombre"],
                cliente["telefono"],
                cliente["correo"],
                cliente["cedula"]
            )

            self._clientes.append(nuevo_cliente)

    def convertir_a_diccionario(self, cliente):
        """
        Convierte un objeto Cliente en un diccionario.
        """

        return {
            "nombre": cliente.nombre,
            "telefono": cliente.telefono,
            "correo": cliente.correo,
            "cedula": cliente.cedula
        }

    def guardar(self):
        """
        Guarda todos los clientes en el archivo JSON.
        """

        datos = []

        for cliente in self._clientes:

            datos.append(
                self.convertir_a_diccionario(cliente)
            )

        Almacenamiento.guardar_json(
            CLIENTES_FILE,
            datos
        )

    def registrar_cliente(
        self,
        nombre,
        telefono,
        correo,
        cedula
    ):
        """
        Registra un nuevo cliente.
        """

        if self.buscar_cliente(cedula) is not None:
            raise ValueError(
                "Ya existe un cliente con esa cédula."
            )

        cliente = Cliente(
            nombre,
            telefono,
            correo,
            cedula
        )

        self._clientes.append(cliente)

        self.guardar()

        Logger.registrar(
            "INFO",
            f"Cliente registrado: {cedula}"
        )

    def buscar_cliente(self, cedula):
        """
        Busca un cliente por su cédula.
        """

        for cliente in self._clientes:

            if cliente.cedula == cedula:

                return cliente

        return None

    def listar_clientes(self):
        """
        Devuelve la lista de clientes.
        """

        return self._clientes

    def actualizar_cliente(
        self,
        cedula,
        nombre,
        telefono,
        correo
    ):
        """
        Actualiza la información de un cliente.
        """

        cliente = self.buscar_cliente(cedula)

        if cliente is None:
            raise ValueError(
                "Cliente no encontrado."
            )

        cliente._nombre = nombre
        cliente._telefono = telefono
        cliente._correo = correo

        self.guardar()

        Logger.registrar(
            "INFO",
            f"Cliente actualizado: {cedula}"
        )

    def eliminar_cliente(self, cedula):
        """
        Elimina un cliente.
        """

        cliente = self.buscar_cliente(cedula)

        if cliente is None:
            raise ValueError(
                "Cliente no encontrado."
            )

        self._clientes.remove(cliente)

        self.guardar()

        Logger.registrar(
            "INFO",
            f"Cliente eliminado: {cedula}"
        )