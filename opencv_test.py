
import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

img = cv2.imread('screens/screen1.jpg',0)
img2 = img.copy()
template = cv2.imread('screens/example_card.jpg',0)
w, h = template.shape[::-1]


# Reset the image from the copy
img = img2.copy()
method = cv2.TM_CCORR

# Apply template Matching
res = cv2.matchTemplate(img,template,method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img,top_left, bottom_right, 255, 2)

plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.subtitle(meth)

plt.show()



img_rgb = cv2.imread('screens/screen2.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('screens/example_plus5.jpg',0)
w, h = template.shape[::-1]


res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.6
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imwrite('res.png',img_rgb)





img_rgb = cv2.imread('screens/screen2.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('screens/example_card.jpg',0)
w, h = template.shape[::-1]

#new_img = img_gray[400:630 , 490:950]
new_img = img_gray[0:630 , 0:950]

res = cv2.matchTemplate(new_img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv2.imwrite('res.png',img_rgb)

0.8 catches 4 cards (all light ones)
0.7 identifies all yellow cards

len(np.where(res >= threshold)[1])




np.where(res >= threshold)[0]  # This is the height
np.where(res >= threshold)[1]  # This is the width, 

np.where(np.where(res >= threshold)[0] > 400+(0.5*h))

h
w

img_gray.shape

cv2.imshow("cropped", new_img)





def notInList(newObject):
    for detectedObject in detectedObjects:
        if math.hypot(newObject[0]-detectedObject[0],newObject[1]-detectedObject[1]) < thresholdDist:
            return False
    return True


img_rgb = cv2.imread('screens/screen2.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('screens/example_card.jpg',0)
w, h = template.shape[::-1]

new_img = img_gray[0:630 , 0:950]

res = cv2.matchTemplate(new_img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where( res >= threshold)

detectedObjects=[]
thresholdDist=30

## This works but doesn't produce the image
for pt in zip(*loc[::-1]):
    if len(detectedObjects) == 0 or notInList(pt):
        detectedObjects.append(pt)
        cellImage=img_rgb[pt[1]:pt[1]+h, pt[0]:pt[0]+w]
        cv2.imwrite("results/"+str(pt[1])+"_"+str(pt[0])+".jpg",cellImage, [int(cv2.IMWRITE_JPEG_QUALITY), 50])

detectedObjects

## This works nicely!
for pt in zip(*loc[::-1]):
    if len(detectedObjects) == 0 or notInList(pt):
        detectedObjects.append(pt)
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv2.imwrite('res.png',img_rgb)

len(detectedObjects)

cellImage
pt
cv2.imwrite()

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv2.imwrite('res.png',img_rgb)
