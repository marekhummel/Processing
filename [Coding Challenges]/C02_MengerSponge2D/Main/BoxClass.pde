class Box {

  PVector center;
  float size;


  Box(float x, float y, float s) {
    center = new PVector(x, y);
    size = s;
  }


  void display() {
    pushMatrix();
    translate(center.x, center.y);
    rect(0, 0, size, size);    
    popMatrix();
  }




  ArrayList<Box> split() {
    ArrayList<Box> boxes = new ArrayList<Box>();

    float ns = size/3;
    for (int x = -1; x < 2; x++) {
      float nx = center.x + x * ns;
      for (int y = -1; y < 2; y++) {
        if (x == 0 && y == 0)
          continue;

        float ny = center.y + y * ns;
        boxes.add(new Box(nx, ny, ns));
      }
    }

    return boxes;
  }
}