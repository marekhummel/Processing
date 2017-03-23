Bird b;
ArrayList<Obstacle> obs;
float gravity = 0.2;

int score;

void setup() {
  size(400, 400);
  b = new Bird();
  obs = new ArrayList<Obstacle>();
}




void draw() {
  translate(30, height/2);
  background(200, 255, 255);


  b.applyForce(gravity);
  if (keyPressed) b.applyForce(-5);
  b.update();
  b.display();


  if (frameCount % 75 == 1) {
    obs.add(new Obstacle(width));
  }

  for (int i = obs.size() - 1; i >= 0; i--) {    
    Obstacle o = obs.get(i);
    if (o.x < -o.w) {
      obs.remove(i);
      continue;
    }

    boolean state = o.passed;
    b.dead |= o.hit(b);  
    if (o.passed && !state) score++;

    o.update();
    o.display();
  }

  fill(0);
  textSize(20);
  text(score, 0, -height/2+30);

  if (b.dead) noLoop();
}