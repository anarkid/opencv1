#import opencv
import cv2

#declare cap to camera under inheritance of opencv
cap = cv2.VideoCapture(0)

#while running
while True:
    #read data from camera
    success, img = cap.read()

    #show data from camera
    cv2.imshow("Image", img)
    #dont close
    cv2.waitKey(1)

