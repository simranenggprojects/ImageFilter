import cv2 # importing opencv
import numpy as np # importing numerical python

img = cv2.imread("Resources/Welcome.png")
cv2.imshow("Welcome Users!!",img)
cv2.waitKey(0)

webCam = cv2.VideoCapture(0) # starting webcam
webCam.set(10,100) # setting brightness to 100

while True: # need to have loop since webcam is live video and video is sequence of images
    success, img = webCam.read()  #success is a boolean variable which returns True if frame is grabbed and img gets img
    cv2.imshow("Hey Lovely Human, Capture Your Image by pressing 'q'",img) # display image
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #img is last image captured when pressed 'q' and cvtColor converts color space
imgBlur = cv2.GaussianBlur(img,(5,5),2)
imgCanny = cv2.Canny(cv2.GaussianBlur(imgGray,(3,3),1),35,100)
imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imgFrame = cv2.rectangle(img,(10,10),(img.shape[1]-10,img.shape[0]-10),(0,0,0),2)

image = cv2.imread("Resources/Choice.png")
cv2.imshow("Your Choices", image)
key = cv2.waitKey(0)
if key == ord('1'):
        cv2.imshow("Original Image! You are flawless! Press 'q' to exit",img)
elif key == ord('2'):
        cv2.imshow("Blur! Your personality didn't blur though! Press 'q' to exit",imgBlur)
elif key == ord('3'):
        cv2.imshow("GrayScale! Enjoy this 90's look! Press 'q' to exit",imgGray)
elif key == ord('4'):
        cv2.imshow("The Sketchy You!! Press 'q' to exit",imgCanny)
elif key == ord('5'):
        cv2.imshow("You truly look amazing!! Press 'q' to exit",imgRGB)
elif key == ord('6'):
        cv2.imshow("You look good!! Press 'q' to exit",imgFrame)
elif key == ord('q'):
    cv2.waitKey(1)
else:
    invalid = cv2.imread("Resources/Wrong.png")
    cv2.imshow("Invalid Input",invalid)
cv2.waitKey(0)

