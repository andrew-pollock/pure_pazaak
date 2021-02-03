

import cv2
import math
import highlight_yellows

vidcap = cv2.VideoCapture('clip/example_clip.mp4')

card_template = cv2.imread('screens/example_card.jpg', 0)

success = True
while success:

    success, image = vidcap.read()
    highlight_yellows.count_cards(image, card_template, threshold=0.65)

    cv2.imshow('my_image', image)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

vidcap.release()
cv2.destroyAllWindows()


# waitKeys
# 0 = still immage
# 1 = super quick
# 50 = half speed?
