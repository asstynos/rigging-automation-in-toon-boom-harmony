import pyautogui

from Library.constants import application_properties, deformador_puntos_properties, coordenadas_color_properties
from Properties.properties_managment import Properties
from Puppet import puppet


def agregar_linea_al_final(file, argumento, input_file, value):
    with open(file, 'a') as archivo:
        archivo.write(f"{argumento}{input_file} = {value}" + '\n')


class Deformacion:
    def __init__(self):
        self.properties = Properties(application_properties)
        self.puppet = puppet
        self.deformacion_enter = eval(self.properties.get_property_value(
            "deformacion.boton.enter"))
        self.deformacion_input = eval(self.properties.get_property_value(
            "deformacion.boton.input"))
        self.click_pantalla = (60, 124)

    def main(self):
        properties_deformador = Properties(deformador_puntos_properties)
        for sublist in self.puppet:
            for item in sublist:
                print(item)
                pyautogui.click(self.deformacion_input[0], self.deformacion_input[1])
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.hotkey(properties_deformador.get_property_value(f"deformador.nodes.{item}"))
                pyautogui.click(self.deformacion_enter[0], self.deformacion_enter[1])
                pyautogui.click(self.click_pantalla[0], self.click_pantalla[1])
                pyautogui.hotkey('j')

    @staticmethod
    def click_color(name):
        properties_color = Properties(coordenadas_color_properties)
        properties_value = f"automatizacion.color.{name}"
        coordenada = eval(properties_color.get_property_value(properties_value))
        pyautogui.click(coordenada[0], coordenada[1])
