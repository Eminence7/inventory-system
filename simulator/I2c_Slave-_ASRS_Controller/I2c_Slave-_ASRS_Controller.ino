// Wire Slave Receiver

#include <Wire.h>
#include <Stepper.h>

const int stepsPerRevolution=200;
Stepper stepper_X_axis (stepsPerRevolution,8,9,10,11);
int motSpeed=10;
int StepsPerMillimeterX = 5.0;
int Loc_int;



void setup() {
  stepper_X_axis.setSpeed(motSpeed);
  
  //Wire.begin(8);                // join i2c bus with address #8
  //Wire.onReceive(receiveEvent); // register event
  //Serial.begin(9600);           // start serial for output
  }

void loop() {
  stepper_X_axis.step(stepsPerRevolution);
  //delay(100);
  
}

// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany) {
      //while (1 < Wire.available()) { // loop through all but the last
      //char c = Wire.read(); // receive byte as a character
      //Serial.print(c);         // print the character
      // }
  while (Wire.available()){
  char x = Wire.read();    // receive byte as an integer
  Serial.println(x);         // print the integer
  int Loc_Int =x ;
  Serial.println(Loc_Int);
  stepper_X_axis.step(stepsPerRevolution);
  }
  delay(500);
}
