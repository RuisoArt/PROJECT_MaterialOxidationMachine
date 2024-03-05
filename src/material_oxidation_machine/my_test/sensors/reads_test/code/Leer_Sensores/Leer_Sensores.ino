

// Variable para almacenar el valor obtenido del sensor (0 a 1023)
float tempCentigrados_1;
float tempCentigrados_2;
float tempCentigrados_3;
float tempCentigrados_4;
float tempCentigrados_5;
float tempCentigrados_6;
float tempCentigrados_7;
float tempCentigrados_8;

float myTempArrayLM35[8];

int pinLM35_1 = 0; // entrada temperatura 1(A0)
int pinLM35_2 = 1; // entrada temperatura 2(A1)
int pinLM35_3 = 2; // entrada temperatura 3(A2)
int pinLM35_4 = 3; // entrada temperatura 4(A3)
int pinLM35_5 = 4; // entrada temperatura 5(A4)
int pinLM35_6 = 5; // entrada temperatura 6(A5)
int pinLM35_7 = 6; // entrada temperatura 7(A6)
int pinLM35_8 = 7; // entrada temperatura 8(A7)

void initAnalogRead(){
  // Con analogRead leemos el sensor recuerda que es un valor de 0 a 1023
  tempCentigrados_1 = analogRead(pinLM35_1);
  tempCentigrados_2 = analogRead(pinLM35_2);
  tempCentigrados_3 = analogRead(pinLM35_3);
  tempCentigrados_4 = analogRead(pinLM35_4);
  tempCentigrados_5 = analogRead(pinLM35_5);
  tempCentigrados_6 = analogRead(pinLM35_6);
  tempCentigrados_7 = analogRead(pinLM35_7);
  tempCentigrados_8 = analogRead(pinLM35_8);
}

void mathLM35(){
  // Calculamos la temperatura con la fórmula
  tempCentigrados_1 = (5.0 * tempCentigrados_1 * 100.0)/1024.0;
  tempCentigrados_2 = (5.0 * tempCentigrados_2 * 100.0)/1024.0;
  tempCentigrados_3 = (5.0 * tempCentigrados_3 * 100.0)/1024.0;
  tempCentigrados_4 = (5.0 * tempCentigrados_4 * 100.0)/1024.0;
  tempCentigrados_5 = (5.0 * tempCentigrados_5 * 100.0)/1024.0;
  tempCentigrados_6 = (5.0 * tempCentigrados_6 * 100.0)/1024.0;
  tempCentigrados_7 = (5.0 * tempCentigrados_7 * 100.0)/1024.0;
  tempCentigrados_8 = (5.0 * tempCentigrados_8 * 100.0)/1024.0;

  myTempArrayLM35[0] = tempCentigrados_1;
  myTempArrayLM35[1] = tempCentigrados_2;
  myTempArrayLM35[2] = tempCentigrados_3;
  myTempArrayLM35[3] = tempCentigrados_4;
  myTempArrayLM35[4] = tempCentigrados_5;
  myTempArrayLM35[5] = tempCentigrados_6;
  myTempArrayLM35[6] = tempCentigrados_7;
  myTempArrayLM35[7] = tempCentigrados_8;
}

void SerialPrintData(){
  // Envia el dato al puerto serial
  for(int i=0; i<8 ;i++){
    Serial.print("Temp");
    Serial.print(i+1);
    Serial.print(": ");
    Serial.println(myTempArrayLM35[i]);
    delay(500);
  }
  Serial.println("_________________");
  

}

void setup() {
  // Configuramos el puerto serial a 9600 bps
  Serial.begin(9600);
 
}
 
void loop() {
  initAnalogRead();
  mathLM35();
  SerialPrintData();
}
