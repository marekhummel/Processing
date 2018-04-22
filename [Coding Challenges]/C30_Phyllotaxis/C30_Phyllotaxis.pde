float c;
float angle;

void setup() {
  size(500, 500);
  c = 7;
  angle = radians(137.7);    //.3 .5 .7
  
  colorMode(HSB, 1500, 100, 100);
  background(0);
  //stroke(255);
  //fill(0, 127, 0);
  frameRate(120);
}



void draw() {
  translate(width/2, height/2);

  float r = 0.5 * c * sqrt(frameCount);
  float theta = frameCount * angle;
  PVector p = new PVector(r * cos(theta), r * sin(theta));
  
  fill(frameCount % 2500, 100, 100);
  ellipse(p.x, p.y, c, c);
}