from BaseCircle import BaseCircle
from LissajousFigure import LissajousCurve


sqsize = 100
sizeScalar = 0.85
speedScalar = 0.015
colors = [0xFFFF00, 0x00FF00, 0x3124FF, 0xFF69B4, 0xFF0000]

baseCirclesX = []
baseCirclesY = []
lissajous = []

def setup():   
    size(600, 400)
    
    # Init circles
    for i in range(1, width / sqsize):
        baseCirclesX.append(BaseCircle(i * sqsize, 0, sqsize*sizeScalar, i * speedScalar, colors[i-1], True))
    for j in range(1, height / sqsize):
        baseCirclesY.append(BaseCircle(0, j * sqsize, sqsize*sizeScalar, j * speedScalar, colors[j-1], False))
    
    # Init curves
    for i in range(1, width / sqsize):
        for j in range(1, height / sqsize):
            lissajous.append(LissajousCurve(i * sqsize, j * sqsize, sqsize*sizeScalar, (baseCirclesX[i-1], baseCirclesY[j-1])))

    smooth()        
    
def draw():
    background(10)
    translate(sqsize >> 1, sqsize >> 1)
    
    # Draw the circles as orientation (basically the header of the table)
    for circle in baseCirclesX + baseCirclesY:
        circle.update()
        circle.draw()
    
    # Draw figures - calcDone describes whether new coordinates need to be calculated, or if the curve is now repeating itself
    calcDone = baseCirclesX[0].speed * frameCount > TWO_PI and baseCirclesX[1].speed * frameCount > TWO_PI
    for lissa in lissajous:
        lissa.update(calcDone)
        lissa.draw()

    
    
        
