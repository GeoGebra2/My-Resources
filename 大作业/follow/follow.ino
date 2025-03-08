#include <Servo.h>

#define STOP      0
#define FORWARD   1
#define BACKWARD  2
#define TURNLEFT  3
#define TURNRIGHT 4

int leftMotor1 = 9;
int leftMotor2 = 10;
int rightMotor1 = 11;
int rightMotor2 = 12;

int leftPWM = 5;
int rightPWM = 6;

Servo myServo;  //舵机

int inputPin=7;   // 定义超声波信号接收接口
int outputPin=8;  // 定义超声波信号发出接口

int state = FORWARD;

void setup() {
  // put your setup code here, to run once:
  //串口初始化
  Serial.begin(9600); 
  //舵机引脚初始化
  myServo.attach(3);
  //测速引脚初始化
  pinMode(leftMotor1, OUTPUT);
  pinMode(leftMotor2, OUTPUT);
  pinMode(rightMotor1, OUTPUT);
  pinMode(rightMotor2, OUTPUT);
  pinMode(leftPWM, OUTPUT);
  pinMode(rightPWM, OUTPUT);
  //超声波控制引脚初始化
  pinMode(inputPin, INPUT);
  pinMode(outputPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  avoidance();
}
void motorRun(int cmd,int value)
{
  analogWrite(leftPWM, value);  //设置PWM输出，即设置速度
  analogWrite(rightPWM, value);
  switch(cmd){
    case FORWARD:
      Serial.println("FORWARD"); //输出状态
      digitalWrite(leftMotor1, HIGH);
      digitalWrite(leftMotor2, LOW);
      digitalWrite(rightMotor1, HIGH);
      digitalWrite(rightMotor2, LOW);
      //delay(1000);
      break;
     case BACKWARD:
      Serial.println("BACKWARD"); //输出状态
      digitalWrite(leftMotor1, LOW);
      digitalWrite(leftMotor2, HIGH);
      digitalWrite(rightMotor1, LOW);
      digitalWrite(rightMotor2, HIGH);
      //delay(1000);
      break;
     case TURNLEFT:
      Serial.println("TURN  LEFT"); //输出状态
      digitalWrite(leftMotor1, HIGH);
      digitalWrite(leftMotor2, LOW);
      digitalWrite(rightMotor1, LOW);
      digitalWrite(rightMotor2, HIGH);
      //delay(1000);
      break;
     case TURNRIGHT:
      Serial.println("TURN  RIGHT"); //输出状态
      digitalWrite(leftMotor1, LOW);
      digitalWrite(leftMotor2, HIGH);
      digitalWrite(rightMotor1, HIGH);
      digitalWrite(rightMotor2, LOW);
      //delay(1000);
      break;
     default:
      Serial.println("STOP"); //输出状态
      digitalWrite(leftMotor1, LOW);
      digitalWrite(leftMotor2, LOW);
      digitalWrite(rightMotor1, LOW);
      digitalWrite(rightMotor2, LOW);
  }
}
void avoidance()
{
  int pos;
  double dis[3];//距离
  double offset;
  
  myServo.write(90);
  //delay(15);
  dis[1]=getDistance(); //中间
  Serial.print("front: ");
  Serial.println(dis[1]);

  if (dis[1] > 30 and dis[1] < 200){
    motorRun(FORWARD, 200);
  }
  else if (dis[1] < 30){
    motorRun(BACKWARD, 200);
  }
  else{
    motorRun(STOP, 0);
  }
  /*
  myServo.write(30);
  double minAngle = 30, minDis = getDistance();
  for (pos = 30; pos <= 150; pos += 1) 
  {
      myServo.write(pos);              // tell servo to go to position in variable 'pos'
      delay(15);                       // waits 15ms for the servo to reach the position
      if (getDistance() < minDis){
        minDis = getDistance();
        minAngle = pos;
      }
      
  }
  Serial.print("1angle: ");
  Serial.println(minAngle);
  Serial.print("1dis: ");
  Serial.println(minDis);

  if (minDis < 30 || minDis > 200){
    motorRun(STOP, 0);
  }
  else{
    if (minAngle >= 60 && minAngle <= 120){
      motorRun(FORWARD, 200);
      delay(1000);
    }
    else if(minAngle < 60)
    {
      motorRun(TURNRIGHT, 250);
      delay(90 - minAngle);
    }
    else{
      motorRun(TURNLEFT, 250);
      delay(minAngle - 90);
    }
  }

  minDis = getDistance();

  for (pos = 150; pos >= 30; pos -= 1) 
  {
      myServo.write(pos);              // tell servo to go to position in variable 'pos'
      delay(15);                       // waits 15ms for the servo to reach the position
      if (getDistance() < minDis){
        minDis = getDistance();
        minAngle = pos;
      }
      
  }
  Serial.print("2angle: ");
  Serial.println(minAngle);
  Serial.print("2dis: ");
  Serial.println(minDis);

  if (minDis < 30 || minDis > 200){
    motorRun(STOP, 0);
  }
  else{
    if (minAngle >= 60 && minAngle <= 120){
      motorRun(FORWARD, 200);
      delay(1000);
    }
    else if(minAngle < 60)
    {
      motorRun(TURNRIGHT, 250);
      delay(90 - minAngle);
    }
    else{
      motorRun(TURNLEFT, 250);
      delay(minAngle - 90);
    }
  }*/


  
  

}
int getDistance()
{
  digitalWrite(outputPin, LOW); // 使发出发出超声波信号接口低电平2μs
  delayMicroseconds(2);
  digitalWrite(outputPin, HIGH); // 使发出发出超声波信号接口高电平10μs，这里是至少10μs
  delayMicroseconds(10);
  digitalWrite(outputPin, LOW); // 保持发出超声波信号接口低电平
  int distance = pulseIn(inputPin, HIGH); // 读出脉冲时间
  distance= distance/58; // 将脉冲时间转化为距离（单位：厘米）
  //Serial.println(distance); //输出距离值
 
  return distance;
}
