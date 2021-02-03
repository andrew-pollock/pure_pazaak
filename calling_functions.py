

import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
import count_cards_func


video_screenshot = cv2.imread('screens/screen2.jpg')

card_template = cv2.imread('screens/example_card.jpg', 0)

count_cards_func.count_cards(
    screenshot=video_screenshot,
    template=card_template,
    output_location="results/example.png")

count_cards_func.count_cards(
    screenshot=video_screenshot,
    template=card_template,
    threshold=0.7,
    output_location="results/example_point7.png")
