float f(float x) {
  return 5*x;
}

float xmin = -40;
float xmax = 60;
float ymin = -5;
float ymax = 10;



float xscl, yscl;
void setup() {
  size(600, 600);
  xscl = width/(xmax-xmin);
  yscl = height/(ymax-ymin);
}



void draw() {
  background(245);
  translate(map(0, xmin, xmax, 0, width), map(0, ymin, ymax, height, 0));
  scale(xscl, yscl);

  grid();

  //Plot
  noFill();
  stroke(255, 0, 0);
  strokeWeight(1/min(xscl, yscl));
  beginShape();
  for (float x = xmin; x <= xmax; x += 2/xscl) vertex(x, -f(x));
  endShape();
  noLoop();
}



void grid() {
  float xdist = pow(10, floor(log((xmax-xmin))/log(10))-1);
  float ydist = pow(10, floor(log((ymax-ymin))/log(10))-1);;

  stroke(0, 50);
  for (float i = 0;; i++) {
    strokeWeight((i == 0 ? 3 : 1)/xscl);
    line(i*xdist, -ymin, i*xdist, -ymax);
    line(-i*xdist, -ymin, -i*xdist, -ymax);
    if (i*xdist > xmax && -i*xdist < xmin) break;
  }
  
  for (float i = 0;; i++) { 
    strokeWeight((i == 0 ? 3 : 1)/yscl);
    line(xmin, -i*ydist, xmax, -i*ydist);
    line(xmin, i*ydist, xmax, i*ydist);
    if (i*ydist > ymax && -i*ydist < ymin) break;
  }
  
  pushMatrix();
  resetMatrix();
  noStroke();
  fill(0);
  textSize(10);
  textAlign(LEFT, TOP);
  text(nf(xdist, 1, 2) + "|" + nf(ydist, 1, 2), 10, 10);
  popMatrix();
}