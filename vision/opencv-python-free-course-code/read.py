import cv2 as cv
from pathlib import Path

# read an img as a matrix

script_dir = Path(__file__).parent

# img_path = str(script_dir / "photos" / "lena.png")

# img = cv.imread(img_path)

# # display img as a new window
# cv.imshow(
#     "cat", # name of the window
#     img # image
# )

# wait an infinite amount of time for a keyboard key to be pressed
# cv.waitKey(0) # wait 0 seconds


# --------------------
# READ A VIDEO

# capture = cv.VideoCapture(0) # webcam (0 first camera)
capture = cv.VideoCapture(0) # webcam (0 first camera)

while True:
    # read the video frame by frame
    isTrue, frame = capture.read()

    cv.imshow('video',frame)

    # breaking the loop: if the letter 'd' is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release() # release the capture pointer
cv.destroyAllWindows()
