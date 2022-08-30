import cv2
import matplotlib.pyplot as plt
from PIL import Image
import os

class Pixel:
    def __init__(self, theR = 0, theG = 0, theB = 0):
        self.r=theR
        self.g=theG
        self.b=theB
    def __repr__(self):
        return f'Pixel({self.r},{self.g},{self.b})'


class Image:
    def __init__(self, l, w, ps):
        self.length=l
        self.width=w
        self.pixels=ps
    def __repr__(self):
        return f'Image(\n  {self.length}x{self.width}\n  {self.pixels}\n)'



def showImage(path):
    img = cv2.imread(path)
    # Remember, opencv by default reads images in BGR rather than RGB
    # So we fix that by the following
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imwrite(".temp.png",img) 
    img2 = Image.open(".temp.png")
    img2.show()
    os.remove(".temp.png") 
    
def loadImage(path):
    allPixels = []
    f = open(path, "r")
    allLines= f.readlines()
    usefullLines = []
    for line in allLines:
        if line.startswith('#') or len(line)==0:
            None
        else:
            usefullLines.append(line)

    usefullLines = usefullLines[1:]
    dimensionsAndPixels=[]

    for line in usefullLines:
        for w in line.split():
            dimensionsAndPixels.append(w)


    length=dimensionsAndPixels[0]
    width=dimensionsAndPixels[1]
    for i in range(3,len(dimensionsAndPixels)-1,3):
        allPixels.append(Pixel(dimensionsAndPixels[i],dimensionsAndPixels[i+1],dimensionsAndPixels[i+2]))
    return Image(length,width,allPixels)



def saveImage(img,path):
    f = open(path, "w")
    f.write("P3\n")
    f.write("#created by my wonderfull app !\n")
    f.write(f'{img.length} {img.width} 255\n')
    for i in range(3,len(img.pixels)-1,3):
        f.write(img.pixels[i],img.pixels[i+1],img.pixels[i+2],"\n")



