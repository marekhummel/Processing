class Metaball {

  PVector pos, vel;
  float radius;
  
  Metaball() {
    pos = new PVector(random(width), random(height));  
    vel = PVector.random2D().mult(random(4,8));
    radius = random(20, 70);
  }
  
  
  
  float func(int x, int y) {
    float dis = PVector.dist(pos, new PVector(x,y));
    return radius / dis;  
  }
  
  
  
  
  void move() {
    pos.add(vel);
    
    if (pos.x <= 0 || pos.x >= width) vel.x *= -1;
    if (pos.y <= 0 || pos.y >= height) vel.y *= -1;
  }



}