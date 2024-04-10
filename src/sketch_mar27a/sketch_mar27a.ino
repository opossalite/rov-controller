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
const int PIN = 10;
bool buttonA_state = false;

void setup() {
  Serial.begin(9600);  // start serial communication at 9600 baud
  //pinMode(buttonPin, INPUT_PULLUP);    // Set the switch pin as input
  pinMode(PIN, OUTPUT);
  analogWrite(PIN, 128); //ensure we start at middle position

}
void loop() {
  //if (Serial.read() == 1) {
  //  buttonA_state = !buttonA_state;
  //  digitalWrite(PIN, buttonA_state);
  //}
  int thing = Serial.read();
  //Serial.println(thing);
  if (thing == -1) {
    return;
  }
  analogWrite(PIN, thing);

}

