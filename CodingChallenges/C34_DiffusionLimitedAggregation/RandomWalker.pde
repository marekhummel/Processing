class RandomWalker {

  PVector pos;
  RandomWalker(ArrayList<PVector> pts) {
    pos = pts.get(floor(random(pts.size()))).copy();
  }


  void move() {
    pos.add(PVector.random2D());
    pos.x = constrain(pos.x, 0, width);
    pos.y = constrain(pos.y, 0, height);
  }


  boolean stuck(ArrayList<PVector> seeds, float dis) {
    for (PVector s : seeds) {
      if ((pos.x-s.x)*(pos.x-s.x)+(pos.y-s.y)*(pos.y-s.y) <= dis*dis) return true;
    }
    return false;
  }
}