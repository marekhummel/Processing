float angle = PI/6;
int maxd = 1;

void setup() {
  size(600, 600);
}


int ticks;
void draw() {
  ticks++;
  
  if (ticks % 30 == 0) maxd++;
  angle = map(mouseX, 0, width, 0, PI/2);
  
  background(0);
  translate(width/2, height);
  strokeCap(ROUND);
  branch(height * .3);
}



int depth = 0;
void branch(float len) {
  if (depth == maxd || len < 4) {
    leaf(len);
    return;
  }

  depth++;
  stroke(255);
  strokeWeight(len / 30);
  noFill();
  line(0, 0, 0, -len);

  translate(0, -len);
  pushMatrix();
  rotate(-angle);
  branch(len * 0.7);
  popMatrix();
  pushMatrix();
  rotate(angle);
  branch(len * 0.7);
  popMatrix();
  depth--;
}


void leaf(float r) {
  stroke(255);
  strokeWeight(1);
  fill(0, 255, 0, 127);
  ellipse(0, 0, r, r);
}