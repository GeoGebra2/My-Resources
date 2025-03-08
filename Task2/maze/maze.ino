#include <RPLidar.h>
#include "MecanumDriver.h" 

// 创建激光雷达对象
RPLidar lidar;
// 创建麦克纳姆轮驱动器对象
MecanumDriver mecanum(9, 8, 12, 13, 11, 10, 46, 21);
// 用于存储激光雷达数据的数组（0到359度共360个值）
float distances[360] = { 0 };
float directions[8] = {0};

enum{
  BEGINNING = 0,
  TURN_LEFT = 1,
  TURN_RIGHT = 2,
  GO_STRAIGHT = 3,
  TURN_AROUND = 4
};

int state = BEGINNING;
bool have_turn = false;
int straight_count = 0;
bool start_count = false;
void setup() {
  Serial.begin(115200);  // 开启用于调试的串口
  lidar.begin(Serial2);  // 将激光雷达连接到串口2（19、20引脚）
  mecanum.begin();  // 启动麦克纳姆轮驱动器
}

void loop() {
  
  if (IS_OK(lidar.waitPoint())) {                                // 等到一个新的扫描点
    float distance = lidar.getCurrentPoint().distance / 1000.0;  // 距离值，单位m
    int angle = lidar.getCurrentPoint().angle;                   // 角度值（整数，四舍五入）
    bool startBit = lidar.getCurrentPoint().startBit;            // 每进入一次新的扫描时为true，其它时候为false
    float front_dis = 0, right_dis = 0, left_dis = 0;
    float left_dis2 = 0, right_dis2 = 0, right_dis3 = 0, front_dis2 = 0;
    int left_num = 0, right_num = 0, front_num = 0;
    double offset;
    if (angle >= 0 && angle < 360) {                             // 角度值在[0, 359]范围内
      distances[angle] = distance;                               // 将距离值存储到数组
    }
    if (startBit) {             // 每进入一次新的扫描处理并控制一次
      Serial.print("state: ");
      Serial.println(state);
      for (int angle = 158; angle < 203; angle++)
      {
        if (distances[angle] >= 0.15)
        {
          front_dis += distances[angle];
          front_num += 1;
        }
      }
      front_dis2 = front_dis / front_num;
      front_dis /= 45;


      for (int angle = 90; angle < 135; angle++)
      {
        if (distances[angle] >= 0.15)
        {
          left_dis += distances[angle];
          //left_num += 1;
        }
      }
      left_dis /= 45;
      

      for (int angle = 225; angle < 270; angle++)
      {
        if (distances[angle] >= 0.15)
        {
          right_dis += distances[angle];

        }
      }

      right_dis /= 45;
      //left_dis2 /= 45;

      for (int angle = 68; angle < 113; angle++)
      {
        if (distances[angle] >= 0.15)
        {
          left_dis2 += distances[angle];
          //left_num += 1;
        }
      }
      left_dis2 /= 45;

      for (int angle = 248; angle < 293; angle++)
      {
        if (distances[angle] >= 0.15)
        {
          right_dis2 += distances[angle];
          //left_num += 1;
        }
      }
      right_dis2 /= 45;


      Serial.print("front: ");
      Serial.print(front_dis);
      Serial.print("\n");
      Serial.println(front_dis2);
      Serial.print("left: ");
      Serial.print(distances[90]);
      Serial.print("\n");
      Serial.print("right: ");
      Serial.print(distances[270]);
      Serial.print("\n");
      Serial.print(left_dis);
      Serial.print("\n");
      Serial.print(right_dis);
      Serial.print("\n");
      Serial.println(left_dis2);
      Serial.println(right_dis2);

      bool canTurnRight = right_dis2 > 0.6 || right_dis > 0.6;
      bool canNotGoStraight = front_dis <= 0.35;
      bool canTurnLeft = left_dis2 > 0.6;
      bool canNotTurnRight = right_dis2 <= 0.3;
      bool canGoStraight = front_dis > 0.35;
      switch (state){
        case BEGINNING:
          state = GO_STRAIGHT;
          break;
        case TURN_RIGHT:
          if ((front_dis > 0.7 || front_dis2 > 1.0) && have_turn && (left_dis - right_dis < 0.55)){
            state = GO_STRAIGHT;
            start_count = true;
            //have_turn = true;
          }
          break;
        case TURN_LEFT:
          if (front_dis > 0.45){
            state = GO_STRAIGHT;
          }
          break;
        case GO_STRAIGHT:
          if (canTurnRight && !start_count){
            state = TURN_RIGHT;
            have_turn = false;
          }
          else if (canNotGoStraight && canTurnLeft){
            state = TURN_LEFT;
          }
          else if (front_dis < 0.35 && front_dis2 < 0.35){
            state = TURN_AROUND;
          }
          break;
        case TURN_AROUND:
          if (canGoStraight){
            state = GO_STRAIGHT;
          }
          break;
        default:
          state = GO_STRAIGHT;
          break;
      }

      switch(state){
        case TURN_RIGHT:
          Serial.println("turn right");
          if (front_dis < 0.5)
          {
            Serial.println("ttttttttttttttttttttttttttttttttttt");
            have_turn = true;
          }
          mecanum.driveAllMotor(70, 20, 70, 20);
          
          break;
        case TURN_LEFT:
          Serial.println("turn left");
          mecanum.driveAllMotor(-50, 50, -50, 50);
          break;
        case GO_STRAIGHT:
          Serial.println("straight");
          offset = right_dis - 0.3;
          if (start_count)
          {
            straight_count += 1;
          }
          if (straight_count > 7)
          {
            start_count = false;
            straight_count = 0;
          }
          mecanum.driveAllMotor(70+60*offset, 70-60*offset, 70+60*offset, 70-60*offset);

          break;
        case TURN_AROUND:
          Serial.println("turn around");
          mecanum.driveAllMotor(-50, 50, -50, 50);
          break;
        default:
          mecanum.driveAllMotor(100, 100, 100, 100);
          break;
      }
    }
  } else {
    // 重新连接激光雷达
    rplidar_response_device_info_t info;
    if (IS_OK(lidar.getDeviceInfo(info, 100))) {
      lidar.startScan();
      delay(1000);
    }
  }
}
