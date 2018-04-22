class DNA {

  PVector[] genes;
  int ols, lifespan;

  DNA(int ls) {
    ols = ls;
    lifespan = ls;
    genes = new PVector[ls];
    for (int i = 0; i < ls; i++) {
      genes[i] = PVector.random2D().mult(2);
    }
  }


  DNA(int ls, PVector[] g) {
    ols = ls;
    lifespan = ls;
    genes = new PVector[ls];
    for (int i = 0; i < ls; i++) { 
      genes[i] = g[i];
    }
  }



  DNA crossover(DNA other) {
    PVector[] g = new PVector[ols];
    for (int i = 0; i < ols; i++) {
      g[i] = (random(1) < 0.5 ? genes[i].copy() : other.genes[i].copy());
      if (random(1) < 0.01) g[i] = PVector.random2D().mult(2);
    }
    return new DNA(ols, g);
  }
}