
def check_for_table(screenshot,
                    template,
                    threshold=0.8,
                    debug_mode=False):
    """Check if the pazaak table is onscreen

    Args:
        screenshot: This is the image to search
        template: An example image of the pazaak table
        threshold: How good a match is required. Defaults to 0.8.
        debug_mode: Do you want to draw a box on the image. Defaults to False.
    """

    # Import needed packages
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt
    import math

    # Convert screenshot to grey
    gray_img = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Get the cards dimensions
    w, h = template.shape[::-1]

    # Search for matches of the template in the cropped image
    res = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)

    # Am I playing Pazaak?
    playing_pazaak = max_val > threshold

    # If I'm playing Pazaak and in debug mode, then plot the rectangle
    if debug_mode and playing_pazaak:
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        # Draw the rectangle (just for testing)
        cv2.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2)

    # If I'm in debug mode and not playing Pazaak, then add text
    if debug_mode and not playing_pazaak:
        cv2.putText(screenshot, 'This is not Pazaak :(',
                    org=(10, 500),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1,
                    color=(255, 255, 255),
                    lineType=2)

    # Return the boolean value
    return playing_pazaak
