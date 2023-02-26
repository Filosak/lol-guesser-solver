import cv2 as cv
import numpy as np
from PIL import ImageGrab


class find_ability:
    def find_by_img(self, image):
        img = np.array(ImageGrab.grab(bbox=None))
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        w, h = image.shape[::-1]
        method = eval("cv.TM_CCOEFF")

        res = cv.matchTemplate(img,image,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0] + w, top_left[1] + h)

        return top_left, bottom_right


    def find(self):
        template = cv.imread('projekt/find_images/template.png', 0)
        top_left, bottom_right = self.find_by_img(template)
        return top_left + bottom_right
    

    def find_input(self):
        template = cv.imread('projekt/find_images/input.png', 0)

        top_left, bottom_right = self.find_by_img(template)
        final = top_left + bottom_right

        return (final[0] + final[2]) // 2, (final[1] + final[3]) // 2 

    
    def find_Q(self):
        template = cv.imread('projekt/find_images/Q.png', 0)

        top_left, bottom_right = self.find_by_img(template)
        final = top_left + bottom_right
        
        return (final[0] + final[2]) // 2, (final[1] + final[3]) // 2 
    
    def find_W(self):
        template = cv.imread('projekt/find_images/W.png', 0)

        top_left, bottom_right = self.find_by_img(template)
        final = top_left + bottom_right
        
        return (final[0] + final[2]) // 2, (final[1] + final[3]) // 2 
    
    def find_E(self):
        template = cv.imread('projekt/find_images/E.png', 0)

        top_left, bottom_right = self.find_by_img(template)
        final = top_left + bottom_right
        
        return (final[0] + final[2]) // 2, (final[1] + final[3]) // 2 
    
    def find_R(self):
        template = cv.imread('projekt/find_images/R.png', 0)

        top_left, bottom_right = self.find_by_img(template)
        final = top_left + bottom_right
        
        return (final[0] + final[2]) // 2, (final[1] + final[3]) // 2 
    
    def find_P(self):
        template = cv.imread('projekt/find_images/P.png', 0)

        top_left, bottom_right = self.find_by_img(template)
        final = top_left + bottom_right
        
        return (final[0] + final[2]) // 2, (final[1] + final[3]) // 2 

    def find_play(self):
        template = cv.imread('projekt/find_images/play.png', 0)

        top_left, bottom_right = self.find_by_img(template)
        final = top_left + bottom_right
        
        return (final[0] + final[2]) // 2, (final[1] + final[3]) // 2 
    
    def find_spell_name(self):
        template = cv.imread('projekt/find_images/spell_name.png', 0)

        top_left, bottom_right = self.find_by_img(template)
        final = top_left + bottom_right
        
        return final
    
    def find_submit(self):
        template = cv.imread('projekt/find_images/submit.png', 0)

        top_left, bottom_right = self.find_by_img(template)
        final = top_left + bottom_right
        
        return (final[0] + final[2]) // 2, (final[1] + final[3]) // 2 
    

class pictures:
    def __init__(self):
        self.h_bins = 50
        self.s_bins = 60
        self.histSize = [self.h_bins, self.s_bins]
        self.h_ranges = [0, 180]
        self.s_ranges = [0, 256]
        self.ranges = self.h_ranges + self.s_ranges
        self.channels = [0, 1]

    def image_to_hist(self, path):
        # getting picture of ability
        curr_img = cv.imread(path)
        colored_curr_img = cv.cvtColor(curr_img, cv.COLOR_BGR2HSV)

        # converting picture to histogram
        hist_curr_img = cv.calcHist([colored_curr_img], self.channels, None, self.histSize, self.ranges, accumulate=False)
        cv.normalize(hist_curr_img, hist_curr_img, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

        return hist_curr_img