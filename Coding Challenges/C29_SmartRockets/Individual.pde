class Individual {

  DNA dna;
  float fitness;
  boolean succeeded;
  boolean dead;

  PVector pos, vel;

  Individual(DNA d) {
    pos = new PVector(0, height-20);
    vel = new PVector(0, 0);
    dna = d;
  }



  Individual crossover(Individual o) {
    DNA newdna = dna.crossover(o.dna);
    return new Individual(newdna);
  }


  void update(PVector target) {
    if (succeeded || dead) return;


    dna.lifespan--;
    vel.setMag(10);
    vel.add(dna.genes[dna.lifespan]);
    vel.limit(3);
    pos.add(vel);

    if (pos.x < -width/2 || pos.x > width/2 || pos.y < 0 || pos.y > height) {
      dead = true;
      fitness = 0.1;
      return;
    }

    float dist = PVector.dist(pos, target);
    if (dist < 10) {
      succeeded = true;
      fitness = 5;
      return;
    }

    fitness = dist / (height - target.y);
  }


  void display() {
    pushMatrix();
    translate(pos.x, pos.y);
    rotate(vel.heading() - HALF_PI);
    stroke(255, 100);
    fill(200, 100);
    rectMode(CENTER);
    rect(0, 0, 10, 20);
    popMatrix();
  }
}