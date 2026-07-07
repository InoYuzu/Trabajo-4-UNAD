"""
main.py
=======

Punto de entrada del sistema.
"""

from config.configuracion import preparar_entorno

from controllers.controlador_clientes import ControladorClientes
from controllers.controlador_servicios import ControladorServicios
from controllers.Controlador_Reservas import ControladorReservas

from views.ventana_principal import VentanaPrincipal


def main():
    """
    Inicializa el sistema y abre la interfaz gráfica.
    """

    # Preparar carpetas y archivos necesarios
    preparar_entorno()

    # Crear controladores
    controlador_clientes = ControladorClientes()
    controlador_servicios = ControladorServicios()
    controlador_reservas = ControladorReservas(
        controlador_clientes,
        controlador_servicios
    )

    # Abrir interfaz
    app = VentanaPrincipal(
        controlador_clientes,
        controlador_servicios,
        controlador_reservas
    )

    app.mainloop()


if __name__ == "__main__":
    main()