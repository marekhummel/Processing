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


  void update(PVector target, ArrayList<Obstacle> obs) {
    if (succeeded || dead) return;


    dna.lifespan--;
    vel.setMag(10);
    vel.add(dna.genes[dna.lifespan]);
    vel.limit(3);
    pos.add(vel);

    float dist = PVector.dist(pos, target);
    fitness = pow(0.99, dist);

    if (pos.x < -width/2 || pos.x > width/2 || pos.y < 0 || pos.y > height) {
      dead = true;
      fitness *= 0.1;
      return;
    }

    for (Obstacle o : obs) {
      if (o.hit(pos)) {
        dead = true;
        fitness *= 0.1;
        return;
      }
    }


    if (dist < 10) {
      succeeded = true;
      fitness *= 10;
      return;
    }
  }


  void display() {
    pushMatrix();
    translate(pos.x, pos.y);
    rotate(vel.heading() - HALF_PI);
    strokeWeight(1);
    stroke(255, 100);
    fill(200, 100);
    rectMode(CENTER);
    rect(0, 0, 10, 20);
    popMatrix();
  }
}