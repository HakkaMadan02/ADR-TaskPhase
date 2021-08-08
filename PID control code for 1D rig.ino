#include <Wire.h> 
#include <Servo.h> 
#include <SoftwareSerial.h> //importing the libraries

Servo right_motor ;
Servo left_motor ;


long accelX, accelY, accelZ ; //raw data for accelerometer
float AXg, AYg, AZg ; //acceleration values

long gyroX, gyroY, gyroZ ; //raw data for gyro
float rotX, rotY, rotZ ; //angle values for gyro

float rad_to_deg = 180.0/3.14 ;

float Acceleration_angle[2]; //will be calculating 2 angle values for x and y axis by accelerometer data
float Total_angle[2];
float desiredAngle = 0; //our desired setpoint for balancing the rig

float elapsedTime, time, PrevTime;

float Kp =3;
float Ki=1; //giving random practical values for the code to work
float Kd = 1;

double control_signal;
float error;
float total_error;
float delta_error;
float last_error;
float pwmLeft;
float pwmRight;

double throttle = 1300; //initial throttle value for the motors

float PID_P=0;
float PID_I=0;
float PID_D=0;




void setup() {
 
Serial.begin(9600);
Wire.begin(); //begin the wire communication
setupMPU(); //function to set up the MPU6050

right_motor.attach(3); //attaching the right motor to pin 3
right_motor.attach(5); //attaching the left motor to pin 5

time= millis(); //start counting time in milli seconds
left_motor.writeMicroseconds(1000); ///1000us is the minimum PWM value
right_motor.writeMicroseconds(1000);
delay(7000); //giving around 7s time for motors to start up and get adjusted to initial throttle value

}

void loop() {
  
recordAccelRegisters();
recordGyroRegisters(); //functions to set up gyro and accelerometer registers

Acceleration_angle[0] = atan((AYg)/sqrt(pow((AXg),2) + pow((AZg),2)))*rad_to_deg;
//X angle     
Acceleration_angle[1] = atan((AXg)/sqrt(pow((AYg),2) + pow((AZg),2)))*rad_to_deg;
//Y angle
//Euler formula for calculating the arctangent

PrevTime = time;  //stores the previous time before the actual time is read
time = millis();  // actual time read
elapsedTime = (time - PrevTime) / 1000; // time elapsed in our observation, in seconds
 
Total_angle[0] = 0.8 *(Total_angle[0] + rotX*elapsedTime) + 0.2*Acceleration_angle[0]; //rotation about
 //X angle 
Total_angle[1] = 0.8 *(Total_angle[1] + rotY*elapsedTime) + 0.2*Acceleration_angle[1];
 //Y angle
PID_Control();

left_motor.writeMicroseconds(pwmLeft);
right_motor.writeMicroseconds(pwmRight);
Serial.print(control_signal) ;
Serial.print(pwmLeft);
Serial.print(pwmRight);

printData();
delay(500); //wait half a minute before iterating again

}

void setupMPU(){
  Wire.beginTransmission(0b1101000); //I2C adress of the MPU
  Wire.write(0x6B);//6B is the power management register
  Wire.write(0b00000000); //setting sleep register to 0
  Wire.endTransmission();

  Wire.beginTransmission(0b1101000);
  Wire.write(0x1B); //Accessing register 1B which is for gyro configuration
  Wire.write(0b00000000); //using full scale +/- 250 deg per sec
  Wire.endTransmission();

  Wire.beginTransmission(0b1101000);
  Wire.write(0x1C); //Register for accelerometer configuration
  Wire.write(0b00000000); //Setting accel to +/- 2g sensitivity
  Wire.endTransmission();
  
}

void recordAccelRegisters(){
  Wire.beginTransmission(0b1101000); //I2C adress for the MPU
  Wire.write(0x3B); //starting register for acelerometer readings, there are 6 registers
  Wire.endTransmission();
  Wire.requestFrom(0b1101000,6);// requesting registers (3B-40)
  while(Wire.available() < 6);
  accelX = Wire.read()<<8|Wire.read(); //using bitwise operator. storing 1st two bytes in accelX
  accelY = Wire.read()<<8|Wire.read();// storing middle bytes in accelY
  accelZ = Wire.read()<<8|Wire.read(); //storing last two bytes in accelZ
  processAccelData();
  
}

void processAccelData(){
  AXg = accelX/16384.0 ; //diving by 16384 to get acceleration value from raw data
  AYg = accelY/16384.0 ;
  AZg = accelZ/16384.0 ;
  
}

void recordGyroRegisters() {
  Wire.beginTransmission(0b1101000); //requesting data from 6 gyro registers in thos function
  Wire.write(0x43); //43 is the starting gyro register
  Wire.endTransmission();
  Wire.requestFrom(0b1101000,6); // requesting gyro registers (43-48), hexadecimal adress
  while(Wire.available() < 6);
  gyroX = Wire.read()<<8|Wire.read(); 
  gyroY = Wire.read()<<8|Wire.read(); //storing bytes as mentioned before
  gyroZ = Wire.read()<<8|Wire.read(); 
  processGyroData();
}

void processGyroData() {
  rotX = gyroX / 131.0; //division by 131 as 65.5 reading in raw data means 1 degree per second movement in the MPU
  rotY = gyroY / 131.0; 
  rotZ = gyroZ / 131.0;
}

void printData(){

  Serial.begin(9600);
  Serial.print(" Gyro (deg) ");
  Serial.print(" X= ");
  Serial.print( rotX );
  Serial.print(" Y= ");
  Serial.print( rotY );
  Serial.print(" Z= ");
  Serial.print( rotZ );
  
  Serial.print(" Accel (g) ");
  Serial.print(" X= ");
  Serial.print( AXg );
  Serial.print(" Y= ");
  Serial.print( AYg );
  Serial.print(" Z= ");
  Serial.print( AZg );

}

void PID_Control(){

time = millis(); 
elapsedTime = (time - PrevTime) / 1000 ;  //in seconds



error = desiredAngle - Total_angle[0]; // along X axis, replace with [1] for Y axis

total_error += error; 
PID_P = Kp*error;

if (-3 < error < 3){
  PID_I = Ki*(total_error); // i need the integral to be on only in a small range of angle, otherwise it will cause Integral Winding
}

delta_error = error - last_error; // discontinuous difference in error, to be treated as d(e)/dt

PID_D = Kd*(delta_error / elapsedTime);

control_signal = PID_P + PID_I + PID_D ; 

if(control_signal < -1000)
{
  control_signal = -1000;
}
if(control_signal > 1000)
{
  control_signal = 1000; // since mimimum PWM value is 1000 and max is 2000, we can only give an additional value of 1000 or -1000 to fit inside the limits, hence the limits(-1000, 1000)
}

pwmLeft = throttle + control_signal ;
pwmRight = throttle - control_signal ;



//Right
if(pwmRight < 1000)
{
  pwmRight= 1000;
}
if(pwmRight > 2000)
{
  pwmRight=2000;
}
//Left
if(pwmLeft < 1000)
{
  pwmLeft= 1000;
}
if(pwmLeft > 2000)// 2000 is the maximum allowed PWM value
{
  pwmLeft=2000;
}

last_error = error; //storing values for the next iteration
PrevTime = time;
 
}
