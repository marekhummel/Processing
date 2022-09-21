import sys

WINDOW = 800
RANGE = 3
ANGLE = radians(-30)
STOP_UPDATE = False

colors = [
    color(255, 100, 100),
    color(100, 255, 100),    
    color(100, 100, 255),
    color(255, 255, 100),
    color(255, 100, 255),
    color(100, 255, 255)
]

def setup():
    global SCALE
    SCALE = float(WINDOW / (2 * RANGE))
    
    size(WINDOW, WINDOW)
    ellipseMode(RADIUS)
    textAlign(CENTER, CENTER)
    noStroke()

def draw():
    scale(SCALE)
    translate(RANGE, RANGE)
    
    grid()
    mainline()
    trigs()
    labels()

    
def mouseMoved():
    if not STOP_UPDATE:
        global ANGLE
        ANGLE = atan2(mouseY - height / 2, mouseX - width / 2)

def mouseClicked():
    global STOP_UPDATE, ANGLE
    STOP_UPDATE = not STOP_UPDATE
    mouseMoved()

def grid():
    background(20)
    strokeWeight(1 / SCALE)
    stroke(50)
    for i in range(int(4 * RANGE)):
        xy = (-RANGE + i * 0.5)
        line(-RANGE, xy, RANGE, xy)
        line(xy, -RANGE, xy, RANGE)
    
    stroke(150)
    line(-RANGE, 0, RANGE, 0)
    line(0, -RANGE, 0, RANGE)
    
    noFill()
    stroke(255)
    strokeWeight(3 / SCALE)
    circle(0, 0, 1)
    

def mainline():
    pushMatrix()
    stroke(255)
    strokeWeight(2 / SCALE)
    rotate(ANGLE)
    line(0, 0, 2 * RANGE, 0)
    popMatrix()
    

def trigs():
    cosa, sina = cos(ANGLE), sin(ANGLE)
    seca = 1 / cosa if cosa != 0 else 500 * RANGE
    csca = 1 / sina if sina != 0 else 500 * RANGE
    
    # cos sin tan cot csc sec
    lines = [
        (cosa, 0, cosa, sina),
        (0, sina, cosa, sina),
        (cosa, sina, seca, 0),
        (cosa, sina, 0, csca),
        (0, 0, 0, csca),   
        (0, 0, seca, 0)
    ]

    for c, l in zip(colors, lines):
        stroke(c)
        line(*l)
    
    noStroke()
    fill(255)
    circle(0, 0, 3 / SCALE)
    circle(cosa, sina, 3 / SCALE)
    
    
def labels():
    # Manual scaling due to text size
    scale(1 / SCALE)
    
    # Values
    cosa, sina = cos(ANGLE) * SCALE, sin(ANGLE) * SCALE
    seca = (1 / cos(ANGLE) if cosa != 0 else RANGE) * SCALE
    csca = (1 / sin(ANGLE) if sina != 0 else RANGE) * SCALE
    halfway = RANGE * SCALE // 2
    clamp_halfway = lambda val: max(-halfway, min(val, halfway))    
        
    # cos sin tan cot csc sec
    labels = [
        ("sin", cosa - 15, sina // 2),
        ("cos", cosa // 2, sina + 6),
        ("tan", clamp_halfway((cosa + seca) // 2) + 20, sina // 2 + 6),
        ("cot", cosa // 2 + 20, clamp_halfway((sina + csca) // 2 + 6)),
        ("csc", -15, clamp_halfway(csca // 2)),
        ("sec", clamp_halfway(seca // 2), 6)
    ]

    for c, l in zip(colors, labels):
        fill(c)
        text(*l)
        
