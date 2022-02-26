class Invader {
  
  float x, y, r;
  boolean dead;
  
  
  Invader(float x_, float y_, float _r) {
    x = x_;
    y = y_;
    r = _r;
    
    dead = false;
  }
  
  
  
  void move(float xoff, float yoff) {
     x += xoff;
     y += yoff;
  }
  
  
  
  void display() {
    if (dead) { return; }
    
    stroke(0, 220, 0);
    fill(0, 200, 0);
    ellipse(x, y, r, r);  
  }
  
 


}