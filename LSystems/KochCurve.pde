class KochCurve extends LSystem {

  KochCurve() {
    StringDict r = new StringDict();
    r.set("f", "f+f--f+f");
    super.init("f", r);
  }

  void setMatrix() {
    translate(50, height-50);
  }

  void interpretate(char k) {
    float len = 400 * pow(1/3.0, ls.n);

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