#include <Servo.h>

Servo s1; // servo object
Servo s2; // servo object

//servo 1
int angle1; // variable to adjust angle 

//servo 2
int angle2; // variable to adjust angle 

//record angles
int i = 0;
int recAng1[10];
int recAng2[10];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  s1.attach(10); // servo attached to pin 9
  s2.attach(8); // servo attached to pin 8
  s1.write(90); // start in neutral
  s2.write(90); // start in neutral
}

void loop(){
  if(Serial.available() > 0){
    String data = Serial.readStringUntil('\n');
    if(data == "M1"){
      String data1 = Serial.readStringUntil('\n');
      angle1 = data1.toInt();
      angle1 = angle1 + 90;
      s1.write(angle1);
    }
    else if(data == "M2"){
      String data2 = Serial.readStringUntil('\n');
      angle2 = data2.toInt();
      angle2 = angle2 + 90;
      s2.write(angle2);
    }
  }
}
