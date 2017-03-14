class Glower {

  PVector[] pos; 
  PVector vel;
  int hue;
  
  boolean gone;

  Glower(PVector p, PVector v, int h) {
    pos = new PVector[3];
    for (int i = 0; i < pos.length; i++) { 
      pos[i] = p;
    }
    vel = v;
    hue = h;
    
    gone = false;
  }


  void update() {
    for (int i = pos.length-1; i > 0; i--) { 
      pos[i] = pos[i-1].copy();
    }

    vel.add(new PVector(0, 0.05));
    pos[0].add(vel);
    
    float angle = PVector.angleBetween(vel, new PVector(0, 1));
    if (angle < PI/24) gone = true;
  }


  void display() {
    noStroke();
    float angle = PVector.angleBetween(vel, new PVector(0, 1));
   
    for (int i = 0; i < pos.length; i++) {
      float s = map(i, 0, pos.length-1, 2, 0);
      float a = map(i, 0, pos.length-1, angle * 100, 0);
      fill(hue, 100, 100, a);
      ellipse(pos[i].x, pos[i].y, s, s);
    }
  }
}