class Obstacle {

  float x, y;
  float w, h;
  
  Obstacle(float x_, float y_, float w_, float h_) {
    x = x_;
    y = y_;
    w = w_;
    h = h_;
  }

  boolean hit(PVector p) {
    return (p.x < x+w/2 && p.x > x-w/2 && p.y < y+h/2 && p.y > y-h/2);
  }

  void display() {
    fill(255, 100);
    strokeWeight(3);
    stroke(255);
    rect(x, y, w, h);
  }

}