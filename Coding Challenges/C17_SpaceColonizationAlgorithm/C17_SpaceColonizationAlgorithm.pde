Tree t;
int N = 1000;        //Amount of APs
float d = 10;       //Branch len
float dk = 2*d;     //Kill dis
float di = 10000;     //Attraction dis


void setup() {
  size(400, 600);

  t = new Tree(dk, di, d);
  t.genAPs(N);
}



boolean growing;


void draw() {  
  background(255);
  translate(width/2, height);
  t.display();
  if (growing) t.grow();

  if (t.fullyGrown) noLoop();
}


void keyPressed() {
  growing = !growing;
}