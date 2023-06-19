import pyautogui

from Rigging.Library.constants import coordenadas_color_properties, application_properties, puppet_color
from Rigging.Properties.properties_managment import Properties
from Rigging.Puppet import puppet


class RiggingColoreado:
    def __init__(self):
        self.properties = Properties(application_properties)
        self.puppet = puppet
        self.primer_capa = eval(self.properties.get_property_value(
            "automatizacion.primer.capa"))
        self.capa_color = eval(self.properties.get_property_value(
            "automatizacion.bote.vista.capa.color"))
        self.pintura = eval(self.properties.get_property_value(
            "automatizacion.bote.pintura"))
        self.superior_izquierdo = eval(self.properties.get_property_value(
            "automatizacion.superior.izquierdo"))
        self.inferior_izquierdo = eval(self.properties.get_property_value(
            "automatizacion.inferior.izquierdo"))
        self.inferior_derecho = eval(self.properties.get_property_value(
            "automatizacion.inferior.derecho"))
        self.superior_derecho = eval(self.properties.get_property_value(
            "automatizacion.superior.derecho"))

    def seleccion(self):
        pyautogui.moveTo(self.superior_izquierdo[0], self.superior_izquierdo[1])
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(self.superior_derecho[0], self.superior_derecho[1], duration=0.4)
        pyautogui.moveTo(self.inferior_derecho[0], self.inferior_derecho[1], duration=0.4)
        pyautogui.moveTo(self.inferior_izquierdo[0], self.inferior_izquierdo[1], duration=0.4)
        pyautogui.moveTo(self.superior_izquierdo[0], self.superior_izquierdo[1], duration=0.4)
        pyautogui.mouseUp(button='left')

    def main(self):
        pyautogui.click(self.capa_color[0], self.capa_color[1])
        pyautogui.click(self.pintura[0], self.pintura[1])
        for sublist in self.puppet:
            for item in sublist:
                print(item)
                self.click_color(item)
                self.seleccion()
                pyautogui.hotkey('j')

    @staticmethod
    def click_color(name):
        properties_color = Properties(puppet_color)
        properties_value = f"puppet.color.{name}"
        valor = properties_color.get_property_value(properties_value)
        properties_color = Properties(coordenadas_color_properties)
        coordenada = eval(properties_color.get_property_value(valor))
        pyautogui.click(coordenada[0], coordenada[1])
