#include <RPLidar.h>
#include "MecanumDriver.h" 
#include <Arduino.h>

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
    float left_dis = 0, right_dis = 0, offset = 0;
    float dis_90 = 0, dis_120 = 0, dis_270 = 0, dis_300 = 0, dis_temp=0;
    float angle_left = 0, angle_right = 0, angle_offset;
    int left_num = 0, right_num = 0;
    if (angle >= 0 && angle < 360) {                             // 角度值在[0, 359]范围内
      distances[angle] = distance;                               // 将距离值存储到数组
    }

    if (startBit) {             // 每进入一次新的扫描处理并控制一次
      for (int angle = 90; angle < 135; angle++)
      {
        if (distances[angle] >= 0.15)
        {
          left_dis += distances[angle];
          left_num++;
        }
      }

      left_dis /= 45;
      
      for (int angle = 225; angle < 270; angle++)
      {
        if (distances[angle] >= 0.15)
        {
          right_dis += distances[angle];
          right_num++;
        }
      }
      right_dis /= 45;

      offset = left_dis - right_dis;
      //offset = distances[90] - distances[270];

      Serial.print("left dis: ");
      Serial.print(left_dis, 3);
      Serial.print('\n');
      Serial.print("right dis: ");
      Serial.print(right_dis, 3);
      Serial.print('\n');
      Serial.print("offset: ");
      Serial.print(offset, 3);
      Serial.print('\n');

/*
      dis_90 = distances[90];
      dis_120 = distances[100];+
      dis_270 = distances[270];
      dis_300 = distances[280];
      Serial.println(dis_90);
      Serial.println(dis_120);
      Serial.println(dis_270);
      Serial.println(dis_300);
      //Serial.println(distances);

      dis_temp = sqrt(dis_90*dis_90 + dis_120*dis_120 - 2 * dis_90 * dis_120 * cos(3.14 / 18));
      angle_left = acos((dis_90*dis_90 + dis_temp*dis_temp - dis_120*dis_120) / (2*dis_90*dis_temp));
      Serial.println(dis_temp, 3);
      dis_temp = sqrt(dis_270*dis_270 + dis_300*dis_300 - 2 * dis_270 * dis_300 * cos(3.14 / 18));
      Serial.println(dis_temp, 3);
      Serial.println(acos(0.5));
      angle_right = acos((dis_270*dis_270 + dis_temp*dis_temp - dis_300*dis_300) / (2*dis_270*dis_temp));

      angle_offset = 3.14 / 2 - (angle_left + angle_right) / 2;

      Serial.print("left angle: ");
      Serial.print(angle_left, 3);
      Serial.print('\n');
      Serial.print("right angle: ");
      Serial.print(angle_right, 3);
      Serial.print('\n');
      Serial.print("offset angle: ");
      Serial.print(angle_offset, 3);
      Serial.print('\n');

*/
      if (true){
        mecanum.driveAllMotor(70-60*offset, 70+60*offset, 70-60*offset, 70+60*offset);
      }
      else
      {
        mecanum.driveAllMotor(70, 70, 70, 70);
      }
      
      //mecanum.driveAllMotor(70 + angle_offset / 2, 70 - angle_offset / 2, 70 + angle_offset / 2, 70 - angle_offset / 2);

      //mecanum.driveAllMotor(100, 50, 100, 50);
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
