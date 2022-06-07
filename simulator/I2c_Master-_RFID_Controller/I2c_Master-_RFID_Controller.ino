/*/ Wire Master Writer

#include <Wire.h>
char c;
void setup() {
  Wire.begin(); // join i2c bus (address optional for master)
  Serial.begin(9600);
  
}

byte x = 0;


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
*/
// Wire Master Writer
#include <SoftwareSerial.h>
SoftwareSerial SoftSerial(2, 3);//rx,tx
#include <Wire.h>
char c;
int count = 0;

String id;
void setup() {
  Wire.begin(); // join i2c bus (address optional for master)
  Serial.begin(9600);
  SoftSerial.begin(9600);
  
}
byte x = 100;
void loop() {
    /*Wire.write("35,45");
    while(Serial.available()>0)
  {
    c = Serial.read();
   count++;
   id += c;
   if(count == 12)  
    {
      Serial.print(id);
      //break;
          
    }
  }
  count = 0;
  id="";
  delay(500);
  */
  while(SoftSerial.available()>0){
  c=SoftSerial.read();
  Wire.beginTransmission(8); // transmit to device #8
  //Wire.write("35,45");        // sends five bytes
  Wire.write(c);              // sends one byte
  Wire.endTransmission();    // stop transmitting
  }
   x;
  delay(500);
}
