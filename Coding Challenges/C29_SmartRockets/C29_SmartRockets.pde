Population p;
PVector target;
int lifetime;

void setup() {
  size(600, 400);
  p = new Population(25);
  target = new PVector(0, 20);
}


void draw() {
  if (lifetime == p.lifespan) {
    p.generate();
    lifetime = 0;
  }
  lifetime++;



  translate(width/2, 0);
  background(20);
  p.run(target);
  
  fill(0, 0, 255);
  ellipse(target.x, target.y, 10, 10);
  
  fill(255);
  textSize(14);
  text(lifetime, -width/2 + 20, 20);
}