class Ball {

  PVector pos, vel, acc;
  float r = 7;
  int bounce_cooldown;
  
  Ball(float x, float y) {
    pos = new PVector(x, y);
    vel = new PVector(0, 0);
    acc = new PVector(0, 0);
  }
  
  
  void applyForce(PVector force) {
    acc.add(force);
  }
  
  
  void update() {
    if(bounce_cooldown > 0) { bounce_cooldown--; };
    vel.add(acc);
    pos.add(vel);
    acc.mult(0);
  }
  
  float tempr;
  void display() {
    if (tempr != r) { tempr++; }
    
    noStroke();
    fill(255);
    ellipse(pos.x, pos.y, tempr, tempr);  
  }
  
}