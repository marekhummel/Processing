n = 120
c = 90 #82
pos = []
angle = 0

def setup():
    global pos
    
    size(500, 500)
    colorMode(HSB, 180, 100, 100)
    for i in range(n):
        pos.append(PVector(width/2, height/2))
    
    
def draw():
    global pos, angle
    
    background(0)
    noStroke()
    
    x = width / 2 + cos(angle) * 150
    y = height / 2 + sin(2*angle) * 150
    l = PVector(x, y)
    for i in range(n):
        fill(180 / n * i, 90, 90)
        p = pos[i]
        v = 0.5 * (l - p)
        p.add(v)
        circle(p.x, p.y, 70)
        l = p
        
    angle += PI / c
