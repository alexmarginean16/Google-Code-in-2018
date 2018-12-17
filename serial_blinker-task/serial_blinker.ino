String inp;

void setup()
{
pinMode(13, OUTPUT);

Serial.begin(9600);
Serial.println(" Type ON if you want to turn the LED on");
Serial.println(" Type OFF if you want to turn the LED off"); 
Serial.println(); 
}

void loop()
{
  while(Serial.available()) {
    inp = Serial.readString();
    
    if(inp == "ON")
    {
      digitalWrite(13,HIGH);
      Serial.print("LED ON");
    }
    
    if(inp == "OFF")
    {
      digitalWrite(13,LOW);
      Serial.print("LED OFF");
    }
    
    Serial.println();
  }
}
