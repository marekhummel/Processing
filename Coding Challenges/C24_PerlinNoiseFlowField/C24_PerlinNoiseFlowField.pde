int scl = 20;
int rows, cols;
float zoff;

Particle[] particles;
PVector[][] vectors;



void setup() {
  size(600, 400);

  rows = height / scl;
  cols = width / scl;
  vectors = new PVector[cols][rows];


  particles = new Particle[500];
  for (int i = 0; i < particles.length; i++) {
    particles[i] = new Particle();
  }
  
  background(255);
}



void draw() {
 // background(255);
  for (int xi = 0; xi < cols; xi++) {
    for (int yi = 0; yi < rows; yi++) {
      float angle = noise(xi * 0.05, yi * 0.05, zoff) * TWO_PI * 2;
      vectors[xi][yi] = PVector.fromAngle(angle);
    }
  }
  
  zoff += 0.005;
  
  
  
  //Draw
  for (Particle p : particles) {
    int xi = floor(p.pos.x / scl);
    int yi = floor(p.pos.y / scl);
    PVector f = vectors[xi][yi];
    p.addDir(f, 1);   

    p.update();
    p.display();
  }


//  stroke(100, 100);
//  fill(100, 100);
//  for (int xi = 0; xi < cols; xi++) {
//    for (int yi = 0; yi < rows; yi++) {
//      float x = (xi + 0.5) * scl;
//      float y = (yi + 0.5) * scl;
//      float x2 = x + vectors[xi][yi].x * scl;
//      float y2 = y + vectors[xi][yi].y * scl;
//      line(x, y, x2, y2);
//      ellipse(x2, y2, 2, 2);
//    }
//  }
}