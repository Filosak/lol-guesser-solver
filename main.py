import cv2 as cv
import numpy as np
import json
import time
import pyautogui
import keyboard
from PIL import ImageGrab
from find import find_ability

def click(pos):
    pyautogui.click(x=pos[0], y=pos[1])

# variables
json_data = json.load(open("projekt/data.json"))
spells_keys = ["Q", "W", "E", "R", "P"]
data = []     # histogram, champ, key
find_ab = find_ability()

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
    name = json_data["data"][key]["name"]

    for i, spell in enumerate(json_data["data"][key]["spells"]):
        
        # getting picture of ability
        curr_img = cv.imread(f"projekt/images/{spell['image']['full']}")

        colored_curr_img = cv.cvtColor(curr_img, cv.COLOR_BGR2HSV)

        # converting picture to histogram
        hist_curr_img = cv.calcHist([colored_curr_img], channels, None, histSize, ranges, accumulate=False)
        cv.normalize(hist_curr_img, hist_curr_img, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

        # appending it to the list of all histograms
        data.append([hist_curr_img, name, spells_keys[i]])

    # passive
    img_path = json_data["data"][key]["passive"]["image"]["full"]
    curr_img = cv.imread(f"projekt/passives_images/{img_path}")

    colored_curr_img = cv.cvtColor(curr_img, cv.COLOR_BGR2HSV)

    # converting picture to histogram
    hist_curr_img = cv.calcHist([colored_curr_img], channels, None, histSize, ranges, accumulate=False)
    cv.normalize(hist_curr_img, hist_curr_img, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

    # appending it to the list of all histograms
    data.append([hist_curr_img, name, spells_keys[-1]])


# pos variables
Q_pos = find_ab.find_Q()
W_pos = find_ab.find_W()
E_pos = find_ab.find_E()
R_pos = find_ab.find_R()
P_pos = find_ab.find_P()

play_pos = find_ab.find_play()
input_pos = find_ab.find_input()

binding_box = find_ab.find()


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

    for hist, champ, key in data:
        curr_num = cv.compareHist(hist, hist_source, cv.HISTCMP_CORREL)

        if curr_num > final[0]:
            final = [curr_num, champ, key]

    pyautogui.write(final[1])
    
    if final[2] == "Q":
        click(Q_pos)
    elif final[2] == "W":
        click(W_pos)
    elif final[2] == "E":
        click(E_pos)
    elif final[2] == "R":
        click(R_pos)
    elif final[2] == "P":
        click(P_pos)

    # time.sleep(0.5)

    if keyboard.is_pressed('esc'):
        break