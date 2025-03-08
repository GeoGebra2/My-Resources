#include <RPLidar.h>
#include "MecanumDriver.h" 

// 创建激光雷达对象
RPLidar lidar;
// 创建麦克纳姆轮驱动器对象
MecanumDriver mecanum(9, 8, 12, 13, 11, 10, 46, 21);
// 用于存储激光雷达数据的数组（0到359度共360个值）
float distances[360] = { 0 };
float directions[8] = {0};

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
    if (angle >= 0 && angle < 360) {                             // 角度值在[0, 359]范围内
      distances[angle] = distance;                               // 将距离值存储到数组
    }

    if (startBit) {             // 每进入一次新的扫描处理并控制一次
      float distance_min = 10;  // 用于存储最近障碍物距离
      int angle_min = 0;        // 用于存储最近障碍物对应角度
      // 遍历寻找[0, 359]范围内最近障碍物距离及其对应角度
      for (int angle = 0; angle < 360; angle++) {
        float distance = distances[angle];
        if (distance >= 0.15) {           // 激光雷达的最小量程为0.15m，>=0.15的才是有效数据
          if (distance < distance_min) {  // 如果障碍物距离<最近距离
            distance_min = distance;      // 更新障碍物最近距离
            angle_min = angle;            // 更新最近障碍物对应角度
          }
        }
      }
      //Serial.print("dis: ");
      //Serial.println(distance_min, 4);
      //Serial.println('\n');
      //Serial.print(" angle: ");
      //Serial.println(angle_min, 4);
      //Serial.println('\n');
      if (distance_min <= 0.4){
        if ((angle_min >= 0 && angle_min <= 22.5) || (angle_min > 337.5 && angle_min < 360))
        {
          mecanum.driveAllMotor(100, 100, 100, 100);
        }
        else if (angle_min > 22.5 && angle_min <= 67.5)
        {
          mecanum.driveAllMotor(100, 0, 0, 100);
        }
        else if (angle_min > 67.5 && angle_min <= 112.5)
        {
          mecanum.driveAllMotor(100, -100, -100, 100);
        }
        else if (angle_min > 112.5 && angle_min <= 157.5)
        {
          mecanum.driveAllMotor(0, -100, -100, 0);
        }
        else if (angle_min > 157.5 && angle_min <= 202.5)
        {
          mecanum.driveAllMotor(-100, -100, -100, -100);
        }
        else if (angle_min > 202.5 && angle_min <= 247.5)
        {
          mecanum.driveAllMotor(-100, 0, 0, -100);
        }
        else if (angle_min > 247.5 && angle_min <=292.5)
        {
          mecanum.driveAllMotor(-100, 100, 100, -100);
        }
        else if (angle_min > 292.5 && angle_min <=337.5)
        {
          mecanum.driveAllMotor(0, 100, 100, 0);
        }
      }
      else
      {
        mecanum.driveAllMotor(0,0,0,0);
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
