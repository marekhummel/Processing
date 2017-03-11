class Circle {

  float r;
  float theta;
  Circle parent;
  float d;
  float x, y;
  float speed;

  Circle(float r_, Circle p, float s) {
    this(r_, p, s, 0.0);
  }

  Circle(float r_, Circle p, float s, boolean t) {
    this(r_, p, s, (t ? r_ : 0));
  }

  Circle(float r_, Circle p, float s, float d_) {
    r = r_;
    parent = p;
    speed = s;
    d = d_;
    theta = 0;
  }


  void update() {
    if (parent != null) {
      x = parent.x + (parent.r + r) * cos(theta);
      y = parent.y + (parent.r + r) * sin(theta);
    }
    theta -= speed;
  }



  void display() {
    if (r < 1) return;
    strokeWeight(parent == null ? 3 : 1);
    stroke(CIRCLE);
    noFill();
    ellipse(x, y, r, r);
  }



  PVector trace() {
    float spin = theta * (parent.r / r + 1);
    float tx = x - d * cos(spin);
    float ty = y - d * sin(spin);

    if (r > 2) {
      line(x, y, tx, ty);
      noStroke();
      fill(0, 127);
      ellipse(x, y, r/4, r/4);
      fill(255, 0, 0, 127);
      ellipse(tx, ty, 5, 5);
    }

    return new PVector(tx, ty);
  }
}