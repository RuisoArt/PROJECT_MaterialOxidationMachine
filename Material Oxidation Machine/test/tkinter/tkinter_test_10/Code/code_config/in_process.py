import datetime as dt
from code_body import notices_control as ntc

def machine_on(window, hora, minute):
    

    my_hora = int(hora)
    my_minute = int(minute)

    #primer caso tiempo hacia adelante, maximo por defecto dos dias entonces que se podria explotar el software
    
    #ciclo para la hora
    while True:
        date = dt.datetime.now()
        actual_hour = int( date.strftime("%H") )

        if actual_hour < my_hora:
            print("No apagar, no es la hora")
        elif actual_hour == my_hora:
            print("Apagar, ya es la hora")
            break
        elif actual_hour > my_hora:
            print("Apagar, ya se paso de la hora")
            break
        else:
            print("algo paso en el ciclo de la hora")
    
    #ciclo del minuto
    while True:
        date = dt.datetime.now()
        actual_minute = int( date.strftime("%M") )
        #print("hora actual = "+str(actual_hour)+":"+str(actual_minute))
        if actual_minute < my_minute:
            print("No apagar, aun no es el minuto, estoy en: "+str(actual_minute)+" y le dije: "+ str(my_minute))
        elif actual_minute == my_minute:
            print("Apagar, ya es el minuto")
            ntc.finich_process(window, "now")
            break
        elif actual_minute > my_minute:
            print("Apagar, ya se paso del minuto")
            ntc.finich_process(window, "now")
            break
        else:
            print("algo paso en el ciclo del minuto")
    

    


