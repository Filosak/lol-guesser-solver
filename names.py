import json
import time
import pyautogui
import keyboard
import numpy as np
import pytesseract
import cv2 as cv
from PIL import Image
from PIL import ImageGrab
from find import find_ability

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract.exe'

# variables
find_ab = find_ability()
json_data = json.load(open("projekt/data.json"))
binding_box = find_ab.find_spell_name()
spells_keys = ["Q", "W", "E", "R", "P"]
data = {}
fails = 0



for key in sorted(json_data["keys"].values()):
    name = json_data["data"][key]["name"]

    for i, spell in enumerate(json_data["data"][key]["spells"]):
        data[spell["name"].lower().replace(" ", "").replace("\n", "").replace(".", "").replace(":", "").replace("!", "")] = [name, spells_keys[i]]
    
    data[json_data["data"][key]["passive"]["name"].lower().replace(" ", "").replace("\n", "").replace(".", "").replace(":", "").replace("!", "")] = [name, spells_keys[-1]]



def click(pos):
    pyautogui.click(x=pos[0], y=pos[1])

for d in data:
    print(d, data[d])

Q_pos = find_ab.find_Q()
W_pos = find_ab.find_W()
E_pos = find_ab.find_E()
R_pos = find_ab.find_R()
P_pos = find_ab.find_P()

play_pos = find_ab.find_play()
input_pos = find_ab.find_input()



click(play_pos)

while True:
    img = ImageGrab.grab(bbox=binding_box)
    img_np = cv.cvtColor(np.array(img), cv.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(img_np).lower().replace(" ", "").replace("\n", "").replace(".", "").replace(":", "").replace("!", "")

    if keyboard.is_pressed('esc'):
        break
    
    print(text)  
    if text not in data:
        print("not in data")
    else:
        champ, key = data[text]
        print(data[text])

    click(input_pos)
    pyautogui.write(champ)

    if key == "Q":
        click(Q_pos)
    elif key == "W":
        click(W_pos)
    elif key == "E":
        click(E_pos)
    elif key == "R":
        click(R_pos)
    elif key == "P":
        click(P_pos)

    time.sleep(0.2)