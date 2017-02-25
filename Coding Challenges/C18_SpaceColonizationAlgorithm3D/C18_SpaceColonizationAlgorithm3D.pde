import peasy.*;
import peasy.org.apache.commons.math.*;
import peasy.org.apache.commons.math.geometry.*;

Tree t;
int N = 100;          //Amount of APs
float d = 5;          //Branch len
float dk = 2*d;       //Kill dis
float di = 10000;     //Attraction dis

PeasyCam cam;

void setup() {
  size(400, 600, P3D);

  t = new Tree(dk, di, d);
  t.genAPs(N);
  
  cam = new PeasyCam(this, 0, -100, 0, 200);
}



boolean growing;


void draw() {  
  background(255);
  t.display();
  if (growing) t.grow();

  if (t.fullyGrown) {t.display(); noLoop(); }
}


void keyPressed() {
  growing = !growing;
}