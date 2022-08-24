import time
import numpy as np
import cv2
from mss import mss
# from PIL import Image

region = {'top': 100, 'left': 0, 'width': 400, 'height': 300}

sct = mss()

while True:
    print(time.time())
    last_time = time.time()

    sct_img = sct.grab(region)
    img = np.array(sct_img)
    cv2.imshow('screen', img)

    print("fps: {}".format(1 / (time.time() - last_time)))

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
