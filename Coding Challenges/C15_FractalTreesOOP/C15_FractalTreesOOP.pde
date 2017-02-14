Branch _trunk;

void setup() {
  size(400, 400);
  _trunk = new Branch(new PVector(width/2, height), new PVector(width/2, height-100));
}


int ticks;
int depth = 0;
int maxd = 4;
int c = 5;
float a = PI/6;
void draw() {
  ticks++;

  background(0);
  
  if (ticks % 30 == 0) {
    depth++;
    if (depth < maxd) {
      _trunk.addChildren(c, a);
    } else if (depth == maxd) {
      _trunk.addLeaf();
    }
  }


  _trunk.display();
}