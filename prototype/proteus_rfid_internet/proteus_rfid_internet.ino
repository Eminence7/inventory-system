int count = 0;
char c;
String id;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  //Serial.println("Please scan your RFID TAG");
}
void loop() {
  while(Serial.available()>0)
  {
    c = Serial.read();
   count++;
   id += c;
   if(count == 12)  
    {
      Serial.print(id);
      //break;
     
      if(id=="AB123456789A")
      {
        Serial.println("Valid TAG");
       }
      else
      {
       Serial.println("Invalid TAG");
      }
    }
  }
  count = 0;
  id="";
  delay(500);

}
