import cv2 as cv

capture = cv.VideoCapture("Resources/dog.mp4")
# cv.videoCapture(0) -> uses video camera connected to PC

# use while loop to read video frame by frame
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video Window', frame)

    if cv.waitKey(20) & 0xFF == ord('d'): # closes window when u click 'd'
        break

capture.release()
cv.destroyAllWindows()

'''
-215 Assertion Error: cv2 couldn't find video, most likely that path is wrong
'''