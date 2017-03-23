class Cell {

  PVector pos;
  float r;
  float hue;

  Cell(float x, float y, float r_) {
    pos = new PVector(x, y);
    r = r_;
    hue = random(255);
  }


  void move() {
    PVector dir = new PVector(mouseX - width/2, mouseY - height/2);
    float mag = constrain(map(dir.mag(), 0, (width + height)/2, 0, 10), 0, 4);
    dir.setMag(mag);
    pos.add(dir);
    pos.x = constrain(pos.x, -2*width, 2*width);  
    pos.y = constrain(pos.y, -2*height, 2*height);
  }


  void display() {
    stroke(0);
    strokeWeight(r / 12);
    fill(hue, 255, 255);
    ellipse(pos.x, pos.y, 2*r, 2*r);
  }
}