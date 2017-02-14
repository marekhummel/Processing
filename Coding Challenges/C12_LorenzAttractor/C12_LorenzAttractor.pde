import peasy.*;
import peasy.org.apache.commons.math.*;
import peasy.org.apache.commons.math.geometry.*;

PeasyCam _cam;

ArrayList<PVector> _pts;

float a, b, c;  //sigma, rho, beta
float dt;
float x, y, z;

void setup() {
  size(600, 600, P3D);
  _cam = new PeasyCam(this, 100);
  _cam.setMinimumDistance(10);
  colorMode(HSB, 360, 100, 100);

  _pts = new ArrayList<PVector>();

  a = 10;
  b = 28;
  c = 8/3;
  dt = 0.01;

  x = 0.1;
  y = 0;
  z = 0;
}




void draw() {  
  //Calculate new point
  //  dx / dt = a (y - x)
  //  dy / dt = x (b - z) - y
  //  dz / dt = xy - c * z
  //dt is basically the time difference, so u can set any fitting value
  //since dx,dy,dz are diffences, the values are added to there old values
  float dx = dt * a * (y - x);
  float dy = dt * (x * (b - z) - y);
  float dz = dt * (x * y - c * z);


  //Save
  x += dx;
  y += dy;
  z += dz;
  _pts.add(new PVector(x, y, z));


  //Plot
  background(0);
  noFill();
  
  float hue = 0;
  beginShape();
  for (PVector p : _pts) {
    hue = (hue + 0.1) % 360;
    stroke(hue, 100, 100);
    vertex(p.x, p.y, p.z);
  }
  endShape();
  
}