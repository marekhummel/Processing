ArrayList<Firework> fireworks;

void setup() {
  size(600, 400);
  colorMode(HSB, 360, 100, 100, 100);
  fireworks = new ArrayList<Firework>();
  background(10);
}


void draw() {
  fill(10, 20);
  rect(0, 0, width, height);
  
  if (frameCount % 20 == 0) fireworks.add(new Firework());

  for (int i = 0; i < fireworks.size(); i++) {
    fireworks.get(i).update();
    fireworks.get(i).display();

    if (fireworks.get(i).gone) fireworks.remove(i);
  }
}