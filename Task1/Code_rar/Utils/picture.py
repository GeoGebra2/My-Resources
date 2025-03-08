import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)        #打开摄像头

# threshold = 0.5
last_time = 0
i = 1
while(1):
    # get a frame
    ret, frame = cap.read()
#     frame = cv2.undistort(frame, intrinsicMat, distortionCoe, None, intrinsicMat)
    # show a frame
    cv2.imshow("capture", frame)     #生成摄像头窗口
    cv2.waitKey(1)
    now_time = time.time()
    if cv2.waitKey(1) & 0xFF == ord('q'):   #如果按下q 就截图保存并退出            
        break
    # elif now_time - last_time >= 5:
    else:
        Img_Name = "/home/pi/Code/pic/" + str(i) + ".jpg"
        i += 1
        cv2.imwrite(Img_Name, frame)
        last_time = now_time
 
cap.release()
cv2.destroyAllWindows()