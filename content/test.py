import helperIIW

img = helperIIW.PPMImage(2,2,[helperIIW.Pixel(255,255,255),helperIIW.Pixel(),helperIIW.Pixel(),helperIIW.Pixel(255,255,255)])

img = helperIIW.loadImage("pict/miniDamier.ppm")

for p in img.pixels:
    if p.r == 255:
        p.r = 0
        
print(img)
print(len(img.pixels))

helperIIW.saveImage(img,'pict/modified/miniDamier.ppm')


#fichierSource = open("données.iiw")
#for ligne in fichierSource :
     #print(int(ligne)*2)
#fichierSource.close()

