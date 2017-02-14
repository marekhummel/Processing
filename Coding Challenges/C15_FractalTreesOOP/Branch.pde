class Branch {

  PVector start, end;
  Branch[] children;
  Leaf leaf;

  Branch(PVector s, PVector e) {
    start = s;
    end = e;
  }




  void addChildren(int c, float angle) {
    if (children != null) {
      for (Branch b : children) b.addChildren(c, angle);
      return;
    }


    PVector dir = end.copy().sub(start);

    children = new Branch[c];      
    for (int i = 0; i < c; i++) {
      float m = map(i, 0, c-1, -floor(c/2.0), floor(c/2.0));
      PVector d = dir.copy();
      d.mult(0.7);
      d.rotate(m * angle);
      PVector newend = end.copy().add(d);
      children[i] = new Branch(end, newend);
    }
  }



  void addLeaf() {
    if (children != null) {
      for (Branch b : children) b.addLeaf();
      return;
    }
    
    leaf = new Leaf(end.x, end.y);
  }



  void display() {
    PVector dir = end.copy().sub(start);
    strokeCap(ROUND);
    strokeWeight(2);
    stroke(255);
    line(start.x, start.y, end.x, end.y);
    if (leaf != null) leaf.display();

    if (children == null) return; 
    for (Branch b : children) b.display();
  }
}