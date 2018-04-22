class Population {

  int size;
  Individual[] creatures;
  ArrayList<Obstacle> obstacles;
  int lifespan = 200;
  
  Population(int s) {
    size = s;
    creatures = new Individual[s];
    for (int i = 0; i < s; i++) {
      creatures[i] = new Individual(new DNA(lifespan));
    }
    obstacles = new ArrayList<Obstacle>();
  }

   
  
  void generate() {
    ArrayList<Individual> pool = new ArrayList<Individual>();
    for (Individual c : creatures) {
      for (int i = 0; i < c.fitness * 100; i++) pool.add(c);
    }
    
    
    Individual[] newcreatures = new Individual[size];
    for (int i = 0; i < size; i++) {
      Individual a = pool.get(floor(random(pool.size())));
      Individual b = pool.get(floor(random(pool.size())));
      newcreatures[i] = a.crossover(b);
    }
    
    creatures = newcreatures;
   }
  
  
  
  void run(PVector target) {  
    for (Individual i : creatures) {
      i.update(target, obstacles);
      i.display();    
    }
    for (Obstacle o : obstacles) {
      o.display();
    }
  }
  
}