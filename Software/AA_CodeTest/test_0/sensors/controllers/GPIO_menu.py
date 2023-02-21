import time
import sensors.controllers.GPIO_behaviour as task

class GPIO_menu():
    def gpio_menu_switch():
        task.GPIO_behaviour.security_init_pin()

        estado = int(input("cuantas veces que se encienda el pin: "))
        for i in range(estado):
            task.GPIO_behaviour.encender_pin_15()
            time.sleep(5)
            task.GPIO_behaviour.apagar_pin_15()
            time.sleep(5)