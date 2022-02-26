class BaseCircle:
    def __init__(self, x, y, sz, spd, col, isX):
        self.x = x
        self.y = y
        self.size = sz
        self.speed = spd
        self.color = col
        self.isX = isX
        self.angle = 0

    
    def update(self):
        # Rotate the point by increasing the angle
        self.angle = (self.angle - (self.speed)) % TWO_PI
        
    def dotPos(self):
        # Return polar coordinates from angle
        return (sin(self.angle + PI), cos(self.angle + PI))
    
    def draw(self):
        # Transformation, so that the circles center is the origin and its radius is 1
        pushMatrix()
        translate(self.x, self.y)
        scale(self.size / 2)
        stroke(self.color >> 16, self.color >> 8 & 0xFF, self.color & 0xFF)
        strokeWeight(1 / self.size * 3)
        
        # Circle
        noFill()
        ellipse(0, 0, 2, 2)
        
        # Dot
        fill(255)
        ellipse(self.dotPos()[0], self.dotPos()[1], 0.15, 0.15)      
        popMatrix()
        
        # Line
        strokeWeight(0.5)
        stroke(0xDD, 0xDD, 0xDD)
        if self.isX:
            x = self.x + self.dotPos()[0]*self.size/2
            line(x, -self.size, x, height)
        else:
            y = self.y + self.dotPos()[1]*self.size/2
            line(-self.size, y, width, y)
            
            
            
