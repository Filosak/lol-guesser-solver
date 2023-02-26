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