#include <Servo.h>

Servo myservo;

void setup() {
  myservo.attach(3);  // 将舵机连接到数字引脚4
  Serial.begin(9600);
}

void loop() {
  myservo.write(0);  // 将舵机旋转到0度位置
  Serial.println("0");
  delay(1000);      // 等待1秒
  myservo.write(90); // 将舵机旋转到90度位置
  Serial.println("90");
  delay(1000);      // 等待1秒
  myservo.write(180); // 将舵机旋转到180度位置
  Serial.println("180");
  delay(1000);      // 等待1秒
  myservo.write(90);
  Serial.println("90");
  delay(1000);
  myservo.write(0);
  Serial.println("0");
  delay(1000);
  myservo.write(-90); // 将舵机旋转到90度位置
  Serial.println("-90");
  delay(1000);      // 等待1秒
  myservo.write(-180); // 将舵机旋转到180度位置
  Serial.println("-180");
  delay(1000);      // 等待1秒
  myservo.write(-90); // 将舵机旋转到90度位置
  Serial.println("-90");
  delay(1000);
}