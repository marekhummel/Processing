rule = "LRRRRRLLR"
speed = 100

ax = 0
ay = 0
ar = 0    # 0 1 2 3, up right down left
grid = []

def setup():
    global ax, ay, ar, grid
    size(600, 400)

    grid = [[0 for y in range(height)] for x in range(width)]
    ax = width / 2
    ay = height / 2
    
    background(245) 
    colorMode(HSB, 255, 255, 255)      
       
    
def draw():
    global ax, ay, ar, rule;
    
    loadPixels()
    for n in range(speed):
        grid[ax][ay] = (grid[ax][ay] + 1) % len(rule)
        pix = ay * width + ax
       
        h = int(255 * grid[ax][ay] / len(rule))
        pixels[pix] = color(h, 255, 255)
        
        
        # Move ant
        letter = rule[grid[ax][ay]]
        if letter == 'L': ar -= 1
        elif letter == 'R': ar += 1
        elif letter == 'U': ar += 2
        if (ar < 0) : ar += 4
        if (ar > 3) : ar -= 4
        
        if (ar == 0): ay -= 1
        elif (ar == 1): ax += 1
        elif (ar == 2): ay += 1
        elif (ar == 3): ax -= 1
    updatePixels()
