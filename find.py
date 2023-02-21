import cv2 as cv
import numpy as np
from PIL import ImageGrab


class find_ability:
    def find():
        template = cv.imread('project/find_images/template.png', 0)

        img = np.array(ImageGrab.grab(bbox=None))
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        w, h = template.shape[::-1]
        method = eval("cv.TM_CCOEFF")

        res = cv.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0] + w, top_left[1] + h)

        return top_left + bottom_right
    

    def find_input():
        template = cv.imread('project/find_images/input.png', 0)

        img = np.array(ImageGrab.grab(bbox=None))
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        w, h = template.shape[::-1]
        method = eval("cv.TM_CCOEFF")

        res = cv.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0] + w, top_left[1] + h)

        final = top_left + bottom_right

        return (final[0] + final[2]) // 2, (final[1] + final[3]) // 2 

    
    def find_Q():
        template = cv.imread('project/find_images/Q.png', 0)

        img = np.array(ImageGrab.grab(bbox=None))
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        w, h = template.shape[::-1]
        method = eval("cv.TM_SQDIFF_NORMED")

        res = cv.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0] + w, top_left[1] + h)

        final = top_left + bottom_right

        return (final[0] + final[2]) // 2, (final[1] + final[3]) // 2 
    
    def find_W():
        template = cv.imread('project/find_images/W.png', 0)

        img = np.array(ImageGrab.grab(bbox=None))
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        w, h = template.shape[::-1]
        method = eval("cv.TM_SQDIFF_NORMED")

        res = cv.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0] + w, top_left[1] + h)

        final = top_left + bottom_right

        return (final[0] + final[2]) // 2, (final[1] + final[3]) // 2 
    
    def find_E():
        template = cv.imread('project/find_images/E.png', 0)

        img = np.array(ImageGrab.grab(bbox=None))
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        w, h = template.shape[::-1]
        method = eval("cv.TM_SQDIFF_NORMED")

        res = cv.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0] + w, top_left[1] + h)

        final = top_left + bottom_right

        return (final[0] + final[2]) // 2, (final[1] + final[3]) // 2 
    
    def find_R():
        template = cv.imread('project/find_images/R.png', 0)

        img = np.array(ImageGrab.grab(bbox=None))
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        w, h = template.shape[::-1]
        method = eval("cv.TM_SQDIFF_NORMED")

        res = cv.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0] + w, top_left[1] + h)

        final = top_left + bottom_right

        return (final[0] + final[2]) // 2, (final[1] + final[3]) // 2 

    
    def find_play():
        template = cv.imread('project/find_images/play.png', 0)

        img = np.array(ImageGrab.grab(bbox=None))
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        w, h = template.shape[::-1]
        method = eval("cv.TM_SQDIFF_NORMED")

        res = cv.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0] + w, top_left[1] + h)

        final = top_left + bottom_right

        return (final[0] + final[2]) // 2, (final[1] + final[3]) // 2 