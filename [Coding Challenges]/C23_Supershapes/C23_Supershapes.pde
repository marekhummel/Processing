// http://paulbourke.net/geometry/supershape/

float a = 1, b = 1;
float n1 = 0.1, n2 = 1.7, n3 = 1.7;
float m = 5;


void setup() {
  size(500, 500);
  noLoop();
}



void draw() {
  translate(width/2, height/2);
  scale(0.9 * width/2, 0.9 * height/2);
  background(51);
  
  stroke(255);
  strokeWeight(0.005);
  noFill();
  beginShape();
  for (float theta = 0; theta < TWO_PI; theta += PI/200) {  
    float apart = pow(abs(1.0/a * cos(m/4.0 * theta)), n2);
    float bpart = pow(abs(1.0/b * sin(m/4.0 * theta)), n3);
    float r = 1.0 / pow(apart + bpart, 1.0/n1);
    
    float x = r * cos(theta);
    float y = r * sin(theta);
    vertex(x, y);
  }
  endShape(CLOSE);
}