Cell me;
Cell[] enemies;


void setup() {
  size(600, 600);
  colorMode(HSB);

  me = new Cell(0, 0, 64);

  enemies = new Cell[400];
  for (int i = 0; i < enemies.length; i++) {
    enemies[i] = new Cell(random(-2 * width, 2 * width), random(-2*height, 2*height), 8);
  }
}



void draw() {
  me.move();
  translate(width/2, height/2);
  translate(-me.pos.x, -me.pos.y);

  background(245);
  stroke(0);
  strokeWeight(4);
  noFill();
  rect(-2*width, -2*height, 4*width, 4*height); 

  me.move();
  for (Cell e : enemies) e.display();
  me.display();
}