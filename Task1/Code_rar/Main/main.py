# coding:utf-8
# 加入摄像头模块，让小车实现自动循迹行驶
# 思路为:摄像头读取图像，进行二值化，将白色的赛道凸显出来
# 选择下方的一行像素，红色为 0
# 找到0值的中点
# 目标中点与标准中点(320)进行比较得出偏移量
# 根据偏移量来控制小车左右轮的转速
# 考虑了偏移过多失控->停止;偏移量在一定范围内->高速直行(这样会速度不稳定，已删)

# import pandas as pd
# from scipy import linalg
# import tflite_runtime.interpreter as tflite
# import threading  
# import threading  # 导入 threading 库

import cv2
import numpy as np
from new_driver import driver
import time
from threading import Thread
import cv2
import torch
import torchvision.transforms as transforms
from PIL import Image

STRAIGHT_POWER = 60
DETECTION_THRESH = 50
# Define VideoStream class to handle streaming of video from webcam in separate processing thread
class VideoStream:
    """Camera object that controls video streaming from the Picamera"""
    def __init__(self,resolution=(640,480),framerate=20):
        # Initialize the PiCamera and the camera image stream
        self.stream = cv2.VideoCapture(0)
        #ret = self.stream.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        #ret = self.stream.set(3,resolution[0])
        #ret = self.stream.set(4,resolution[1])
            
        # Read first frame from the stream
        (self.grabbed, self.frame) = self.stream.read()

    # Variable to control when the camera is stopped
        self.stopped = False

    def start(self):
    # Start the thread that reads frames from the video stream
        Thread(target=self.update,args=()).start()
        return self

    def update(self):
        # Keep looping indefinitely until the thread is stopped
        while True:
            # If the camera is stopped, stop the thread
            if self.stopped:
                # Close camera resources
                self.stream.release()
                return

            # Otherwise, grab the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
    # Return the most recent frame
        return self.frame

    def stop(self):
    # Indicate that the camera and thread should be stopped
        self.stopped = True

car = driver()
# 定义看到crosswalk的次数
crosswalk_num = 0
# 初始化输入网络的图像尺寸
image_size=(28,28)
# 打开摄像头，图像尺寸 640*480(长*高)，opencv 存储值为 480*640(行*列) 
videostream = VideoStream(resolution=(480,640),framerate=10).start()
time.sleep(1)

# upload calibration matrix
# data = np.load('calibration.npz')
# cameraMatrix = data['cameraMatrix']
# distCoeffs = data['distCoeffs']
preOffset = 0
blind_second = 0
try:
    while True:
        #print("while start")
        frame = videostream.read()
        
        frame = cv2.resize(frame, None, fx = 0.25, fy = 0.25, interpolation = cv2.INTER_NEAREST)
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #lower_white = np.array([0, 0, 230])
        #upper_white = np.array([180, 30, 255])
        #lower_yellow = np.array([0, 0, 180])
        #upper_yellow = np.array([180, 255, 255])
        lower_yellow = np.array([0, 0, 180])
        upper_yellow = np.array([180, 255, 255])
        
        #mask = cv2.inRange(hsv_img, lower_white, upper_white)
        mask2 = cv2.inRange(hsv_img, lower_yellow, upper_yellow)
        
        height, width = mask2.shape
        line_y = int(height * 0.9)
        
        line_section2 = mask2[line_y]
        #line_section = mask[line_y]
        #print(line_section)
        print(line_section2)
        #sum_width = np.sum(line_section)
        #if sum_width == 0
        #    print("Sum width == 0")
        #    continue
        
        #midpoint = int(np.where(line_section == 255)[0].mean())
        
        centerPoint_left = 0
        whiteNum_left = 0
        for i in range(0, 80):
            if line_section2[i] == 255:
                centerPoint_left += i
                whiteNum_left += 1
            #if line_section[i+1] == 0:
              #  break;
                
        centerPoint_right = 0
        whiteNum_right = 0
        for i in range(80, 160):
            if line_section2[i] == 255:
                centerPoint_right += i
                whiteNum_right += 1
            #if line_section[i+1] == 0:
             #   break;
            
                
        if (whiteNum_left == 0 and whiteNum_right != 0):
            centerPoint_right /= whiteNum_right
            centerPoint_left = 0
            offset = (centerPoint_left + centerPoint_right) / 2 - 80
        elif (whiteNum_right == 0 and whiteNum_left != 0):
            centerPoint_left /= whiteNum_left
            centerPoint_right = 160
            offset = (centerPoint_left + centerPoint_right) / 2 - 80
        elif (whiteNum_right != 0 and whiteNum_left != 0):
            centerPoint_right /= whiteNum_right
            centerPoint_left /= whiteNum_left
            offset = (centerPoint_left + centerPoint_right) / 2 - 80
        else :
            offset = 0
            
        #if whiteNum_left > 30 or whiteNum_right > 30:
        #    blind_second += 1
        #    if (blind_second <= 30):
        #        offset = preOffset
        #    else:
        #        offset = 0
        #else:
        #    preOffset = offset
            
        #offset = 46.5 - centerPoint_left
                
        #offset -= 10
        #print("center point: ", centerPoint)
        #print("WhiteNum: ", whiteNum)
        #center_position = width // 2
        #offset = centerPoint - center_position
        #print("center position: ", center_position)
        print("offset: ", offset)
        #print("centerPoint left : ", centerPoint_left)
        #print("centerPoint right: ", centerPoint_right)
        #if abs(offset) > DETECTION_THRESH:
            #print("turn1")
            #car.set_speed(50, 0, -offset)
        #elif (abs(offset) > 30 and abs(offset) < 40):
            #print("turn2")
            #car.set_speed(50, 0, -offset)
        #else:
            #print("straight")
            #car.set_speed(50, 0, 0)
            
        #car.set_speed(0, 0, 0)
        car.set_speed(100, 0, -2*offset)
        #car.set_speed(0, 0, 0)
        #car.set_speed(0, 0, 0)
    
        #cv2.imshow("Mask", mask)
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask2", mask2)
        #print("blind: ", blind_second)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;
        #car.set_speed(STRAIGHT_POWER, 0, 0)

finally:
    # 确保在程序退出前停止小车
    print("Stopping the vehicle...")
    car.set_speed(0, 0, 0)
    videostream.stop()
    cv2.destroyAllWindows()


        
