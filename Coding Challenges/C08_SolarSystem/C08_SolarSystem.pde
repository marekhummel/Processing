import peasy.*;

PeasyCam cam;
Planet sun;

void setup() {
  size(500, 500, P3D);
  cam = new PeasyCam(this, 500);

  sun = new Planet(0, 60, 0);
}


void draw() {
  //Update
  sun.update();
  
  
  //Draw
  background(0);
  lights();
  
  sun.display();
  pointLight(255, 255, 255, 0, 0, 0);
}