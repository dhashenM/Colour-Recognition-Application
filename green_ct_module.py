import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

#defining the colour range
lower = np.array([38, 150, 20])
upper = np.array([79, 255, 255])

#creating a loop to display live video feed from a bunch of real time images
while True:
    #obtaining a frame from the camera
    _, frame = cap.read()

    #converting the taken frame to hsv
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #creating a mask object to find and seperate the colour we want from the original image
    mask = cv2.inRange(hsv_frame, lower, upper)

    #defining the object contours
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #checking to see if there are any contours of the specified colour and enclosing a rectangle around it
    if len(contours) != 0:
        for contour in contours:
            #to make sure there are no single dots that are detected
            if cv2.contourArea(contour) > 500:
                #this is to obtain the coordinates and the measurements of the rectangle of the contour that encloses the colour
                x, y, w, h = cv2.boundingRect(contour)
                #this to to actually draw the rectangle, to be displayed, around the colour
                cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 0, 255), 2)

    #showing the image that we specify
    #cv2.imshow("mask", mask)
    cv2.imshow("webcam", frame)

    #keeping the image on hold and adding a break to exit
    key = cv2.waitKey(1)
    if key == 27:
        break