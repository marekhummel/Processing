color BACKGROUND = color(54);
color CIRCLE = color(255, 127);
color TRACE = color(255, 100, 100);

ArrayList<Circle> circles; 
ArrayList<PVector> tracepts;

int k = -4;
int s = 3;
int freq = 50;

void setup() {
  size(600, 600);
  ellipseMode(RADIUS);

  float scale = 1 / (180 / PI * freq);
  circles = new ArrayList<Circle>();
  circles.add(new Circle(100, null, pow(k, 0) * scale));
  for (int i = 1; i < 11; i++) {
    Circle last = circles.get(circles.size()-1);
    circles.add(new Circle(last.r / s, last, pow(k, i) * scale));
  }

  tracepts = new ArrayList<PVector>();
}



void draw() {
  //Update

  for (int i = 0; i < freq; i++) {
    for (Circle c : circles) {
      c.update();
    };
    PVector newpt = circles.get(circles.size()-1).trace();
    if (!tracepts.contains(newpt)) tracepts.add(newpt);
  }


  //Draw
  translate(width/2, height/2);
  rotate(-HALF_PI);
  background(BACKGROUND);
  for (Circle c : circles) {
    c.display();
  }

  stroke(TRACE);
  strokeWeight(1);
  noFill();
  beginShape();
  for (PVector pt : tracepts) {
    vertex(pt.x, pt.y);
  }
  endShape();
}