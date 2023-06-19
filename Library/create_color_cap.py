import pyautogui

from Library.constants import application_properties
from Properties.properties_managment import Properties


class RiggingCrearCapaColor:
    def __init__(self, puppet_master):
        self.properties = Properties(application_properties)
        self.puppet = puppet_master
        self.primer_capa = eval(self.properties.get_property_value(
            "automatizacion.primer.capa"))
        self.crear_capa_de_color = eval(self.properties.get_property_value(
            "rigging.crear_capa_de_color"))

    def count_sub_values_puppet(self):
        total_quantity = 0
        for sublist in self.puppet:
            amount_sub_values = len(sublist)
            total_quantity += amount_sub_values
        return total_quantity

    def main(self):
        count = self.count_sub_values_puppet()
        print("Capas existentes: ", count)
        for i in range(count):
            pyautogui.click(self.crear_capa_de_color[0], self.crear_capa_de_color[1])
            pyautogui.hotkey('j')
            print("completado ", i, "/", count)
