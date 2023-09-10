int sensorPin = A0;  // select the input pin for the potentiometer
int sensorValue;
char userInput;


void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {

    userInput = Serial.read();
      
    if(userInput == 'g'){
      sensorValue = analogRead(sensorPin);
      Serial.println(sensorValue);
    }
  }
}
