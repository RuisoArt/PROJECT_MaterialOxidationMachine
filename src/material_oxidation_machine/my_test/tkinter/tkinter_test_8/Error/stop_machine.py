from ..Code.code_gpio import output_7_seven as off

def emergency_stop(sensor4):
    if sensor4 == "0":
        print("La maquina debe apagarse")
        off.output_off(7)
    else:
        print("Sigue la maquina encendida")
    
