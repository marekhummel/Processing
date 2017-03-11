float a = 1;
float b = 1;
float n = 1/2.0;


void setup() {
  size(500, 500);
  noLoop();
}



void draw() {
  translate(width/2, height/2);
  scale(0.9 * width/2, 0.9 * height/2);
  background(0);
  
  stroke(255);
  strokeWeight(0.01);
  noFill();
  beginShape();
  for (float theta = 0; theta < TWO_PI; theta += PI/36) {
    float x = pow(abs(cos(theta)), 2.0/n) * a * sgn(cos(theta));
    float y = pow(abs(sin(theta)), 2.0/n) * b * sgn(sin(theta));
    vertex(x, y);
  }
  endShape();
}



int sgn(float a) {
  if (a > 0) return 1;
  if (a < 0) return -1;
  return 0;
}