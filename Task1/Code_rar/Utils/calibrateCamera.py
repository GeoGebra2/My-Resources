#!/usr/bin/env python

import cv2
import numpy as np
import os
import glob

# 定义棋盘格的尺寸
CHECKERBOARD = (6,9)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# 创建向量以存储每个棋盘图像的 3D 点向量
objpoints = []
# 创建向量以存储每个棋盘图像的 2D 点向量
imgpoints = [] 


# 定义 3D 点的世界坐标
objp = np.zeros((1, CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
objp[0,:,:2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)
prev_img_shape = None

# 提取存储在给定目录中的单个图像的路径
images = glob.glob('./*.jpg')
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # 找到棋盘角
    # 如果在图像中找到所需数量的角，则 ret = true
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)
    
    """
    如果检测到所需数量的角， 我们细化像素坐标并可视化
    """
    if ret == True:
        objpoints.append(objp)
        # 细化给定二维点的像素坐标。
        corners2 = cv2.cornerSubPix(gray, corners, (11,11),(-1,-1), criteria)
        
        imgpoints.append(corners2)

        # 绘制并显示角
        img = cv2.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)
    
    cv2.imshow('img',img)
    cv2.waitKey(0)

cv2.destroyAllWindows()

h,w = img.shape[:2]

"""
通过传递已知 3D 点 (objpoints) 的值 和检测到的角点（imgpoints）对应的像素坐标 实现相机标定
"""
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print("Camera matrix : \n")
print(mtx)
print("dist : \n")
print(dist)
print("rvecs : \n")
print(rvecs)
print("tvecs : \n")
print(tvecs)

