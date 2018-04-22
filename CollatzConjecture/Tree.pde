class Tree {

  Node root;
  int limit;
  int maxgen;
  int gen;
  IntList vals;

  Tree(int lim, int gl) {
    root = new Node(2);
    vals = new IntList();
    vals.append(root.value);
    limit = lim;
    maxgen = gl;
  }


  ArrayList<Node> actives = new ArrayList<Node>();
  void generateNext() {
    if (gen == 0) actives.add(root);
    if (actives.size() == 0) return;

    for (int i = actives.size()-1; i >= 0; i--) {
      Node n = actives.get(i);
      if (n.addChildren(limit, vals)) {
        actives.addAll(n.children);
        for (Node c : n.children) vals.append(c.value);
      }
      actives.remove(i);
    }
    gen++;
    println(vals.size());
  }



  void display(float x, float y, float angle) {
    for (Node n : actives) n.hl = true;
    root.display(x, y, angle);
  }
}