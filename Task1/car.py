import cv2
import numpy as np
from new_driver import driver
import time
from threading import Thread

STRAIGHT_POWER = 70
DETECTION_THRESH = 5  # 设定一个阈值，用于判断路径中心偏移

# Define VideoStream class to handle streaming of video from webcam in separate processing thread
class VideoStream:
    def __init__(self, resolution=(640, 480), framerate=20):
        self.stream = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                self.stream.release()
                return
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True

car = driver()
videostream = VideoStream(resolution=(480, 640), framerate=10).start()
time.sleep(1)

try:
    while True:
        frame = videostream.read()
        frame = cv2.resize(frame, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_NEAREST)
        
        # 转换为HSV颜色空间
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 设定白色的HSV范围
        lower_white = np.array([0, 0, 200])  # 根据实际情况调整
        upper_white = np.array([180, 25, 255])

        # 进行二值化处理
        mask = cv2.inRange(hsv_img, lower_white, upper_white)

        # 选择下方某一行像素（例如第90行），计算其像素值
        height, width = mask.shape
        line_y = int(height * 0.25)  # 选择图像底部的75%
        line_section = mask[line_y]

        # 找到0值的中点
        sum_width = np.sum(line_section)
        if sum_width == 0:
            continue  # 如果没有检测到路径则跳过

        midpoint = int(np.where(line_section == 255)[0].mean())
        centerPoint = 0
        whiteNum = 0
        for i in range(24, 55):
            if line_section[i] == 255:
                centerPoint += i
                whiteNum += 1
        
        centerPoint /= whiteNum

        print("center point: ", centerPoint)
        print("whiteNum: ", whiteNum)
        # 计算偏移量
        center_position = width // 2
        offset = centerPoint - center_position
        print("offset: ", offset)
        
        # 根据偏移量调整小车速度
        if abs(offset) > DETECTION_THRESH:
            car.set_speed(STRAIGHT_POWER, 0, -offset * 3)  # 控制小车

        else:
            car.set_speed(STRAIGHT_POWER, 0, 0)  # 控制小车

        # 可视化
        cv2.imshow("Mask", mask)
        cv2.imshow("Frame", frame)

        # 按q键可以退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    print("Stopping the vehicle...")
    car.set_speed(0, 0, 0)
    videostream.stop()
    cv2.destroyAllWindows()