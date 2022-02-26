class Bullet {
  
  float x, y, w, h;
  
  
  Bullet(float x_) {
    x = x_;
    y = height - 30;
    
    w = 10;
    h = 20;
  }
  
  
  
  void update() {
    y -= 20;
  }
  
  
  
  void display() {
    noStroke();
    fill(0);
    rectMode(CENTER);
    rect(x, y, w, h, 5, 5, 0, 0);  
  }
  

}