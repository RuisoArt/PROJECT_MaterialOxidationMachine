import datetime as dt
from code_body import notices_control as ntc

def machine_on(window, hora, minute):
    date = dt.datetime.now()

    my_hora = int(hora)
    my_minute = int(minute)

    #primer caso tiempo hacia adelante, maximo por defecto dos dias entonces que se podria explotar el software
    while True:
        actual_hour = int( date.strftime("%H") )
        actual_minute = int( date.strftime("%M") )
        print("hora actual = "+str(actual_hour)+":"+str(actual_minute))

        if my_hora >= actual_hour:
            print("hora conseguida")
            if my_minute <= actual_minute:
                print("minuto conseguido")
                ntc.finich_process(window, "now")
                break
            elif my_minute > actual_minute:
                print("minuto menor al conseguir")
                
                
                break
            else:
                continue
        else:
            print("Hora aun no conseguida")


