
def _notInList(newObject, detectedObjects, thresholdDist):
    """
    Calculates the Euclidean distance of a new match from all previous matches.
    If the distance is smaller than the threshold, returns False otherwise
    returns True.
    """
    import math

    for detectedObject in detectedObjects:
        if math.hypot(
                newObject[0] - detectedObject[0],
                newObject[1] - detectedObject[1]) < thresholdDist:
            return False
    return True


def highlight_cards(screenshot,
                    template,
                    color="green",
                    threshold=0.8,
                    thresholdDist=30):
    """Identifies any instances of a template image within a larger screenshot.

    Args:
        screenshot: This is the image to search
        template: The image that you're looking for within screenshot
        color: The color of the box you want to draw. Defaults to "green".
        threshold: How good a match is required for a box to be draw. Defaults to 0.8.
        thresholdDist: The minimum Euclidean distance between matches for them to be considered as a new card. Defaults to 30.
    """

    # Import needed packages
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt
    import math

    # Convert screenshot to grey and crop
    gray_img = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)[0:630, 0:950]

    # Set the color we'll use for the box
    if color == "blue":
        box_color = (255, 0, 0)
    elif color == "red":
        box_color = (0, 0, 255)
    else:
        box_color = (0, 255, 0)

    # Get the cards dimensions
    w, h = template.shape[::-1]

    # Search for matches of the template in the cropped image
    res = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    # Create an empty list for valid cards
    detectedObjects = []

    # Append every card which is further than thresholdDist
    # Draw a box on the original image showing the location of each card
    for new_object in zip(*loc[::-1]):
        if len(detectedObjects) == 0 or _notInList(new_object, detectedObjects, thresholdDist):
            detectedObjects.append(new_object)
            cv2.rectangle(screenshot,
                          new_object,
                          (new_object[0] + w, new_object[1] + h),
                          box_color, 2)

    # Save the result
    return screenshot
