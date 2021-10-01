CRADIUS = 15
WINDOW = (800, 800)


def settings():
    global GRIDSIZE, CELLSIZE
    GRIDSIZE = (CRADIUS * 2 + 5, CRADIUS * 2 + 5)
    CELLSIZE = WINDOW[0] // GRIDSIZE[0]
    size(GRIDSIZE[0] * CELLSIZE, GRIDSIZE[1] * CELLSIZE)  # adapt window size to fit cells
    

def setup():
    draw_grid()
    draw_circle()
    myFont = createFont("Source Code Pro", CELLSIZE)
    textFont(myFont)
    text(str(CRADIUS), 0, CELLSIZE-1)
    noLoop()
    # save('circle.jpg')
    
    
def draw_grid():
    background(245)
    
    for i in range(1, GRIDSIZE[0]):
        stroke(200 if i % 5 == 0 else 230)
        x = i * CELLSIZE
        line(x, 0, x, height)
        
    for j in range(1, GRIDSIZE[1]):
        stroke(200 if j % 5 == 0 else 230)
        y = j * CELLSIZE
        line(0, y, width, y)
        

def draw_circle():
    # center
    center = (GRIDSIZE[0] // 2, GRIDSIZE[1] // 2)
    fill(255, 0, 0)
    stroke(100, 0, 0)
    fill_rect(*center)

    start = (center[0] + CRADIUS, center[1])
    last_cell = start
    
    fill(55)
    stroke(25)
    fill_rect(*last_cell)

    while True:
        neighbors = moore(*last_cell)
        poss_neighbors = [n for n in neighbors if is_in_front_ccw(center, last_cell, n)]
        if start in poss_neighbors: break
        
        distances = [(n, distance(center, n)) for n in poss_neighbors]
        best = sorted(distances, key=lambda d: abs(CRADIUS-d[1]))[0][0]
        fill_rect(*best)
    
        last_cell = best
           

def moore(i, j):
    neighbors = []
    if i != 0: neighbors.append((i-1, j))            # left
    if i != width-1: neighbors.append((i+1, j))      # right 
    if j != 0: neighbors.append((i, j-1))            # top 
    if j != height-1: neighbors.append((i, j+1))     # bottom 
    
    if i != 0 and j != 0 : neighbors.append((i-1, j-1))              # top left
    if i != 0 and j != height-1 : neighbors.append((i-1, j+1))       # bottom left
    if i != width-1 and j != 0 : neighbors.append((i+1, j-1))        # top right
    if i != width-1 and j != height-1 : neighbors.append((i+1, j+1)) # bottom right

    return neighbors


def is_in_front_ccw(center, p1, p2):
    v1 = (p1[0] - center[0], p1[1] - center[1])
    v2 = (p2[0] - center[0], p2[1] - center[1])    
    # z-entry of cross product, if negative it means v2 is left of v1 (ccw)
    c3 = v1[0]*v2[1] - v1[1]*v2[0]
    return c3 < 0

def distance(center, pt):
    v = (pt[0] - center[0], pt[1] - center[1])
    return sqrt(v[0]*v[0] + v[1]*v[1])


def fill_rect(i, j):
    sw = CELLSIZE * 0.1
    strokeWeight(sw)
    rect(i*CELLSIZE + sw//2, j*CELLSIZE + sw//2, CELLSIZE - sw + 1, CELLSIZE - sw + 1)
