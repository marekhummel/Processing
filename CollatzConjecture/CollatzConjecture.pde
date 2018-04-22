Tree t;

void setup() {
  size(600, 600);
  t = new Tree(10000, 20);
  frameRate(2);
  stroke(0);
  textAlign(CENTER, CENTER);
  textSize(10);
}



void draw() {
  background(51);
  translate(3*width/4, height-20);
  t.display(0, 0, PI);
  t.generateNext();  
}


void mousePressed() {noLoop();}