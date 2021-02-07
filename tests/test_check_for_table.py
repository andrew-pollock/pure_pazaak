
import cv2
from check_for_table import *

# Read the template image
template = cv2.imread('screens/pazaak_table.jpg', 0)

# Create two empty dictionary
pazaak_tables = {}
not_pazaak_tables = {}

# Read the test images into their dictionaries
for x in range(1, 3):
    pazaak_tables[x] = cv2.imread(f"tests/test_images/pazaak{x}.jpg", 1)
    not_pazaak_tables[x] = cv2.imread(f"tests/test_images/not_pazaak{x}.jpg", 1)


# Check the images of Pazaak tables all return True
for x in range(1, 3):
    assert check_for_table(screenshot=pazaak_tables[x],
                           template=template) is True, (
        f"A table wasn't found in pazaak{x}")

# Check the images that aren't Pazaak tables all return False
for x in range(1, 3):
    assert check_for_table(screenshot=not_pazaak_tables[x],
                           template=template) is False, (
        f"A table was wrongly detected in not_pazaak{x}")
