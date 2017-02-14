class Cell {

  int i, j;
  boolean visited;
  boolean[] walls;  //TOP RIGHT BOTTOM LEFT
  
  Cell(int i_, int j_) {
    i = i_;
    j = j_;
    
    visited = false;
    walls = new boolean[] {true, true, true, true};
  }



  void display(int size, boolean path, boolean tip) {
    int x = i * size, y = j * size;
    
    noStroke();
    
    if (tip) { fill(0, 255, 0); }
    else if (path) { fill(0, 127, 0); }
    else { fill(0); }
    rect(x, y, size, size);
    
    stroke(200);
    noFill();
    if (walls[0]) { line(x, y, x + size, y); }
    if (walls[1]) { line(x + size, y, x + size, y + size); }
    if (walls[2]) { line(x, y + size, x + size, y + size); }
    if (walls[3]) { line(x, y, x, y + size); }
  }
}