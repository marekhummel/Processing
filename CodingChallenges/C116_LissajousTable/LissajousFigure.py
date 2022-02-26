class LissajousCurve:

    
    def __init__(self, x, y, sz, base):
        self.x = x
        self.y = y
        self.size = sz
        self.base = base
        self.color = lerpColor(base[0].color, base[1].color, 0.5)
    
        self.points = [(self.base[0].dotPos()[0], self.base[1].dotPos()[1])]
        
    
    def update(self, finished):  
        # If calc is done, only rotate the point array, else add new point  
        if finished:
            self.points = self.points[1:] + self.points[0:1]
        else:    
            new = (self.base[0].dotPos()[0], self.base[1].dotPos()[1])
            self.points.append(new)
            
            
        
        
    def draw(self):
        # Transformation, so that the curves center (center of mass if u wish) is the origin and the size of the surrounding box is 2
        pushMatrix()
        translate(self.x, self.y)
        scale(self.size / 2)
        stroke(self.color >> 16, self.color >> 8 & 0xFF, self.color & 0xFF)
        strokeWeight(1 / self.size * 2)
        
        # Figure
        noFill()
        beginShape()
        for pt in self.points:
            vertex(pt[0], pt[1])
        endShape()
        
        # Dot
        fill(255)
        ellipse(self.points[-1][0], self.points[-1][1], 0.15, 0.15)      
        popMatrix()
