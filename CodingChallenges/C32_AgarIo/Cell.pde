class Cell {

  PVector pos;
  float r;
  float hue;
  boolean wobble;

  Cell(float x, float y, float r_, boolean w) {
    pos = new PVector(x, y);
    r = r_;
    wobble = w;
    hue = random(255);
  }



  boolean eat(Cell other) {
    if (other.r >= r) return false;
    if (PVector.dist(other.pos, pos) > other.r + r) return false;

    r = sqrt(r*r + other.r*other.r);
    return true;
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
    strokeWeight(r / 20);
    fill(hue, 255, 255);

    if (!wobble) {
      ellipse(pos.x, pos.y, 2*r, 2*r);
    } else {
      beginShape();
      for (float theta = 0; theta < TWO_PI; theta+=PI/36) {
        float wr = r + map(random(1), 0, 1, -r/16, r/16); // noise instead of random
        float x = pos.x + wr * cos(theta);
        float y = pos.y + wr * sin(theta);
        vertex(x, y);
      }
      endShape(CLOSE);
    }
  }
}
