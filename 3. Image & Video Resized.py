import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale) # frame.shape[1] is width
    height = int(frame.shape[0] * scale) # frame.shape[0] is height
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# resize image

img = cv.imread("Resources/test.jpeg")
resized_image = rescaleFrame(img, scale=10)
cv.imshow("Image", img)
cv.imshow("Resized image", resized_image)
cv.waitKey(0)

# resize video
capture = cv.VideoCapture("Resources/dog.mp4")

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.2) # scale = 0.5 is same size, 0.2 is smaller window and 0.7 is larger
    cv.imshow('Video Window', frame)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'): # closes window when u click 'd'
        break

capture.release()
cv.destroyAllWindows()
