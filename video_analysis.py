
import cv2
import math
from purepazaak import *

yellow_template = cv2.imread('screens/example_card.jpg', 0)
blue_template = cv2.imread('screens/example_plus5.jpg', 0)

# I'm not sure what this is doing?
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Set where the altered video will be saved to
out = cv2.VideoWriter('output.avi', fourcc, fps=30.0, frameSize=(1280, 720))

vidcap = cv2.VideoCapture('clip/example_clip.mp4')
success = True
while success:

    success, image = vidcap.read()
    highlight_cards(image, yellow_template, color="green", threshold=0.65)
    highlight_cards(image, blue_template, color="blue", threshold=0.65)

    out.write(image)
    cv2.imshow('my_image', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vidcap.release()
out.release()
cv2.destroyAllWindows()


# waitKeys
# 0 = still immage
# 1 = super quick
# 50 = half speed?
