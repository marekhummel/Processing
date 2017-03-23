float t;
float scl = 50;

void setup() {
  size(600, 600);
  background(245);
  lx = 0;
  ly = -exp(1) + 2;


  int steps = 400;
  translate(width/2, height/2);
  noStroke();
  fill(150);
  for (float i = 0; i < steps; i++) {
    ellipse(lerp(-width, width, i / steps), 0, 1, 1);
    ellipse(0, lerp(-height, height, i / steps), 1, 1);
  }
  
  for (float theta = 0; theta < TWO_PI; theta += PI/steps * 2) {
    for (int r = 1; r < 10; r++) {
      ellipse(r * scl * cos(theta), r * scl * sin(theta), 1, 1);
    }
  }
}


float lx, ly;
void draw() {
  translate(width/2, height/2);

  float r = exp(cos(t)) - 2 * cos(4*t) - pow(sin(t / 12), 5);
  float x = sin(t) * r;
  float y = -cos(t) * r;
  stroke(255, 0, 0, 100);
  line(x*scl, y*scl, lx*scl, ly*scl);

  lx = x;
  ly = y;
  t += 0.04;
}