import cv2
import numpy as np

#code for defining the camera and setting the screen resolution
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

#creating a loop to display live video feed from a bunch of real time images
while True:
    #obtaining a frame from the camera
    _, frame = cap.read()
    #converting the taken frame to hsv
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #flipping the video horizontally
    frame_flip = cv2.flip(frame, 1)

    #defining image shape
    height, width, _ = frame_flip.shape
    cx = int(width / 2)
    cy = int(height / 2)

    #picking the pixel value of the middle of the screen
    pixel_centre = hsv_frame[cy,cx]

    #Configuring each colour value
    hue_value = pixel_centre[0]
    sat_value = pixel_centre[1]
    val_value = pixel_centre[2]
    """
    colour = "Undefined"
    if sat_value < 30:
        colour = "WHITE"
    elif val_value < 100 and sat_value <100:
        colour = "GRAY"     
    elif val_value < 100:
        colour = "BLACK"     
    elif hue_value < 5:
        colour = "RED"
    elif hue_value < 22:
        colour = "ORANGE"
    elif hue_value < 22:
        colour = "YELLOW"
    elif hue_value < 78:
        colour = "GREEN"
    elif hue_value < 130:
        colour = "BLUE"
    elif hue_value < 170:
        colour = "VIOLET"
    else:
        colour = "BLACK"
    """

    colour = "Undefined"
    if 0 <= sat_value <= 20:
        colour = "WHITE"
    elif (70 <= val_value <= 150 and sat_value <= 90) or (60 <= val_value <= 180 and 0 <= sat_value <= 30):
        colour = "GRAY"
    elif 0 < val_value < 50:
        colour = "BLACK"  
    elif hue_value <= 5 or hue_value >= 175:
        colour = "RED"
    elif 6 <= hue_value <= 20 and 70 <= val_value <= 190:
        colour = "BROWN"
    elif 6 <= hue_value <= 20:
        colour = "ORANGE"
    elif 21 <= hue_value <= 37:
        colour = "YELLOW"
    elif 38 <= hue_value <= 79:
        colour = "GREEN"
    elif 80 <= hue_value <= 94:
        colour = "CYAN"
    elif 95 <= hue_value <= 130:
        colour = "BLUE"
    elif 131 <= hue_value <= 148:
        colour = "PURPLE"    
    elif 149 <= hue_value <= 169:
        colour = "PINK"
    else:
        colour = "BLACK"

    #D3v3l0p3r
    #dispalying the value of the colour of the selected pixel
    print(pixel_centre)

    #matching the recognized colour with the displayed text colour
    pixel_centre_bgr = frame_flip[cy, cx]
    b, g, r = int(pixel_centre_bgr[0]), int(pixel_centre_bgr[1]), int(pixel_centre_bgr[2])

    #displaying the name of the colour
    cv2.putText(frame_flip, colour,  (20, 70), 0, 2, (b, g, r), 2)

    #crosshair
    cv2.line(frame_flip, (cx+3,cy), (cx+20,cy), (0, 0, 255), 2)
    cv2.line(frame_flip, (cx-3,cy), (cx-20,cy), (0, 0, 255), 2)
    cv2.line(frame_flip, (cx,cy+3), (cx,cy+20), (0, 0, 255), 2)
    cv2.line(frame_flip, (cx,cy-3), (cx,cy-20), (0, 0, 255), 2)

    #displaying a series of camera images(as a video)
    cv2.imshow("Frame", frame_flip)

    #keeping the image on hold and adding a break to exit
    key = cv2.waitKey(1)
    if key == 27:
        break

#closing the camera and all open windows
cap.release()
cv2.destroyAllWindows()


