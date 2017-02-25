class AttractionPoint {

  PVector pos;
  boolean reached;
  
  
  AttractionPoint(float x, float y) {
    pos = new PVector(x, y);
  }

  AttractionPoint() {
    float scx, scy;
    do {
      scx = random(-1, 1);
      scy = random(1);
    } while (!CrownArea.inArea(scx, scy));


    float x = map(scx, -1, 1, -width/2, width/2);
    float y = map(scy, 0, 1, 0, -height); 
    pos = new PVector(x, y);
  }


  void display() {
    if (reached) return;
    
    noStroke();
    fill(20);
    ellipse(pos.x, pos.y, 2, 2);
  }
}