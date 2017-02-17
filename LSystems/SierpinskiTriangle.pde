class SierpinskiTriangle extends LSystem {

  SierpinskiTriangle() {
    StringDict r = new StringDict();
    r.set("f", "f-g+f+g-f");
    r.set("g", "gg");
    super.init("f-g-g", r);
  }

  void setMatrix() {
    translate(50, 50);
  }

  void interpretate(char k) {
    float len = 400 * pow(1/2.0, ls.n);

    switch(k) {
    case 'f':
    case 'g':
      line(0, 0, len, 0);
      translate(len, 0);
      break;
    case '+':
      rotate(-radians(120));
      break;
    case '-':
      rotate(radians(120));
      break;
    }
  }
}