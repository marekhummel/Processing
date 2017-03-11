class Circle {

  float r;
  float theta;
  Circle parent;
  boolean epi;
  float d;
  float x, y;
  float speed;

  Circle(float r_, Circle p, boolean e, float s) {
    this(r_, p, e, s, r_);
  }

  Circle(float r_, Circle p, boolean e, float s, float d_) {
    r = r_;
    parent = p;
    epi = e;
    speed = s;
    d = d_;
    theta = 0;
  }


  void update() {
    if (parent != null) {
      x = parent.x;
      x += parent.r * cos(theta);
      x += (epi ? 1 : -1) * r * cos(theta); 
      y = parent.y;
      y += parent.r * sin(theta);
      y += (epi ? 1 : -1) * r * sin(theta);
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


  void drawtrace(PVector t) {
    if (r > 2) {
      stroke(CIRCLE);
      line(x, y, t.x, t.y);
      noStroke();
      fill(CIRCLE);
      ellipse(x, y, r/4, r/4);
      fill(TRACE);
      ellipse(t.x, t.y, 5, 5);
    }
  }


  PVector trace() {
    float spin = theta * (parent.r / r + 1);
    float tx = x - d * cos(spin);
    float ty = y - d * sin(spin);

    return new PVector(tx, ty);
  }
}