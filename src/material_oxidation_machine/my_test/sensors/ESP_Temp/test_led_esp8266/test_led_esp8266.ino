// Instalacion de ESP8266 en Arduino IDE: https://randomnerdtutorials.com/how-to-install-esp8266-board-arduino-ide/

//Codigo de prueba de instalacion, encender un led externo, encender un pinen 1 logico
int pin = 2;

void setup() {
  // initialize GPIO 2 as an output.
  pinMode(pin, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(pin, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);               // wait for a second
  digitalWrite(pin, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);               // wait for a second
}
