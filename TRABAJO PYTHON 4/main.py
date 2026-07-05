"""
main.py
=======

Punto de entrada del sistema.
"""

from controllers.controlador_clientes import (
    ControladorClientes
)

from controllers.controlador_servicios import (
    ControladorServicios
)

from controllers.Controlador_Reservas import (
    ControladorReservas
)


def main():
    """
    Inicializa todos los controladores.
    """

    controlador_clientes = ControladorClientes()

    controlador_servicios = ControladorServicios()

    controlador_reservas = ControladorReservas(
        controlador_clientes,
        controlador_servicios
    )

    print("Sistema inicializado correctamente.")

    return (
        controlador_clientes,
        controlador_servicios,
        controlador_reservas
    )


if __name__ == "__main__":
    main()