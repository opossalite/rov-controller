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
  //int thing = Serial.read();
  //Serial.println(thing);
  //if (thing == -1) {
  //  return;
  //}
  //analogWrite(PIN, thing);

  if (Serial.available() > 0) {
    
  }
}

