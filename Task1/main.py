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


import torch.nn as nn
import torch.nn.functional as F
import os

from torch.utils.data import Dataset, DataLoader

import torch.optim as optim

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
        
transform = transforms.Compose([
    transforms.Resize((28, 28)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,)),
    transforms.Grayscale(num_output_channels = 1)
])


        
class TrafficSignNet(nn.Module):
    def __init__(self):
        super(TrafficSignNet, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(1,16,3,padding=1),
            #nn.LeakyReLU(0.01),
            nn.Conv2d(16,16,5),
            nn.ReLU(),
            #nn.LeakyReLU(0.01),
            nn.MaxPool2d(2,stride=2),
            nn.Dropout(0.3),
            nn.Conv2d(16,32,5),
            nn.ReLU(),
            #nn.LeakyReLU(0.01),
            nn.MaxPool2d(2, stride=2),
            nn.Dropout(0.3)
        )
        self.fc = nn.Sequential(
            nn.Linear(32*4*4,100),
            nn.ReLU(),
            nn.Linear(100,4)
        )

    def forward(self, x):
        x= self.conv(x)
        x=x.view(-1,32*4*4)
        x= self.fc(x)
        return x
    

# 实例化网络
net = TrafficSignNet()
net.load_state_dict(torch.load('model5.pth', map_location = 'cpu'))
net.double()
net.eval()


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
turn_cout = 1
can_add = False
is_follow = False
stop_cout = 0
try:
    while True:
        #print("while start")
        frame = videostream.read()
        
        frame = cv2.resize(frame, None, fx = 0.25, fy = 0.25, interpolation = cv2.INTER_NEAREST)
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #print(type(frame))
        
        
        lower_yellow = np.array([0, 0, 220])
        upper_yellow = np.array([180, 255, 255])
        lower_blue = np.array([100, 80, 150])
        upper_blue = np.array([124,255,255])
        
        mask2 = cv2.inRange(hsv_img, lower_yellow, upper_yellow)
        mask_blue = cv2.inRange(hsv_img, lower_blue, upper_blue)
        cv2.imshow("MaskBlue", mask_blue)
        
        height, width = mask2.shape
        blue_point = 0
        
        blueUP = 120
        blueLow = 0
        blueLe = 160
        blueRi = 0
        for i in range(1, 119):
            for j in range(10, 150):
                if (mask_blue[i][j] == 255 and (mask_blue[i][j+1] == 255 or mask_blue[i][j-1] == 255)):
                    blue_point += 1
                    if (i < blueUP):
                        blueUP = i
                    if (i > blueLow):
                        blueLow = i
                    if (j < blueLe):
                        blueLe = j
                    if (j > blueRi):
                        blueRi = j
                      
        #blueUP = blueLow + (blueRi - blueLe)
                        
        #print(blueUP, blueLow, blueLe, blueRi)
    
        hsv_cut = []
        for i in range(blueUP, blueLow+1):
            temp = []
            for j in range(blueLe, blueRi+1):
                temp.append(frame[i][j])
            hsv_cut.append(temp)
            
        hsv_cut = np.array(hsv_cut)
        print("blue num: ", blue_point)
        #print(hsv_cut)
        if (hsv_cut.shape[0] == 0):
            continue
            #hsv_cut = np.append(hsv_cut, [])
        #cv2.imshow('cut',hsv_cut)

        img_pil = Image.fromarray(frame)
        #img_pil = transforms.CenterCrop(100)(img_pil)
        img_show = np.array(img_pil)
        cv2.imshow('img_show', img_show)
        #img_pil = img_pil.convert('L')
        
        roi = transform(img_pil)
        roi = roi.unsqueeze(1)
        with torch.no_grad():
            outputs = net(roi.double())
            _, predicted = torch.max(outputs.data, 1)
        #print('output data: ',outputs.data)
        max_label = int(predicted)
        print("label: ", max_label)
        print("blue num: ", blue_point)
                
        line_y = int(height * 0.9)
        
        line_section2 = mask2[line_y]
        #print(line_section2)
        
        centerPoint = 0
        whiteNum = 0
        for i in range(10, 150):
            if line_section2[i] == 255:
                centerPoint += i
                whiteNum += 1
            
        if (whiteNum == 0):
            offset = 0
        else:
            centerPoint /= whiteNum
            #print(centerPoint)
            offset = centerPoint - 80
            
        print("offset: ",offset)
        #turn_cout += 1
        #car.set_speed(0, 0, 0)

        if (turn_cout < 1):
            turn_cout += 1
            car.set_speed(50, 0, 100)
        else:
            car.set_speed(50, 0, -offset)
        
        if (blue_point < 100 and can_add):
            turn_cout += 1
            can_add = False
           
        if (turn_cout == 1):
            if (blue_point >= 400):
                car.set_speed(50, 0, 85.5)
                can_add = True
            else:
                car.set_speed(50,0,-0.45*offset)
        elif (turn_cout == 2):
            if (blue_point >= 300):
                car.set_speed(50,0,-90)
                can_add = True
            else:
                car.set_speed(50, 0, -0.45*offset)
        elif (turn_cout == 3):
            if (blue_point >= 300):
                car.set_speed(50,0,-85)
                can_add = True
            else:
                car.set_speed(50,0,-0.5*offset)
        elif (turn_cout ==4):
            if (stop_cout >= 6):
                car.set_speed(0,0,0)
            else:
                car.set_speed(50,0,0)
                stop_cout+= 1
        print("turn: ", turn_cout)
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask2", mask2)
        print("round: ", turn_cout)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;

finally:
    # 确保在程序退出前停止小车
    print("Stopping the vehicle...")
    car.set_speed(0, 0, 0)
    videostream.stop()
    cv2.destroyAllWindows()


        
