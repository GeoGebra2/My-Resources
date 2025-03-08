import joblib
#from sklearn import datasets
#from sklearn.model_selection import train_test_split
#from sklearn import svm
#from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from PIL import Image
import numpy as np
import os
import cv2
classes = ('left', 'right','stright','pause')

clf=joblib.load('my_svm.m')
lower_blue = np.array([100, 143, 46])
upper_blue = np.array([124, 255, 255])
cap1 = cv2.VideoCapture(0)
while True:
    _, frame1 = cap1.read()
    #_, frame2 = cap2.read()

    roi = frame1[140:230,535:610]
    roi_hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    mask_flag = cv2.inRange(roi_hsv,lower_blue,upper_blue)
    print(np.sum(mask_flag == 255))
    cv2.imshow('roi',mask_flag)
    cv2.waitKey(1)
    roi = Image.fromarray(cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))
    new_image=roi

    #new_image = Image.open("./raw_data/train/pause/frame_505.jpg")
    new_image = new_image.resize((28,28))
    new_image = np.array(new_image)
    new_image = np.reshape(new_image, (new_image.shape[0]*new_image.shape[1]*new_image.shape[2]))
    new_image = preprocessing.scale(new_image)
    new_image_pred = clf.predict([new_image])
    print(new_image_pred)
    print("New Image Prediction:", new_image_pred,end=' ')
    print(classes[int(new_image_pred)])
