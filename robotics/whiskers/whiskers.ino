#include <Servo.h>                           // Include servo library

Servo servoLeft;                             // Declare left servo signal
Servo servoRight;                            // Declare right servo signal

int leftWhisker = 5;
int rightWhisker = 7;

void setup() {
  Serial.begin(9600); //serial port at 9600
  Serial.println("Set up port "); // println gives us a new line
  Serial.print("and stuff"); // print will not return with a new line
  
  //Set our pins to input mode
  pinMode(leftWhisker, INPUT);
  pinMode(rightWhisker, INPUT);

  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);                     // Attach right signal to pin 12
  servoLeft.writeMicroseconds(1500);        // Calibrate left servo
  servoRight.writeMicroseconds(1500);       // Calibrate right servo

}

void loop() {
  //get input value from whiskers
  int leftWhiskerValue = digitalRead(leftWhisker);
  int rightWhiskerValue = digitalRead(rightWhisker);
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
  //AND operator uses && between the two conditions
  //OR operator uses || between two conditions
  //NOT operator uses ! before the condition
  //CONDITIONS should always go in parenthesis ()
  if(leftWhiskerValue == 0 && rightWhiskerValue == 0){ 
     Serial.println("Both Whiskers Pushed!");
     servoLeft.writeMicroseconds(-1700);
     servoRight.writeMicroseconds(-1300);
  } else if(leftWhiskerValue == 0){
    Serial.println("Left Whisker Pushed!");
    servoLeft.writeMicroseconds(0);
  } else if(rightWhiskerValue == 0){
    Serial.println("Right Whisker Pushed!");
    servoRight.writeMicroseconds(0);
  } else {
    Serial.println("No whiskers pushed!");
  }
  
  //  
  //  Serial.print("Left: ");
  //  Serial.println(leftWhiskerValue);
  //  Serial.print("Right: ");
  //  Serial.println(rightWhiskerValue);
  //have slight delay so we don't over load our bot
  delay(500);
}
