import numpy as np
import cv2
from driver import driver

car = driver()

cap = cv2.VideoCapture(1)

fourcc =cv2.VideoWriter_fourcc(*'XVID')
out =cv2.VideoWriter('/home/pi/Code/video8.avi',fourcc,20.0,(640,480))

i = 0
while(cap.isOpened()):
    ret,frame=cap.read()
    #car.set_speed(5, 5)
    if ret==True:
        out.write(frame)
        #cv2.imwrite('%d'%(i)+".jpg",frame)
        cv2.imshow('frame',frame) 
        if cv2.waitKey(100) &0xff==ord('q'):
            break      
    else:
        break
    i = i + 1
    
cap.release()
out.release()
cv2.destroyAllWindows()