class HexagonalGosper extends LSystem {

  HexagonalGosper() {
    StringDict r = new StringDict();
    r.set("x", "x+yf++yf-fx--fxfx-yf+");
    r.set("y", "-fx+yfyf++yf+fx--fx-y");
    super.init("xf", r);
  }

  void setMatrix() {
    translate(2*width/3, height-50);
  }

  void interpretate(char k) {
    float len = 100 * pow(1/2.0, ls.n);

    switch(k) {
    case 'f':
      line(0, 0, len, 0);
      translate(len, 0);
      break;
    case '+':
      rotate(-PI/3);
      break;
    case '-':
      rotate(PI/3);
      break;
    }
  }
}