# https://www.youtube.com/watch?v=kbKtFN71Lfs

WINDOW = 800
TRACE_RADIUS = 0.5
RANDOM_TRIG = False
JUMP = 0.5

def setup():
    size(WINDOW, WINDOW)
    ellipseMode(RADIUS)
    background(245)
    noStroke()
    
    gen_triangle()
    gen_start()
    
    frameRate(2)

    
def draw():
    global TRACE, TRIG, JUMP
    
    new_trace = []
    for x, y in TRACE:
        for tx, ty in TRIG:
            nx = x + JUMP * (tx - x)
            ny = y + JUMP * (ty - y)
            new_trace.append((nx, ny))
            fill(0, 0, 0, 180)
            circle(nx, ny, TRACE_RADIUS)
    TRACE = new_trace
    
    if frameCount == 10:
        print("Stop")
        noLoop()
        
        
def gen_triangle():
    global TRIG, RANDOM_TRIG, WINDOW
    
    if not RANDOM_TRIG:
        TRIG = [(400, 100), (100, 700), (700, 700)]
        return
    
    while True:
        x1, y1 = (random(WINDOW), random(WINDOW))
        x2, y2 = (random(WINDOW), random(WINDOW))
        x3, y3 = (random(WINDOW), random(WINDOW))
        
        cx, cy = ((x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3) # centroid
        area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        target_area = 0.25 * (WINDOW * WINDOW)
        s = sqrt(target_area / area)
        
        x1, y1 = (cx + s * (x1 - cx), cy + s * (y1 - cy))
        x2, y2 = (cx + s * (x2 - cx), cy + s * (y2 - cy))
        x3, y3 = (cx + s * (x3 - cx), cy + s * (y3 - cy))
        TRIG = [(x1, y1), (x2, y2), (x3, y3)]
        
        if all(0 <= v < WINDOW for v in [x1,x2,x3,y1,y2,y3]):
            break
        
    
    print("trig found")
    fill(0)
    for tx, ty in TRIG:
        circle(tx, ty, 7)
        

def gen_start():
    global TRIG, TRACE
    
    x1, y1 = TRIG[0]
    x2, y2 = TRIG[1]
    x3, y3 = TRIG[2]
    denominator = ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3));
    while True:
        candidate = (random(WINDOW), random(WINDOW))
        x, y = candidate
        
        a = ((y2 - y3)*(x - x3) + (x3 - x2)*(y - y3)) / denominator;
        b = ((y3 - y1)*(x - x3) + (x1 - x3)*(y - y3)) / denominator;
        if a >= 0 and b >= 0 and (1-a-b) >= 0:
            TRACE = [candidate]
            fill(255, 0, 0)
            circle(candidate[0], candidate[1], TRACE_RADIUS * 3)
            print("start found")
            break
    
