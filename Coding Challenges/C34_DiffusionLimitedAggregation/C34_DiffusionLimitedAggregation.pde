int maxwalkers = 100;
int iter = 200;
float rad = 4;

ArrayList<RandomWalker> walkers;
ArrayList<PVector> seeds;
ArrayList<PVector> startingpoints;

void setup() {
  size(400, 400);
  colorMode(HSB);
  noStroke();

  setStartingPoints();
  walkers = new ArrayList<RandomWalker>();
  for (int i = 0; i < maxwalkers; i++) walkers.add(new RandomWalker(startingpoints));
  setSeeds();
}


void setStartingPoints() {
  startingpoints = new ArrayList<PVector>();

  // 1
  for (float x = 0; x < width; x+=0.5) {
    startingpoints.add(new PVector(x, 0));
    startingpoints.add(new PVector(x, height));
  }
  for (float y = 0; y < height; y+=0.5) {
    startingpoints.add(new PVector(0, y));
    startingpoints.add(new PVector(width, y));
  }

  // 2
  //for (float x = 0; x < width; x+=0.5) {
  //  startingpoints.add(new PVector(x, 0));
  //}
}


void setSeeds() {
  seeds = new ArrayList<PVector>();
  
  //1
  seeds.add(new PVector(width/2, height/2));
  
  //2
  //for (float x = 0.5*rad; x < width; x+=rad) {
  //  seeds.add(new PVector(x, height));
  //}
}




void draw() {
  background(51);

  for (int i = 0; i < iter; i++) {
    for (int wi = walkers.size() - 1; wi >= 0; wi--) {
      RandomWalker rw = walkers.get(wi);
      rw.move();
      if (rw.stuck(seeds, rad*2)) {
        seeds.add(rw.pos);
        walkers.remove(wi);
      }
    }
  }

  while (walkers.size() != maxwalkers) walkers.add(new RandomWalker(startingpoints));

  fill(255);
  //for (RandomWalker rw : walkers) ellipse(rw.pos.x, rw.pos.y, 2*rad, 2*rad); 
  
  float c = 0;
  for (PVector s : seeds) {
    c += 0.3;
    fill(c % 255, 255, 255);
    ellipse(s.x, s.y, 2*rad, 2*rad);
  }
}