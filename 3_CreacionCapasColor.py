from Library.TimeSleepPrint import time_sleep
from Library.coloreado import RiggingColoreado
from Library.create_color_cap import RiggingCrearCapaColor
from Puppet import puppet

if __name__ == '__main__':
    time_sleep(5)
    print("CREACION CAPA DE COLOR")
    rigging = RiggingCrearCapaColor(puppet)
    rigging.main()
    time_sleep(5)
    print("COLOREADO")
    rigging_1 = RiggingColoreado()
    rigging_1.main()
