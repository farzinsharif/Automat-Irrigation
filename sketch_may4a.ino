const int pumpPin = 6;
const int soilSensor = A5;
const int dry = 600;

void setup() {
  pinMode(pumpPin, OUTPUT);
  pinMode(soilSensor, INPUT);
  Serial.begin(9600);
  digitalWrite(pumpPin, HIGH);
}

void loop() {
  int humidity = analogRead(soilSensor);
  Serial.println(humidity);
  delay(1000);
  
  if (humidity >= dry) {    
    
    // Serial.println("humidity level is " + String(humidity));
    digitalWrite(pumpPin, LOW);

    // delay(7000);

    digitalWrite(pumpPin, HIGH);
    // Serial.println("Completion of irrigation");
  } else {
    digitalWrite(pumpPin, HIGH);
    Serial.println(humidity);
  //  Serial.println("The soil moisture level is suitable. There is no need to irrigate");
  }
}