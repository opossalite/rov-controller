// USB - USB.ino
//
// Description:
// Executes commands retrieved from serial (USB) port.
//
// Created by John Woolsey on 12/17/2019.
// Copyright (c) 2019 Woolsey Workshop.  All rights reserved.
//bool buttonState = 0;       // variable to hold the button state
//bool Mode = 0;
//bool currentvalue = 0;
bool buttonA_state = false;

void setup() {
  Serial.begin(9600);  // start serial communication at 9600 baud
  //pinMode(buttonPin, INPUT_PULLUP);    // Set the switch pin as input
  pinMode(LED_BUILTIN, OUTPUT);

}
void loop()
{
  if (Serial.read() == 1) {
    //currentvalue = !currentvalue;
    //digitalWrite(LED_BUILTIN, currentvalue);
  //digitalWrite(LED_BUILTIN, HIGH);
  //delay(1000);
    buttonA_state = !buttonA_state;
    digitalWrite(LED_BUILTIN, buttonA_state);
    //if (buttonA_state) {
    //  digitalWrite(LED_BUILTIN, HIGH);
    //} else {
    //  digitalWrite(LED_BUILTIN, LOW);
    //}
  }
  
  //digitalWrite(LED_BUILTIN, HIGH);
  //delay(500);
  //digitalWrite(LED_BUILTIN, LOW);
  //delay(500);

} 
    
    
    
    //if (Serial.read() != currentvalue){
      //digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
      //delay(500);
     // }
  //  } 
//}
