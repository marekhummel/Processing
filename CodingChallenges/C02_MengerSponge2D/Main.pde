ArrayList<Box> boxes;

void settings() { //<>//
  size(400, 400);
}

void setup() {
  background(0);

  rectMode(CENTER);
  fill(128, 0, 0);
  noStroke();

  boxes = new ArrayList<Box>();
  boxes.add(new Box(width/2, height/2, 300));
}



void draw() { 
  background(0);
  for (Box b : boxes) {
    b.display();
  }
}



void keyPressed() { 
  ArrayList<Box> newboxes = new ArrayList<Box>();
  for (Box b : boxes) {
    newboxes.addAll(b.split());
  }
  boxes = newboxes;
}