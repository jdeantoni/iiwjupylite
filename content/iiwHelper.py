import matplotlib.pyplot as plotLib



def display(lstPoint: list):
    xSet: list =[]
    ySet: list = []
    for p in lstPoint:
        xSet = xSet + [p.x]
        ySet = ySet + [p.y]    
    plotLib.plot(xSet, ySet, marker='.',  color = "red")
    plotLib.show()
