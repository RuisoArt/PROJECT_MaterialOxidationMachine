//codigo de lectura y paso de lecturas por serial a raspberry pi
//las lecturas estaran sometidas a la defincion de lectura de los pines
//En caso de lectura de pines analogicos tiene una resolucion del ADC de:
//  10bit = 0 -> 1023 = 0v -> 5v
#include <Arduino.h>
#include <OneWire.h>
#include <DallasTemperature.h>

String sensor_01;
String sensor_02;
String sensor_03;
String sensor_04;
String mensaje;

// lectura digital DS18B20
//const int dataPinDQ = 12; //D12
OneWire onewire(2);
DallasTemperature sensorDS18B20(&onewire);

// LM35
float value_tempLM35_01;
int analogPin = A7; 

// intrruptor
int nivelPin = A0;
int my_var = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(nivelPin, INPUT);
  pinMode (analogPin,INPUT); //configurar el pin de lectura analogico como entrada
  Serial.begin(9600);//9600 baudios
  sensorDS18B20.begin(); //inicializa el bus de datos 1-Wire
}

void loop() {
  my_var = digitalRead(nivelPin);
  // Mandamos comandos para toma de temperatura a los sensores
  //Serial.println("Mandando comandos a los sensores");
  sensorDS18B20.requestTemperatures();

  // Caculo del sensor analogo
  value_tempLM35_01 = analogRead(analogPin);
  value_tempLM35_01 = (5.0 * value_tempLM35_01 * 100.0)/1024.0;
  
  // Impresion serial sensor DS18B20 01
  //Serial.print("Sensor Digital DS18B20 1: ");
  //Serial.print(sensorDS18B20.getTempCByIndex(0));
  //Serial.println(" °C");
  //Serial.print("\n");
  sensor_01 = sensorDS18B20.getTempCByIndex(0);

  // Impresion serial sensor DS18B20 02
  //Serial.print("Sensor Digital DS18B20 2: ");
  //Serial.print(sensorDS18B20.getTempCByIndex(1));
  //Serial.println(" °C");
  //Serial.print("\n");
  sensor_02 = sensorDS18B20.getTempCByIndex(1);

  // Impresion seria Lm35
  //Serial.print("Sensor Analogico LM35: ");
  //Serial.print(value_tempLM35_01);
  //Serial.println(" °C");
  //Serial.print("\n");
  sensor_03 = value_tempLM35_01;

  // Impresion de Nivel
  //configuracion pullup
  if(my_var == LOW){
    sensor_04 = "1";
  }else{
    sensor_04 = "0";
  }
  
  // impresion total
  mensaje = (+";"+sensor_01+";"+sensor_02+";"+sensor_03+";"+sensor_04);
  Serial.print(mensaje);
  Serial.print("\n");


  //tiempo de espera
  delay(1000); //500ms
}