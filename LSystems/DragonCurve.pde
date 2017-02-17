class DragonCurve extends LSystem {

  DragonCurve() {
    StringDict r = new StringDict();
    r.set("x", "x+yf+");
    r.set("y", "-fx-y");
    super.init("fx", r);
  }

  void setMatrix() {
    translate(width/2,height/2);
  }

  void interpretate(char k) {
    float len = 200 * pow(7/10.0, ls.n);
    
    switch(k) {
    case 'f':
      line(0, 0, len, 0);
      translate(len, 0);
      break;
    case '+':
      rotate(-HALF_PI);
      break;
    case '-':
      rotate(HALF_PI);
      break;
    }
  }
}