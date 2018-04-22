class Glower {

  PVector pos; 
  PVector vel;
  int hue;
  int lifetime;

  boolean gone;

  Glower(PVector p, PVector v, int h) {
    pos = p;
    vel = v;
    hue = h;

    gone = false;
  }


  void update() {
    vel.add(new PVector(0, 0.01));
    pos.add(vel);

    float angle = PVector.angleBetween(vel, new PVector(0, 1));
    if (angle < PI/24) gone = true;
    lifetime++;
  }


  void display() {
    noStroke();
    fill(hue, 100, 100, map(lifetime, 0, 150, 100, 0));
    ellipse(pos.x, pos.y, 2, 2);
  }
}