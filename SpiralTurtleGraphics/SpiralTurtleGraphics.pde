float len = 400;

void setup() {
  size(500, 500);
  
  translate(120, 450);
  pushMatrix();
  
  background(0);
  stroke(255, 100);
}


void draw() {
  popMatrix();  
  line(0, 0, 0, -len);
  translate(0, -len);
  rotate(2*PI/3 * 1.005);
  pushMatrix();
 
  len-=1;
  
  if (len <= 0) frameRate(0);
}