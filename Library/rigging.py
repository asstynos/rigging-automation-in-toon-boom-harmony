import pyautogui
from pynput.keyboard import Key, Controller

from Library.constants import application_properties, puppet_color, deformador_puntos_properties
from Library.deformacion import agregar_linea_al_final
from Properties.properties_managment import Properties


def mover_izquierda():
    pyautogui.click(70, 126)
    pyautogui.hotkey('ctrl', 'a')
    keyboard = Controller()
    keyboard.press(Key.shift)
    for _ in range(3):
        keyboard.press(Key.left)
        keyboard.release(Key.left)
    keyboard.release(Key.shift)


class Rigging:
    def __init__(self, puppet_master):
        self.space = 900
        self.space_drawing = 10
        self.properties = Properties(application_properties)
        self.alinear_nodos_horizontalmente = eval(
            self.properties.get_property_value("rigging.alinear_nodos_horizontalmente"))
        self.seleccion_para_agrupar_superior_izquierdo = eval(self.properties.get_property_value(
            "rigging.seleccion_para_agrupar_superior_izquierdo"))
        self.seleccion_para_agrupar_superior_derecho = eval(self.properties.get_property_value(
            "rigging.seleccion_para_agrupar_superior_derecho"))
        self.esquina_inferior_derecho = eval(self.properties.get_property_value(
            "rigging.esquina_inferior_derecho"))
        self.puppet = puppet_master

    def moverse_para_un_costado(self):
        spacing = 1
        for _ in range(spacing):
            pyautogui.moveTo(self.esquina_inferior_derecho[0],
                             self.esquina_inferior_derecho[1])
            pyautogui.keyDown('space')
            pyautogui.mouseDown(button='left')
            pyautogui.move(-1 * self.space, 0, duration=1)
            pyautogui.mouseUp(button='left')
            pyautogui.keyUp('space')

    def crear_composite(self):
        pyautogui.moveTo(self.seleccion_para_agrupar_superior_izquierdo[0],
                         self.seleccion_para_agrupar_superior_izquierdo[1])
        pyautogui.mouseDown()
        pyautogui.moveTo(self.seleccion_para_agrupar_superior_derecho[0],
                         self.seleccion_para_agrupar_superior_derecho[1], duration=1)
        pyautogui.dragTo(self.seleccion_para_agrupar_superior_derecho[0],
                         self.seleccion_para_agrupar_superior_derecho[1], button='left')
        pyautogui.mouseUp()
        pyautogui.hotkey('ctrl', 'h')
        self.moverse_para_un_costado()

    def main(self):
        i = 0
        h = 0
        count = len(self.puppet)
        for sublist in self.puppet:
            h += 1
            print(h, "/", count)
            for item in sublist:
                pyautogui.hotkey('ctrl', 'r')
                pyautogui.write(item)
                agregar_linea_al_final(puppet_color, "puppet.color.", item, "automatizacion.color.")
                agregar_linea_al_final(deformador_puntos_properties, "deformador.nodes.", item, "4")
                pyautogui.hotkey('enter')
                pyautogui.hotkey('escape')
                pyautogui.hotkey('ctrl', 'p')
                pyautogui.hotkey('escape')
                mover_izquierda()
            pyautogui.hotkey('escape')
            self.crear_composite()
            i += 1
