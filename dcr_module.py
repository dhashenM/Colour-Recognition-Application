import cv2
import numpy as np
import webcolors

#defining a function to find the approximate color name from the color value
def closest_color(rgb):
    differences = {}
    #converting the hexa decimal format of the color to the RGB fromat so that the function can take RGB values 
    for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
        r, g, b = webcolors.hex_to_rgb(color_hex)
        #calculating the differences between the true rgb value and the realistic rgb value that is input,
        #squaring the differences between those numbers, adding them all up together and obtaining a list in which
        #all the differences are present as keys and the names as the values
        #using this, we can take the smallest key to get the respective color name which gives us the closest color
        differences[sum([(r - rgb[0]) ** 2,
                         (g - rgb[1]) ** 2,
                          (b - rgb[2]) ** 2])] = color_name
        
    return differences[min(differences.keys())]

#defining the camera and setting the screen resolution
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

#displaying a real time video of the field of view of the camera
while True:
    #reading a frame image from the web camera
    _, frame = cap.read()

    #displaying a series of camera images(as a video)
    cv2.imshow("Frame", frame)

    #keeping the image on hold and adding a function to execute and a break to exit
    key = cv2.waitKey(1)
    if key == 32:

        height, width, _ = np.shape(frame)

        #creating a function to create a bar with the dominant colours of the image along with their values
        def create_bar(height, width, color):
            bar = np.zeros((height, width, 3), np.uint8)
            bar[:] = color
            red, green, blue = int(color[2]), int(color[1]), int(color[0])

            return bar, (red, green, blue)
        
            
        
        #reshaping the image data to get all the pixels and having 3 colour channels
        data = np.reshape(frame, (height * width, 3))
        #converting all data to float type to conduct all calculations
        data = np.float32(data)
        #defining how many colour clusters we want
        number_clusters = 15
        #defining algorithm termination criteria, meaning the minimum search window it can process on, along with the maximum number of iterations it will take
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TermCriteria_MAX_ITER, 10, 1.0)
        #defining how the image is read with the method always starting with a random set of initial samples and trying to converge from there
        flags = cv2.KMEANS_RANDOM_CENTERS
        #use of k-means functions
        compactness, labels, centers = cv2.kmeans(data, number_clusters, None, criteria, 10, flags)

        font = cv2.FONT_HERSHEY_SIMPLEX
        bars = []
        rgb_values = []

        # with the use of enumerate, looping throught the calculated centers where dominant colours are and add it to the bars list, also adding rgb values to the rgb values list
        for index, row in enumerate(centers):
            bar, rgb = create_bar(200, 200, row)
            bars.append(bar)
            rgb_values.append(rgb)

        #creating the image bar and stacking all the colour values horizontally in a bar
        img_bar = np.hstack(bars)

        #looping throught the list of the rgb values using enumerate and adding that colour's rgb value text on the image bar
        for index, row in enumerate(rgb_values):
            
            #converting the rgb values to the color names
            try:
                cname = webcolors.rgb_to_name(row)

            except ValueError:
                cname = closest_color(row) 
            
            #displaying the color names for each dominant color displayed
            image = cv2.putText(img_bar, f'{index + 1}. {cname} ', (5 + 200 * index, 200 - 10),
                                font, 0.7, (255, 0, 0), 1, cv2.LINE_AA)
            
            print(f'{index + 1}. RGB: {row}, Colour: {cname}')
            

        #showing the image and the dominant colours of that image in the bar
        cv2.imshow("Frame", frame)
        cv2.imshow('Dominant colors', img_bar)

        cv2.waitKey(0)

    elif key == 27:    
        break

#closing the camera and all open windows
cap.release()
cv2.destroyAllWindows()


