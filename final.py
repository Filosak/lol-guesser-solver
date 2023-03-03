import cv2 as cv
import numpy as np
import json
import time
import pyautogui
import keyboard
import pytesseract
from PIL import ImageGrab
from find import find_ability, pictures


class solver:
    def __init__(self, mode, difficulty, items_path, images_path, find_images_path, passives_images_path, data_path, item_data_path, tesseract_path):
        self.mode = mode
        self.difficulty = difficulty

        self.items_p = items_path
        self.images_p = images_path
        self.find_images_p = find_images_path
        self.passives_images_p = passives_images_path

        self.data_p = data_path
        self.item_data_p = item_data_path

        self.h_bins = 50
        self.s_bins = 60
        self.histSize = [self.h_bins, self.s_bins]
        self.h_ranges = [0, 180]
        self.s_ranges = [0, 256]
        self.ranges = self.h_ranges + self.s_ranges
        self.channels = [0, 1]

        self.spells_keys = ["Q", "W", "E", "R", "P"]
        self.data = []
        self.names_data = {}


        self.Q_pos = None
        self.W_pos = None
        self.E_pos = None
        self.R_pos = None
        self.P_pos = None

        self.binding_box = None
        self.submit_pos = None
        self.play_pos = None
        self.input_pos = None

        self.json_data = None


        self.find_ab = find_ability(find_images_path)
        self.to_hist = pictures()

        pytesseract.pytesseract.tesseract_cmd = tesseract_path

    
    def load_spell_data(self, json_data):
        for key in sorted(json_data["keys"].values()):
            name = json_data["data"][key]["name"]

            # spells for champions
            for i, spell in enumerate(json_data["data"][key]["spells"]):
                hist_curr_img = self.to_hist.image_to_hist(f"{self.images_p}{spell['image']['full']}")
                self.data.append([hist_curr_img, name, self.spells_keys[i]])

                # passives
                hist_curr_img = self.to_hist.image_to_hist(f"{self.passives_images_p}{json_data['data'][key]['passive']['image']['full']}")
                self.data.append([hist_curr_img, name, self.spells_keys[-1]])


    def load_spell_names(self, json_data):
        for key in sorted(json_data["keys"].values()):
            name = json_data["data"][key]["name"]

            for i, spell in enumerate(json_data["data"][key]["spells"]):
                self.names_data[spell["name"].lower().replace(" ", "").replace("\n", "").replace(".", "").replace(":", "").replace("!", "")] = [name, self.spells_keys[i]]
            
            self.names_data[json_data["data"][key]["passive"]["name"].lower().replace(" ", "").replace("\n", "").replace(".", "").replace(":", "").replace("!", "")] = [name, self.spells_keys[-1]]


    def load_item_data(self, json_data):
        for key in json_data["data"]:
            # getting the picture
            curr_img = cv.imread(f"{self.items_p}{json_data['data'][key]['image']['full']}")
            colored_curr_img = cv.cvtColor(curr_img, cv.COLOR_BGR2HSV)

            # converting picture to histogram
            hist_curr_img = cv.calcHist([colored_curr_img], self.channels, None, self.histSize, self.ranges, accumulate=False)
            cv.normalize(hist_curr_img, hist_curr_img, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

            # appending it to the list of all histograms
            self.data.append([hist_curr_img, json_data["data"][key]["name"]])

    
    def check_possitions(self):
        self.input_pos = self.find_ab.find_input()
        self.play_pos = self.find_ab.find_play()

        if self.mode == "Normal" or self.mode == "Time":
            self.binding_box = self.find_ab.find()
            
            if self.difficulty == "Easy":
                self.submit_pos = self.find_ab.find_submit()
                return
                
            self.Q_pos = self.find_ab.find_Q()
            self.W_pos = self.find_ab.find_W()
            self.E_pos = self.find_ab.find_E()
            self.R_pos = self.find_ab.find_R()
            self.P_pos = self.find_ab.find_P()

        elif self.mode == "Items":
            self.binding_box = self.find_ab.find()
            self.submit_pos = self.find_ab.find_submit()

        elif self.mode == "Names":
            self.binding_box = self.find_ab.find_spell_name()
            
            if self.difficulty == "Easy":
                submit_pos = self.find_ab.find_submit()
                return
                
            self.Q_pos = self.find_ab.find_Q()
            self.W_pos = self.find_ab.find_W()
            self.E_pos = self.find_ab.find_E()
            self.R_pos = self.find_ab.find_R()
            self.P_pos = self.find_ab.find_P()


    def setup(self):
        self.check_possitions()

        if self.mode == "Normal" or self.mode == "Time" or self.mode == "Names":
            self.json_data = json.load(open(self.data_p))

            if self.mode == "Names":
                self.load_spell_names(self.json_data)
            else:
                self.load_spell_data(self.json_data)

        else:
            self.json_data = json.load(open(self.item_data_p))
            self.load_item_data(self.json_data)

    

    def run(self):
        self.click(self.input_pos)

        if self.mode == "Normal" or self.mode == "Time":
            self.normal()

        elif self.mode == "Names":
            self.names()
        
        elif self.mode == "Items":
            self.items()
        
        else:
            print("Wrong mode input")



    def click(self, pos):
        pyautogui.click(x=pos[0], y=pos[1])

    def click_spell(self, key):
        if key == "Q":
            self.click(self.Q_pos)
        elif key == "W":
            self.click(self.W_pos)
        elif key == "E":
            self.click(self.E_pos)
        elif key == "R":
            self.click(self.R_pos)
        elif key == "P":
            self.click(self.P_pos)

    
    def normal(self):
        source_img = ImageGrab.grab(bbox=self.binding_box)
        source_img_np = np.array(source_img)

        converted_img = cv.cvtColor(source_img_np, cv.COLOR_RGB2BGR)
        colored_source = cv.cvtColor(converted_img, cv.COLOR_BGR2HSV)

        hist_source = cv.calcHist([colored_source], self.channels, None, self.histSize, self.ranges, accumulate=False)
        cv.normalize(hist_source, hist_source, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

        final = [0, None, None]

        for hist, champ, key in self.data:
            curr_num = cv.compareHist(hist, hist_source, cv.HISTCMP_CORREL)

            if curr_num > final[0]:
                final = [curr_num, champ, key]

        pyautogui.write(final[1])
        self.click_spell(final[2])
            
    
    def names(self):
        img = ImageGrab.grab(bbox=self.binding_box)
        img_np = cv.cvtColor(np.array(img), cv.COLOR_BGR2GRAY)

        text = pytesseract.image_to_string(img_np).lower().replace(" ", "").replace("\n", "").replace(".", "").replace(":", "").replace("!", "")

        if text not in self.names_data:
            print("not in data")
        else:
            champ, key = self.names_data[text]
            print(self.names_data[text])

        pyautogui.write(champ)
        self.click_spell(key)

        time.sleep(0.2)


    def items(self):
        source_img = ImageGrab.grab(bbox=self.binding_box)
        source_img_np = np.array(source_img)

        converted_img = cv.cvtColor(source_img_np, cv.COLOR_RGB2BGR)
        colored_source = cv.cvtColor(converted_img, cv.COLOR_BGR2HSV)

        hist_source = cv.calcHist([colored_source], self.channels, None, self.histSize, self.ranges, accumulate=False)
        cv.normalize(hist_source, hist_source, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

        final = [0, None, None]

        for hist, name in self.data:
            curr_num = cv.compareHist(hist, hist_source, cv.HISTCMP_CORREL)

            if curr_num > final[0]:
                final = [curr_num, name]


        pyautogui.write(final[1])

        time.sleep(0.5)

        self.click(self.submit_pos)