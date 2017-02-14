ArrayList<Ball> _balls;
ArrayList<Line> _lines;
PVector _gravity;

PVector _spawn;

void setup() {
  size(600, 400);
  
  _spawn = new PVector(10, 200);
  _balls = new ArrayList<Ball>();
  _lines = new ArrayList<Line>();
  _gravity = new PVector(0, 0.2);
}


int _tickcount = 0;
void draw() {
  _tickcount++;
  
  if (_tickcount % 60 == 0) {
    _balls.add(new Ball(_spawn.x, _spawn.y));
  } 
  
  
  background(0);
  
  stroke(255);
  noFill();
  ellipse(_spawn.x, _spawn.y, 8, 8);
  
  for (Line l : _lines) {
    
    for (Ball b : _balls) {
      if (b.bounce_cooldown == 0 && l.touchesBall(b)) {
        //Split vel in two vectors (parallel to line and orthogonal to line)
        PVector par = l.dir();
        float scl = par.dot(b.vel) / par.dot(par);       
        PVector orth = b.vel.copy().sub(par.mult(scl));
        
        //Set new vel (by inverting the orthogonal one)        
        b.vel = par.add(orth.mult(-0.9));
        b.bounce_cooldown = 20;
      }
    }
    
    l.display();
  }  
  
  
  for (Ball b : _balls) {
    b.applyForce(_gravity);
    b.update();
    b.display();
  }
  
  
  if (_start != null) {
    noStroke();
    fill(255);
    rect(_start.x - 2, _start.y - 2, 4, 4);
  }
}



PVector _start;

void mouseClicked() {
  if (mouseButton == RIGHT) {
    _spawn = new PVector(mouseX, mouseY);  
  }
  else if (_start != null) {
    _lines.add(new Line(_start.x, _start.y, mouseX, mouseY));
    _start = null;
  }
  else {
    _start = new PVector(mouseX, mouseY);
  }
}