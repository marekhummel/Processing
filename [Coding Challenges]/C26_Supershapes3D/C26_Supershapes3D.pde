// http://paulbourke.net/geometry/supershape/

import peasy.*;
import peasy.org.apache.commons.math.*;
import peasy.org.apache.commons.math.geometry.*;

PeasyCam cam;

float a = 1, b = 1;

PVector[][] shape;
int steps = 72;



void setup() {
  size(600, 600, P3D);
  colorMode(HSB, 360, 100, 100);
  cam = new PeasyCam(this, 500);
  shape = new PVector[steps+1][steps+1];
}


int hoff = 0;
void draw() {
  if (frameCount % 2 == 0) hoff+=1;
  background(0);
  lights();
  noStroke();
  fill(255);
  supershape(150);
}



void supershape(float r) {
  for (int pi = 0; pi <= steps; pi++) {
    float phi = map(pi, 0, steps, -HALF_PI, HALF_PI);
    for (int ti = 0; ti <= steps; ti++) {
      float theta = map(ti, 0, steps, -PI, PI);
     
      float r1 = cr(theta, 5, 0.1, 1.7, 1.7);
      float r2 = cr(phi, 1, 0.3, 0.5, 0.5);

      float x = r * r1 * cos(theta) * r2 * cos(phi);
      float y = r * r1 * sin(theta) * r2 * cos(phi);
      float z = r * r2 * sin(phi);
      shape[ti][pi] = new PVector(x, y, z);
    }
  }


  
  for (int pi = 0; pi < steps; pi++) {
    beginShape(TRIANGLE_STRIP);
    fill(map(pi + hoff, 0, steps, 0, 360*6) % 360, 100, 100);
    for (int ti = 0; ti <= steps; ti++) { 
      PVector v1 = shape[ti][pi];
      PVector v2 = shape[ti][pi+1];
      vertex(v1.x, v1.y, v1.z);
      vertex(v2.x, v2.y, v2.z);
    }
    endShape();
  }
}






float cr(float angle, float m, float n1, float n2, float n3) {
  float apart = pow(abs(1.0/a * cos(m/4.0 * angle)), n2);
  float bpart = pow(abs(1.0/b * sin(m/4.0 * angle)), n3);
  float r = 1.0 / pow(apart + bpart, 1.0/n1);
  return r;
}