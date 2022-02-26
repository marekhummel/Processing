LSystem ls;
float angle = radians(25);

void setup() {
  size(500, 500);

  StringDict r = new StringDict();
  r.set("f", "ff+[+f-f-f]-[-f+f+f]");
  ls = new LSystem("f", r);

  frameRate(2);
}


void draw() {
  background(0);

  translate(width/2, height);
  stroke(255, 100);
  float len = 150 * pow(0.5, ls.n);

  for (int i = 0; i < ls.currentState.length(); i++) {
    switch(ls.currentState.charAt(i)) {
    case 'f':
      line(0, 0, 0, -len);
      translate(0, -len);
      break;
    case '+':
      rotate(angle);
      break;
    case '-':
      rotate(-angle);
      break;
    case '[':
      pushMatrix();
      break;
    case ']':
      popMatrix();
      break;
    }
  }

  ls.produce();
}