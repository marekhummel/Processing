class Particle {

  PVector pos, dir;
  PVector prev;
  float speed;
  float dec;

  Particle() {
    pos = new PVector(random(width), random(height));
    dir = new PVector(0, 0);
    speed = random(5,7);
    dec = random(0.001, 0.02);
    
    prev = pos;
  }



  void update() {
    if (speed <= 0) return;
    
    prev = pos.copy();
    pos.add(PVector.mult(dir, speed));
    speed -= dec;
    checkEdges();
  }


  void addDir(PVector f, float imp) {
    dir.add(PVector.mult(f, imp)).normalize();
  }


  void checkEdges() {
    if (pos.x <= 0) pos.x = width;
    if (pos.x >= width) pos.x = 0;
    if (pos.y <= 0) pos.y = height;
    if (pos.y >= height) pos.y = 0;
    
    if (pos.x <= 0 || pos.x >= width || pos.y <= 0 || pos.y >= height) prev = pos;
  }


  void display() {
    stroke(0, 10);
    line(pos.x, pos.y, prev.x, prev.y);
  }
}