
def find_scores(screenshot,
                score_template,
                threshold=0.8,
                thresholdDist=30):
    """Identifies any instances of a template image within a larger screenshot.

    Args:
        screenshot: This is the image to search
        score_template: The image that you're looking for within screenshot
        threshold: How good a match is required for a box to be draw. Defaults to 0.8.
        thresholdDist: The minimum Euclidean distance between matches for them to be considered as a new card. Defaults to 30.
    """

    res = cv2.matchTemplate(screenshot, score_template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    w, h = score_template.shape[::-1]

    detectedObjects = []

    for new_object in zip(*loc[::-1]):
        if len(detectedObjects) == 0 or _notInList(new_object, detectedObjects, thresholdDist):
            detectedObjects.append(new_object)
        if len(detectedObjects) == 2:
            break

    return detectedObjects
