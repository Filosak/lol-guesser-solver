import cv2 as cv
import numpy as np
from PIL import ImageGrab
import json
import time
from find import find_ability


# variables
json_data = json.load(open("project/data.json"))
spells_keys = ["Q", "W", "E", "R"]
data = []     # histogram, champ, key

# variable - I don't know what they do :( IMPORTANT ig
h_bins = 50
s_bins = 60
histSize = [h_bins, s_bins]
h_ranges = [0, 180]
s_ranges = [0, 256]
ranges = h_ranges + s_ranges
channels = [0, 1]


# creating list of histograms of abilities and coresponding key and champion
for key in sorted(json_data["keys"].values()):
    for i, spell in enumerate(json_data["data"][key]["spells"]):
        
        # getting picture of ability
        curr_img = cv.imread(f"project/images/{spell['image']['full']}")
        print(f"project/images/{spell['image']['full']}")


        colored_curr_img = cv.cvtColor(curr_img, cv.COLOR_BGR2HSV)

        # converting picture to histogram
        hist_curr_img = cv.calcHist([colored_curr_img], channels, None, histSize, ranges, accumulate=False)
        cv.normalize(hist_curr_img, hist_curr_img, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

        # appending it to the list of all histograms
        data.append([hist_curr_img, key, spells_keys[i]])


binding_box = find_ability.find()

while True:
    source_img = ImageGrab.grab(bbox=binding_box)

    source_img_np = np.array(source_img)

    converted_img = cv.cvtColor(source_img_np, cv.COLOR_RGB2BGR)

    colored_source = cv.cvtColor(converted_img, cv.COLOR_BGR2HSV)

    hist_source = cv.calcHist([colored_source], channels, None, histSize, ranges, accumulate=False)

    cv.normalize(hist_source, hist_source, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

    final = [0, None, None]
    for hist, champ, key in data:
        curr_num = cv.compareHist(hist, hist_source, cv.HISTCMP_CORREL)

        if curr_num > final[0]:
            final = [curr_num, champ, key]

    print(final)
    





# [champion] = [key, histogram]