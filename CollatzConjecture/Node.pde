class Node {

  int value;
  ArrayList<Node> children;
  float r = 5;
  float df = 3;
  float a = PI/13;

  Node(int v) {
    value = v;
    children = new ArrayList<Node>();
  }


  boolean addChildren(int limit, IntList vals) {
    if (value * 2 < limit && !vals.hasValue(value*2)) {
      children.add(new Node(value * 2));
    }
    if ((value*2 - 1) % 3 == 0 && value > 2) {
      int nv = (value*2 - 1) / 3;
      if (!vals.hasValue(nv)) children.add(new Node(nv));
    }

    return children.size() != 0;
  }


  boolean hl;

  void display(float x, float y, float angle) {
    if (children != null) {
      for (Node c : children) {
        float oa = angle;
        if ((c.value & 1) == 0) angle -= a;
        else angle += a;


        float nx = x + df*r*cos(angle);
        float ny = y - df*r*sin(angle);

        strokeWeight(5);
        stroke(255, 100);
        line(x, y, nx, ny);

        c.display(nx, ny, angle);
        angle = oa;
      }
    }

    if (hl) fill(255, 0, 0); else fill(255);
    noStroke();
    strokeWeight(1);
    ellipse(x, y, r, r);
    hl = false;

    fill(0);
  // text(value, x, y);
  }
}