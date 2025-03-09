# https://en.wikipedia.org/wiki/En/articles/Barnsley_fern

WINDOW_HEIGHT = 800
X_RANGE = (-2.2, 2.7)
Y_RANGE = (0, 10)
TRACE_RADIUS = 0.005
UPDATES_PER_FRAME = 500
X, Y = 0, 0

def setup():
    size(int(WINDOW_HEIGHT / (Y_RANGE[1] - Y_RANGE[0]) * (X_RANGE[1] - X_RANGE[0])), WINDOW_HEIGHT)
    
    ellipseMode(RADIUS)
    background(245)
    noStroke()
    fill(0, 100, 0, 100)
    
    frameRate(60)

    
def draw():
    translate(0, height)                       # Move origin to bottom-left
    scale(1, -1);                              # Flip Y-axis
    scale(height / (Y_RANGE[1] - Y_RANGE[0]))  # Given how the width is computed, we have scaleX == scaleY
    translate(-X_RANGE[0], 0)                  # Shift fern to fit correctly
    
    for _ in range(UPDATES_PER_FRAME):
        iterate()
    

def iterate():
    global X, Y

    r = random(1)
    if r < 0.01:
        xn = 0.0
        yn = 0.16 * Y
    elif r < 0.86:
        xn = 0.85 * X + 0.04 * Y
        yn = -0.04 * X + 0.85 * Y + 1.6
    elif r < 0.93:
        xn = 0.2 * X - 0.26 * Y
        yn = 0.23 * X + 0.22 * Y + 1.6
    else:
        xn = -0.15 * X + 0.28 * Y
        yn = 0.26 * X + 0.24 * Y + 0.44

    X, Y = xn, yn     
    circle(X, Y, 0.01)
