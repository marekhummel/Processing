import peasy.*;
import peasy.org.apache.commons.math.*;
import peasy.org.apache.commons.math.geometry.*;

PeasyCam cam;
ArrayList<Firework> fireworks;

void setup() {
  size(600, 400, P3D);
  cam = new PeasyCam(this, 500);
  colorMode(HSB, 360, 100, 100, 100);
  fireworks = new ArrayList<Firework>();
}


void draw() {
  background(10);
  if (frameCount % 40 == 0) fireworks.add(new Firework());

  for (int i = 0; i < fireworks.size(); i++) {
    fireworks.get(i).update();
    fireworks.get(i).display();

    if (fireworks.get(i).gone) fireworks.remove(i);
  }
}