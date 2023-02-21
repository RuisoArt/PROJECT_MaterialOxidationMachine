import time

import sensors.models.PIN_GPIO
import sensors.controllers.GPIO_behaviour
import sensors.controllers.GPIO_menu
import sensors.views.menu_principal as vari 

if __name__ == '__main__':
    vari.menu_principal.run_processes()