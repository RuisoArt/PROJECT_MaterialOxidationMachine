from Code.code_gpio import output_7_seven as seven

def STOP(sensor_4):
    var = str(sensor_4)

    if var == "0":
        print("Se acabo el agua cham0!")
        seven.output_off(7)
    else:
        print("siguele pues")