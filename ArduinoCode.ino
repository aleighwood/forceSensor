// initalise variables
int sensorPin = A0;  
int sensorValue;
char userInput;


void setup() {
  Serial.begin(9600); // for communication with computer
}

void loop() {
  if (Serial.available() > 0) {

    userInput = Serial.read(); // read serial input from computer
      
    if(userInput == 'g'){
      sensorValue = analogRead(sensorPin); // read sensor 
      Serial.println(sensorValue); // send sensor value to computer
    }
  }
}
