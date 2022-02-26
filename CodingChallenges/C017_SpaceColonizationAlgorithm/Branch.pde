class Branch {

 
  PVector pos, dir;
  Branch parent;
  PVector attracDir;

  ArrayList<Branch> children;

  Branch(PVector p, PVector d) {
    pos = p;
    dir = d;
    parent = null;
    children = new ArrayList<Branch>();
    attracDir = new PVector(0, 0);
  }

  Branch(Branch par, PVector d, float m) {
    pos = PVector.add(par.pos, PVector.mult(d, m));
    dir = d;
    parent = par;
    children = new ArrayList<Branch>();
    attracDir = new PVector(0, 0);
  }


  float getR() {
    float exp = 2.7;
    if (children.size() == 0) return 0.5;

    float sum = 0.0;
    for (Branch c : children) sum += pow(c.getR(), exp);
    return pow(sum, 1/exp);
  }


  void display() {
    if (parent == null) return;

    stroke(127, 10, 10);
    strokeWeight(getR() * 2);
    line(parent.pos.x, parent.pos.y, pos.x, pos.y);
  }
}