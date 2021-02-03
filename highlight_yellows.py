
def count_cards(screenshot, template, threshold = 0.8):
    
    # Import needed packages
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt
    import math

    # Convert screenshot to grey and crop
    gray_img = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)[0:630 , 0:950]
    #cropped_img = gray_img[0:630 , 0:950]

    # Get the cards dimensions
    w, h = template.shape[::-1]

    # Search for matches of the template in the cropped image
    res = cv2.matchTemplate(gray_img,template,cv2.TM_CCOEFF_NORMED)
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
            cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    
    # Save the result
    return screenshot

