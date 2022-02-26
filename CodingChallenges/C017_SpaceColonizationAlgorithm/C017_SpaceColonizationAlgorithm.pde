Tree t;
int N = 2000;        //Amount of APs
float d = 10;       //Branch len
float dk = 1*d;     //Kill dis
float di = 200;     //Attraction dis


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


  //Status
  stroke(0);
  if (t.fullyGrown) fill(255, 180, 0); else if (growing) fill(0, 255, 0); else fill(255, 0, 0);
  rect(-width/2-1, -15, 15, 15);


  //Show crown
  stroke(255, 0, 0);
  for (float scy = CrownArea.minHeight; scy <= 1; scy+= 0.02) {
    float x = map(CrownArea.maxDis(scy), -1, 1, -width/2, width/2);
    float y = map(scy, 0, 1, 0, -height); 
    float px = map(CrownArea.maxDis(scy-0.02), -1, 1, -width/2, width/2);
    float py = map(scy-0.02, 0, 1, 0, -height); 
    line(x, y, px, py);
    line(-x, y, -px, py);
  }

  if (t.fullyGrown) noLoop();
}


void keyPressed() {
  growing = !growing;
}