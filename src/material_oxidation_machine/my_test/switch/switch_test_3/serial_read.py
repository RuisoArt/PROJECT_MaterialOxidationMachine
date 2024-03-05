"""
lectura simple: https://putosistema.wordpress.com/2017/08/27/leer-puerto-serial/
comuniacion serial: https://programmerclick.com/article/42921672706/

pip install pyserial => windows so
"""

import serial
from time import sleep

# en windows se pregunta por com en linux por la ruta especifica del sistema

# windows:
ser = serial.Serial("COM5",115200)

try:
    #ser = serial.Serial("COM6",115200)
    ser.setDTR(False)
    sleep(1)
    ser.flushInput()
    ser.setDTR(True)

    while True:
        data = ser.readline()
        my_string = str(data)
        my_string = my_string.replace('b','')
        my_string = my_string.replace('r','')
        my_string = my_string.replace('n','')
        my_string = my_string.replace('str(\\)','')
        #my_string = data.decode('ascii')
        print(my_string)

except:
    print("Error")


ser.close()