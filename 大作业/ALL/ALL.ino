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
  //motorRun(FORWARD,200);
  switch(state){
    case FORWARD:
      motorRun(FORWARD, 200);
      break;
    case TURNRIGHT:
      motorRun(TURNRIGHT, 250);
      break;
    case TURNLEFT:
      motorRun(TURNLEFT, 250);
      break;
    default:
      motorRun(FORWARD, 200);
  }
  myServo.write(90);
  //delay(15);
  dis[1]=0; //中间
  //Serial.print("front: ");
  //Serial.println(dis[1]);

  for (pos = 90; pos <= 170; pos += 1) 
    {
      myServo.write(pos);              // tell servo to go to position in variable 'pos'
      delay(5);                       // waits 15ms for the servo to reach the position
    }
    dis[2]=getDistance(); //左边
    for (pos = 170; pos >= 10; pos -= 1) 
    {
      myServo.write(pos);              // tell servo to go to position in variable 'pos'
      delay(5);                       // waits 15ms for the servo to reach the position
      if(pos < 113 && pos >= 68)
        dis[1] += getDistance(); //中间
    }
    dis[0]=getDistance();  //右边
    dis[1] /= 45;
    for (pos = 10; pos <= 90; pos += 1) 
    {
      myServo.write(pos);              // tell servo to go to position in variable 'pos'
      delay(5);                       // waits 15ms for the servo to reach the position
    }

  //myServo.write(0);
  //delay(15);
  //dis[0] = getDistance();
  Serial.print("right: ");
  Serial.println(dis[0]);
  Serial.print("front: ");
  Serial.println(dis[1]);
  Serial.print("left: ");
  Serial.println(dis[2]);

  offset = dis[0] - dis[2];

  if (dis[0] > 47){
    //右转
    state = TURNRIGHT;
    myServo.write(0);
    //motorRun(FORWARD, 200);
    //delay(500);
    motorRun(FORWARD, 200);
    delay(50);
    motorRun(TURNRIGHT,250);
    delay(50);
    motorRun(FORWARD, 200);
    delay(1000);
    //state = TURNRIGHT;
    
  }
  else if(dis[1]<35)
  {
    if (true)
    {
      //左转
      state = TURNLEFT;
      motorRun(STOP, 0);
      myServo.write(0);
      delay(500);
      dis[0] = getDistance();
      if (getDistance() < 45){
        myServo.write(90);
        dis[1] = getDistance();
        while(dis[1] < 35){
          if (dis[1] < 10){
            motorRun(BACKWARD,200);
            delay(500);
            motorRun(TURNLEFT, 250);
            delay(50);
          }
          else if (dis[0] < 20){
            motorRun(TURNLEFT, 250);
            delay(50);
            motorRun(FORWARD, 200);
            delay(500);

          }
          Serial.print("turn left, front dis: ");
          Serial.println(dis[1]);
          dis[1] = getDistance();
          motorRun(TURNLEFT,250);
          delay(50);
        }
        state = FORWARD;
      }
      else{
        state = TURNRIGHT;
        motorRun(TURNRIGHT, 250);
        delay(50);
        motorRun(FORWARD, 200);
        delay(1000);
      }
      
      
    }
  }
  else{
    state = FORWARD;
    motorRun(FORWARD, 200);
    //delay(50);
    if (dis[0] < 20){
      state = TURNLEFT;
      motorRun(TURNLEFT, 250);
      delay(20);
    }
  }
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
