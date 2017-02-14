class Line {

  PVector start, end;
  
  
  Line(float x1, float y1, float x2, float y2) {
    start = new PVector(x1, y1); 
    end = new PVector(x2, y2);
  }

  PVector dir() { return end.copy().sub(start); }


  boolean touchesBall(Ball b) {
    float dir1 = sqrt(pow(b.pos.x - start.x, 2) + pow(b.pos.y - start.y, 2));
    float dir2 = sqrt(pow(b.pos.x - end.x, 2) + pow(b.pos.y - end.y, 2));
    return (dir1 + dir2) < sqrt(pow(dir().mag(), 2) + pow(b.r / 2, 2));
  }

  
  void display() {
    stroke(255);
    noFill();
    line(start.x, start.y, end.x, end.y);  
  }



}