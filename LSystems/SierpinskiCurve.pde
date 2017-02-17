class SierpinskiCurve extends LSystem {

  SierpinskiCurve() {
    StringDict r = new StringDict();
    r.set("a", "+b-a-b+");
    r.set("b", "-a+b+a-");
    super.init("a", r);
  }

  void setMatrix() {
    translate(50, height - 50);
  }

  void interpretate(char k) {
    float len = 400 * pow(1/2.0, ls.n);

    switch(k) {
    case 'a':
    case 'b':
      line(0, 0, len, 0);
      translate(len, 0);
      break;
    case '+':
      rotate(-radians(60));
      break;
    case '-':
      rotate(radians(60));
      break;
    }
  }
}