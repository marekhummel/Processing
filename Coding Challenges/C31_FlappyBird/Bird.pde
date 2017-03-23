class Bird {
  float y;
  float vel;
  float acc;
  float r = 12;
  
  boolean dead;
  
  
  
  void applyForce(float a) {
    acc += a;
  }


  void update() {
    y += vel;
    vel += acc;
    vel = constrain(vel, -4, 6);
    acc = 0;
    
    if (y > height/2 || y < -height/2) dead = true;
  }
  
  
  
  void display() {
    strokeWeight(1);
    stroke(0);
    fill(240, 240, 60);
    ellipse(0, y, 2*r, 2*r);  
  }


}