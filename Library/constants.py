import os

path = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "Properties")

application_properties = fr'{path}\application.properties'
deformador_puntos_properties = fr'{path}\variables\deformadores.properties'
coordenadas_color_properties = fr'{path}\variables\color_coordenadas.properties'
puppet_color = fr'{path}\variables\asignacion_puppet_color.properties'


def validar_ruta(ruta):
    if os.path.exists(ruta):
        print(f"La ruta '{ruta}' existe.")
    else:
        print(f"La ruta '{ruta}' no existe.")


validar_ruta(application_properties)
validar_ruta(deformador_puntos_properties)
validar_ruta(coordenadas_color_properties)
