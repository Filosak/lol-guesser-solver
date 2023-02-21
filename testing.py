from PIL import ImageGrab
import numpy as np
import cv2
from find import find_ability


pos = find_ability.find_Q()
print("Q: ", pos)

img = ImageGrab.grab(bbox=pos)
img_np = np.array(img)
img_np_c = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

cv2.imshow("test", img_np_c)
cv2.waitKey(0)


pos = find_ability.find_W()
print("W: ", pos)

img = ImageGrab.grab(bbox=pos)
img_np = np.array(img)
img_np_c = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

cv2.imshow("test", img_np_c)
cv2.waitKey(0)


pos = find_ability.find_E()
print("E: ", pos)

img = ImageGrab.grab(bbox=pos)
img_np = np.array(img)
img_np_c = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

cv2.imshow("test", img_np_c)
cv2.waitKey(0)


pos = find_ability.find_R()
print("R: ", pos)

img = ImageGrab.grab(bbox=pos)
img_np = np.array(img)
img_np_c = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

cv2.imshow("test", img_np_c)
cv2.waitKey(0)


pos = find_ability.find_play()
print("play: ", pos)

img = ImageGrab.grab(bbox=pos)
img_np = np.array(img)
img_np_c = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

cv2.imshow("test", img_np_c)
cv2.waitKey(0)







cv2.destroyAllWindows()