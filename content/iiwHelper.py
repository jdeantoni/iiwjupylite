import matplotlib.pyplot as plotLib


#This function takes a list of Point2D as parameter and plot them by using the matplotlib module
def display2DPoints(lstPoint: list):
    xSet: list =[]
    ySet: list = []
    for p in lstPoint:
        xSet = xSet + [p.x]
        ySet = ySet + [p.y]    
    plotLib.plot(xSet, ySet, marker='.',  color = "red")
    plotLib.show()
