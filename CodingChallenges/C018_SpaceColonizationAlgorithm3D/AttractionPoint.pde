class AttractionPoint {

  PVector pos;
  boolean reached;
  
  
  AttractionPoint(float x, float y, float z) {
    pos = new PVector(x, y, z);
  }

  AttractionPoint() {
    float scx, scy, scz;
    do {
      scx = random(-1, 1);
      scy = random(1);
      scz = random(-1, 1);
    } while (!CrownArea.inArea(scx, scy, scz));


    float x = map(scx, -1, 1, -width/2, width/2);
    float y = map(scy, 0, 1, 0, -height); 
    float z = map(scz, -1, 1, -width/2, width/2);
    pos = new PVector(x, y, z);
  }


  void display() {
    if (reached) return;
    
    noStroke();
    fill(255, 0, 0, 100);
    
    pushMatrix();
    translate(pos.x, pos.y, pos.z);
    sphere(1);
    popMatrix();
  }
}