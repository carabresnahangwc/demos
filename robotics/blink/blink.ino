// Let There Be Light: Part 2

int pin = 13; // Make sure your circuit is using digital pin 13!

void setup() {
  // put your setup code here, to run once:
  pinMode(pin, OUTPUT);

}

void dot(){
  digitalWrite(pin, HIGH); //turn on 
  delay(250);
  digitalWrite(pin, LOW);  //turn off
  delay(250);
}

void dash(){
  digitalWrite(pin, HIGH);
  delay(750);
  digitalWrite(pin, LOW);
  delay(250);
}


void loop() {
  // put your main code here, to run repeatedly:

  dot();
  dash();
  dash();
}
