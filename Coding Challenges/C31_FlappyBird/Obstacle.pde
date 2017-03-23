class Obstacle {

  float x;
  float top, bottom;
  float w = 40;
  boolean passed;

  Obstacle(float x_) {
    x = x_;

    float gapsize = random(100, 300);
    top = random(-height/2 + 20, height/2 - 20 - gapsize);
    bottom = top + gapsize;
  }


  boolean hit(Bird b) {   
    if (x + w/2 < 0) passed = true;

    if (x - w/2 > 0 || passed) return false;
    return b.y - b.r <= top || b.y + b.r >= bottom;
  }

  void update() {
    x -= 3;
  }

  void display() {
    strokeWeight(5);
    stroke(0, 50);
    fill(0, 170, 0);

    rect(x - w/2, -height/2, w, height/2 + top);
    rect(x - w/2, height/2, w, -(height/2 - bottom));
  }
}