import cv2
import matplotlib.pyplot as plt
from PIL import Image
import os


def showImage(path)
    img = cv2.imread(path)
    # Remember, opencv by default reads images in BGR rather than RGB
    # So we fix that by the following
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imwrite(".temp.png",img) 
    img2 = Image.open(".temp.png")
    img2.show()
    os.remove(".temp.png") 
    
