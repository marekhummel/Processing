static class CrownArea {

  static float minHeight = 0.25;
  
  static float maxDis(float y) {
    return (pow(2*y, 4) - 2.9*pow(2*y, 3) + pow(2*y, 2) + 2*(2*y))/2;
  }

  static boolean inArea(float scx, float scy, float off) {
    if (scx == 0) return true;
    if (scy < minHeight) return false;
    return abs(scx) + off <= maxDis(scy);
  }
}