#include<ESP8266WiFi.h>
int led = 9;
int brightness = 1;
int fadevalue = 1;

void setup() {
  pinMode(13,OUTPUT);
  Serial.begin(9600);
}

void loop() {
    analogWrite(led, brightness);
    Serial.print(brightness);
    Serial.print("\n");
    brightness += fadevalue;
    if(brightness >= 255 || brightness <= 0)
    {
      fadevalue = -fadevalue;
    }
    delay(10);
}
