from pynput import mouse

from Library.constants import coordenadas_color_properties
from Properties.properties_managment import Properties
from Puppet import colores


def get_next_item():
    for sublist in colores:
        yield sublist


item_generator = get_next_item()


def on_click(x, y, button, pressed):
    if pressed:
        try:
            item = next(item_generator)
            properties = Properties(coordenadas_color_properties)
            properties.update_property_value(f"automatizacion.color.{item}", (x, y))
            print(f"automatizacion.color.{item} = {properties.get_property_value(f'automatizacion.color.{item}')}")
        except StopIteration:
            print("Se procesaron todos los elementos de la lista")
            return False


def on_release(x, y, button):
    print(f"Se soltó el clic en las coordenadas ({x}, {y})")
    return False


def get_mouse_coordinates_crear_properties():
    print(colores)
    with mouse.Listener(on_click=on_click, on_release=on_release) as listener:
        listener.join()
