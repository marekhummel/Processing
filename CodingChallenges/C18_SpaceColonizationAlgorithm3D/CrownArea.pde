static class CrownArea {

  static float minHeight = 0.25;
  
  static float maxDis(float y) {
    return 1-y;
  }

  static boolean inArea(float scx, float scy, float scz) {
    if (scx == 0 && scz == 0) return true;
    if (scy < minHeight) return false;
    return sqrt(scx*scx + scz*scz) <= maxDis(scy);
  }
}