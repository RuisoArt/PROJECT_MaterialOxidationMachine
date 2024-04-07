#pip install pyserial
import serial

import init_text as pr
#from Code.code_gpio import output_7_seven as seven
#import emergency_stop as warning

#Comando Linux para determinar el nombre de dispositivo serial:
# dmesg | grep -v disconnect | grep -Eo "tty(ACM|USB)." | tail -1
#aparecera algo como ttyACM0
#aparecera ttyUSB0

while True:
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    #ser = serial.Serial() #tasa de transferencia de 9600 baudios
    ser.flushInput() #limpia datos del buffer de entrada antes de leer algun dato
    try:
        lineBytes = ser.readline()
        line = lineBytes.decode('utf-8').strip()
        print("se recibio: "+line)
        trama_datos = line.split(";")
        print("La trama de datos es: "+str(trama_datos))
        sensor_1 = str(trama_datos[1])
        sensor_2 = str(trama_datos[2])
        sensor_3 = str(trama_datos[3])
        sensor_4 = str(trama_datos[4])
        print("sensor 1: "+sensor_1)
        print("sensor 2: "+sensor_2)
        print("sensor 3: "+sensor_3)
        print("sensor 4: "+sensor_4)
        
        pr.init_register(sensor_1, sensor_2, sensor_3, sensor_4)
        #warning.STOP(sensor_4)        

    except KeyboardInterrupt:
        break

