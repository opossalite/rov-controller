String ser_data;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Arduino is ready");
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() > 0){
    char rec = Serial.read();
    ser_data += rec;

    if(rec == '\n'){
      Serial.print("Message received: ");
      Serial.println(ser_data);
      ser_data = "";
    }
  }
  delay(10);
}
