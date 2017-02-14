class Leaf {
  
  float x, y;
  
  Leaf(float x_, float y_) {
    x = x_;
    y = y_;
  }
  
  
  
  void display() {
    strokeWeight(1);
    fill(0, 255, 0, 200);
    ellipse(x, y, 10, 10);
  }


}