float r;
int res = 200;
float wobble = 1/5.0;

void setup() {
  size(600, 600);
  r = 1/3.0 * min(width, height);
}





float t = 0;
void draw() {
  translate(width/2, height/2);

  background(51);
  noStroke();
  fill(255);

  beginShape();
  for (int s = 0; s < res; s++) {
    float angle = s * TWO_PI/res;
    float cr = r + map(noise(cos(angle) + 1, sin(angle) + 1, t), 0, 1, -r*wobble, r*wobble);
    float x = cr * cos(angle);
    float y = cr * sin(angle);
    vertex(x, y);
  }
  endShape();
  
  t += 0.01;
}