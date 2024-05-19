import cv2 as cv

img = cv.imread("Resources/test.jpeg")

cv.imshow("Display Window", img)

cv.waitKey(0) # Waits for infinite amount of time for a keyboard key to be pressed


'''
OLD CODE:

import cv2 as cv
import sys

img = cv.imread("test.jpeg")

if img is None:
    sys.exit("Couldn't read the image")

cv.imshow("Display window", img)
cv.waitKey(0) # 0 -> wait forever


Because we want our window to be displayed until the user presses a key 
(otherwise the program would end far too quickly), we use the cv::waitKey 
function whose only parameter is just how long should it wait for a user input 
(measured in milliseconds). Zero means to wait forever. The return value is the key that was pressed.



if 0xFF == ord("x"): # not working - closes the window, if any key on the keyboard is pressed
    cv.destroyAllWindows()

'''