#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <SPI.h>
#include <SparkFun_ADXL345.h>

//Crear el objeto lcd  dirección  0x3F y 16 columnas x 2 filas
LiquidCrystal_I2C lcd(0x27,20,4);
//Crear Objeto acelerometro
ADXL345 adxl = ADXL345();
///// POTENCIOMETRO
 #define salidaA 2
 #define salidaB 3
 #define boton 4
 int contador = 0; 
 int estadoA;
 int estadoPrevioA;  
////// ACELEROMETRO
 int x, y, z;
 void setup() {
  //POTENCIOMETRO 
   pinMode (salidaA,INPUT); // pin 2 
   pinMode (salidaB,INPUT); // pin 3
   // el pulsador debe ser polarizado a valor ALTO
   pinMode (boton, INPUT_PULLUP);
      Serial.begin (9600);
   // Lee el estado inicial de la salida A
   estadoPrevioA = digitalRead(salidaA);   
  /////////////LCD
    // Inicializar el LCD
    lcd.init();
    //Encender la luz de fondo.
    lcd.backlight();
    // Escribimos el Mensaje en el LCD.
    lcd.print("Hola Mundo");
  /////////////
  ////////////ACELEROMETRO
   adxl.powerOn();           
   adxl.setRangeSetting(16);       //Definir el rango, valores 2, 4, 8 o 16
   
}

void loop() {
//leer los valores e imprimirlos
  adxl.readAccel(&x, &y, &z); 
//Codigo potenciometro
  // Lee el estado de la salida A
   estadoA = digitalRead(salidaA);
   // Si el estado previo de la salida A era otro
   // significa que se ha producido un pulso
   if (estadoA != estadoPrevioA){     
     // Si el estado de salida B es diferente del estado
     // de salida A el codificador esta girando a la derecha
     if (digitalRead(salidaB) != estadoA) { 
       contador ++;
       lcd.clear();
     } else {
       contador --;
       lcd.clear();
     }
     /*Serial.print("Posición: ");
     Serial.println(contador);
     Serial.print("angulo: ");    
     Serial.println(contador*180/20);*/
     //////////
     lcd.setCursor(0, 1);
     // Escribimos el número de segundos trascurridos
     lcd.print(contador*180/20);
     //lcd.createChar(0, customChar);
     lcd.home();
     lcd.print(x);
     lcd.print(" X ");
     lcd.print(y);
     lcd.print(" Y ");
     lcd.print(z);
     lcd.print(" Z ");
     lcd.setCursor(3, 1);
     lcd.write(0);
     ////////
   } 
   // actualiza el estado guardado
   estadoPrevioA = estadoA;
 
  bool Bot = digitalRead(boton);
  //Serial.print(B);
   if (!Bot) // si se pulsa el boton su valor va a BAJO
    { Serial.println("Boton pulsado: Contador a 0");
      contador = 0 ;
      delay(300);
    }
}
