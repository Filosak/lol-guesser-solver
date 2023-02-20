from PIL import ImageGrab
import numpy as np
import cv2

img = ImageGrab.grab(bbox=(893.5,217.5,1005,328)) #bbox specifies specific region (bbox= x,y,width,height *starts top-left)
img_np = np.array(img) #this is the array obtained from conversion

cv2.imshow("test", img_np)
cv2.waitKey(0)
cv2.destroyAllWindows()