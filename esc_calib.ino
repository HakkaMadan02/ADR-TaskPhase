#include <Servo.h>

#define MAX_SIGNAL 2000
#define MIN_SIGNAL 1000
#define MOTOR_PIN 9
int DELAY = 1000;

Servo motor;
void setup() {
  Serial.begin(9600);
  Serial.println("Starting calibberation ...");
  Serial.println("  ");
  delay(1500);
  
  motor.attach(MOTOR_PIN);

  Serial.println("writing maximum output");
  Serial.println("MAX_SIGNAL");
  Serial.println("Turn on power source, then wait for 2 seconds and press any key");
  motor.writeMicroseconds(MAX_SIGNAL);

  //waiting for input//
  while (!Serial.available());
  Serial.read();

  //send min input//
  Serial.println("\n");
  Serial.println("\n");
  Serial.println("sending minimum output: ");
  motor.writeMicroseconds(MIN_SIGNAL);
  Serial.println("ESC is now calliberated");

  Serial.println("Type a value between 100 and 200 and press enter");
  Serial.println("motor will now start spinning");
  


}

void loop() {
  if (Serial.available() > 0)
  {
    int DELAY = Serial.parseInt();
    if (DELAY > 999)
    {
      motor.writeMicroseconds(DELAY);
      float SPEED = (DELAY - 1000)/10;
      Serial.println("\n");
      Serial.println("Motor speed :");
      Serial.println("  ");
  Serial.println(SPEED); Serial.println("%");          
      
    }
  }

}
