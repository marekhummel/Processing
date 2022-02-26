import peasy.*;
import peasy.org.apache.commons.math.*;
import peasy.org.apache.commons.math.geometry.*;

PeasyCam cam;

void setup() {
  size(600, 600, P3D);
  cam = new PeasyCam(this, 600);
}



void draw() {
  background(51);
  lights();
  fill(255);
  usphere(150);
}



void usphere(float r) {
  float step = PI/10;
  for (float lon = 0; lon <= TWO_PI + step; lon += step) {

    beginShape(TRIANGLE_STRIP);
     for (float lat = 0; lat <= PI; lat += step/2) {
      float x = r * sin(lat) * cos(lon);
      float y = r * sin(lat) * sin(lon);
      float z = r * cos(lat);
      vertex(x, y, z);
      
      float x2 = r * sin(lat) * cos(lon+step);
      float y2 = r * sin(lat) * sin(lon+step);
      float z2 = r * cos(lat);
      vertex(x2, y2, z2);
    }
    endShape(CLOSE);
  }
}