
## Count all the cards on screen
import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

# Load in a screenshot
img_rgb = cv2.imread('screens/screen2.jpg')
# Convert it to grey
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# Load in the card I want to match
template = cv2.imread('screens/example_card.jpg',0)
# Get the cards dimensions
w, h = template.shape[::-1]

# Crop the image to just the pazaak area
cropped_img = img_gray[0:630 , 0:950]

# Search for matches of the template in the cropped image
res = cv2.matchTemplate(cropped_img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where( res >= threshold)

# Create an empty list for valid cards
detectedObjects=[]
# Set the threshold for how far apart cards must be
thresholdDist=30

# Define a function which excludes a new point if it's too close to an existing card
def notInList(newObject):
    for detectedObject in detectedObjects:
        if math.hypot(newObject[0]-detectedObject[0],newObject[1]-detectedObject[1]) < thresholdDist:
            return False
    return True

# Append every card which passes the above criteria to my list
# Draw a box on the original image showing the location of each card
for pt in zip(*loc[::-1]):
    if len(detectedObjects) == 0 or notInList(pt):
        detectedObjects.append(pt)
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv2.imwrite('res.png',img_rgb)

