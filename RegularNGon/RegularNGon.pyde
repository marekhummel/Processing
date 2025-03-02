N  = 6
DEPTH = 10

WINDOW = 800
BIG_CIRCLE_R = 0.8
CIRCLES = []

class InitPoint:
    R = 0.2
    
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.theta = random(TWO_PI)
        self.delta = random(-0.04, 0.04)
        
    def point(self):
        x = self.cx + sin(self.theta) * self.R
        y = self.cy + cos(self.theta) * self.R
        return (x, y)
        
    def draw(self):
        stroke(0, 100, 0)
        circle(self.cx, self.cy, self.R)                           
        
    def update(self):
        self.theta += self.delta
    

def setup():
    size(WINDOW, WINDOW)
    ellipseMode(RADIUS)
    setup_circles()
    
def draw():
    global CIRCLES
    
    # Center window at (0,0), edges are -1/+1
    translate(WINDOW / 2, WINDOW / 2)
    scale(WINDOW / 2)
    
    strokeWeight(0.005)
    noFill()
    
    background(245)
    for c in CIRCLES:
        c.update()
        c.draw()
    
    points = [c.point() for c in CIRCLES]    
    for i in range(DEPTH):
        points = iterate_midpoints(points, i == 0, i == DEPTH - 1)
    
    
def setup_circles():
    global CIRCLES

    CIRCLES = []
    for i in range(N):
        theta = TWO_PI * i / N
        x = sin(theta) * BIG_CIRCLE_R
        y = cos(theta) * BIG_CIRCLE_R
        CIRCLES.append(InitPoint(x, y))


def iterate_midpoints(points, outer, inner):
    points.append(points[0])
    
    r = 0.01 if (outer or inner) else 0.003
    
    col = (220, 220, 220)
    if outer:
        col = (0, 0, 0)
    elif inner:
        col = (100, 0, 0)
    
    fill(*col)
    stroke(*col)
    
    midpoints = []
    for pi, pj in zip(points, points[1:]):
        dir = (pj[0] - pi[0], pj[1] - pi[1])
        midpoint = (pi[0] + dir[0] / 2, pi[1] + dir[1] / 2)
        midpoints.append(midpoint)
        
        circle(pi[0], pi[1], r)
        line(pi[0], pi[1], pj[0], pj[1])
        
    return midpoints
    

           
