class FractalTree extends LSystem {

  FractalTree() {
    StringDict r = new StringDict();
    r.set("f", "ff+[+f-f-f]-[-f+f+f]");
    super.init("f", r);
  }

  void setMatrix() {
    translate(width/2, height);
    rotate(-HALF_PI);
  }

  void interpretate(char k) {
    float len = 150 * pow(0.5, ls.n);
    
    switch(k) {
    case 'f':
      line(0, 0, len, 0);
      translate(len, 0);
      break;
    case '+':
      rotate(radians(25));
      break;
    case '-':
      rotate(-radians(25));
      break;
    case '[':
      pushMatrix();
      break;
    case ']':
      popMatrix();
      break;
    }
  }
}