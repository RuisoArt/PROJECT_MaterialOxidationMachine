import time
import sensors.controllers.GPIO_menu as gpio_menu

class menu_principal():
    def run_processes():
        estado = True

        while(estado):
            print("Para iniciar el proceso o cerrar este programa seleccione una opcion del menu")
            print("")
            print("[1] Iniciar conmutacion basica")
            print("[2] Finalizar programa")
            print("")
            teclado = int(input("Escribe aqui tu seleccion: "))

            if teclado == 1:
                gpio_menu.GPIO_menu.gpio_menu_switch()
            
            elif teclado == 2:
                estado = False

            else:
                print("tecla incorrecta")