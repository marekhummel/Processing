class Planet {

  PVector loc;
  float r;
  float angle;
  float orbitspeed;
  Planet[] children;


  Planet(float d, float r_, float os) {

    loc = PVector.random3D();
    loc.mult(d);

    r = r_;  
    orbitspeed = os;
    angle = random(TWO_PI);

    //Get some children
    if (r > 10) {
      children = new Planet[floor(random(0, r/7))];
      for (int i = 0; i < children.length; i++) {
        children[i] = new Planet(random(2, 4) * r, random(0.2, 0.4) * r, random(PI/270, PI/90));
      }
    }
  }


  void update() {
    angle += orbitspeed;

    if (children != null)
      for (Planet c : children) { 
        c.update();
      }
  }


  void display() {
    pushMatrix();
    
    PVector rot = loc.cross(new PVector(0, 0, 1)); 
    rotate(angle, rot.x, rot.y, rot.z);
    translate(loc.x, loc.y, loc.z);  

    noStroke();
    fill(255);
    sphere(r);  

    if (children != null)
      for (Planet c : children) { 
        c.display();
      }

    popMatrix();
  }
}