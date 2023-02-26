import cv2 as cv
import numpy as np
import json
import time
import pyautogui
import keyboard
from PIL import ImageGrab
from find import find_ability

json_data = json.load(open("projekt/item.json"))
data = []
find_ab = find_ability()

h_bins = 50
s_bins = 60
histSize = [h_bins, s_bins]
h_ranges = [0, 180]
s_ranges = [0, 256]
ranges = h_ranges + s_ranges
channels = [0, 1]


def click(pos):
    pyautogui.click(x=pos[0], y=pos[1])


for key in json_data["data"]:
    # getting the picture
    curr_img = cv.imread(f"projekt/item/{json_data['data'][key]['image']['full']}")
    colored_curr_img = cv.cvtColor(curr_img, cv.COLOR_BGR2HSV)

    # converting picture to histogram
    hist_curr_img = cv.calcHist([colored_curr_img], channels, None, histSize, ranges, accumulate=False)
    cv.normalize(hist_curr_img, hist_curr_img, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

    # appending it to the list of all histograms
    data.append([hist_curr_img, json_data["data"][key]["name"]])


binding_box = find_ab.find()
submit_pos = find_ab.find_submit()
play_pos = find_ab.find_play()
input_pos = find_ab.find_input()


click(play_pos)

while True:
    click(input_pos)

    source_img = ImageGrab.grab(bbox=binding_box)
    source_img_np = np.array(source_img)

    converted_img = cv.cvtColor(source_img_np, cv.COLOR_RGB2BGR)
    colored_source = cv.cvtColor(converted_img, cv.COLOR_BGR2HSV)

    hist_source = cv.calcHist([colored_source], channels, None, histSize, ranges, accumulate=False)
    cv.normalize(hist_source, hist_source, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

    final = [0, None, None]

    for hist, name in data:
        curr_num = cv.compareHist(hist, hist_source, cv.HISTCMP_CORREL)

        if curr_num > final[0]:
            final = [curr_num, name]


    pyautogui.write(final[1])

    time.sleep(0.5)

    click(submit_pos)

    if keyboard.is_pressed('esc'):
        break