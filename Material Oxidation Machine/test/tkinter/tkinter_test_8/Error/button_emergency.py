#pip install pyserial
import serial
import stop_machine as emergency

while True:
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    ser.flushInput()
    try:
        lineBytes = ser.readline()
        line = lineBytes.decode('utf-8').strip()
        print("se recibio: "+line)
        trama_datos = line.split(";")
        print("La trama de datos es: "+str(trama_datos))
        sensor_4 = str(trama_datos[4])
        print("sensor 4: "+sensor_4)
        emergency.emergency_stop(sensor_4)
        
    except KeyboardInterrupt:
        break

