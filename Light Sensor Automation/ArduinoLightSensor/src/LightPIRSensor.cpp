#include <Arduino.h>

const int pirPin = 2;        // PIR sensor pin
const int lightSensorPin = A0;  // Light sensor pin (Analog)
const int ledPin = 13;       // LED pin

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);        // Start serial communication for debugging
}

void loop() {
  int pirState = digitalRead(pirPin);  // Read PIR sensor
  int lightLevel = analogRead(lightSensorPin); // Read light sensor

  Serial.print("PIR: ");
  Serial.print(pirState);
  Serial.print(" Light: ");
  Serial.println(lightLevel);

  // Example logic: Turn on LED if PIR is triggered and it's dark
  if (pirState == HIGH && lightLevel < 500) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }

  delay(100);  // Delay to avoid bouncing
}
