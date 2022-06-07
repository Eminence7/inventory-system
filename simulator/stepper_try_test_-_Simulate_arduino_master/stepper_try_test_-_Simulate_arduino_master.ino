// Wire Master Writer

#include <Wire.h>
char c;
void setup() {
  Wire.begin(); // join i2c bus (address optional for master)
  Serial.begin(9600);
  
}

byte x = 100;


void loop() {

  while(Serial.available()>0){
  c=Serial.read();
  Wire.beginTransmission(8); // transmit to device #8
  //Wire.write("35,45");        // sends five bytes
  Wire.write(c);              // sends one byte
  Wire.endTransmission();    // stop transmitting
  }
  x;
  delay(500);
}
