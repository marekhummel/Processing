class Firework {
  PVector pos;
  float speed;
  int hue;

  boolean exploded;
  boolean gone;
  Glower[] dust;


  Firework() {
    pos = new PVector(random(width), height);
    speed = random(5, 6);
    hue = floor(random(0, 360));
    exploded = false;
  }




  void update() {
    if (exploded) {
      boolean allgone = true;
      for (Glower g : dust) { 
        g.update();
        allgone &= g.gone;
      }
      if (allgone) gone = true;
      return;
    }



    pos.add(new PVector(0, -speed));    
    speed -= 0.05;
    if (speed <= 0.5) { explode(); }
  }



  void explode() {
    exploded = true;
    dust = new Glower[floor(random(40, 70))];
    for (int i = 0; i < dust.length; i++) { 
      PVector v = PVector.random2D();
      dust[i] = new Glower(pos.copy(), v.mult(random(1)), hue);
    }
  }



  void display() {
    if (!exploded) {
      noStroke();
      fill(hue, 100, 100, 80);
      ellipse(pos.x, pos.y, 5, 5);
    } else {
      for (Glower g : dust) { 
        g.display();
      }
    }
  }
}