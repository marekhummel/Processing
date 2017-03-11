color BACKGROUND = color(54);
color CIRCLE = color(255, 127);
color TRACE = color(255, 100, 100);

ArrayList<Circle> circles; 
ArrayList<PVector> tracepts;


int freq = 50;

void setup() {
  size(600, 600);
  ellipseMode(RADIUS);

  circles = new ArrayList<Circle>();
  circles.add(new Circle(150, null, false, 0));
  circles.add(new Circle(50, null, true, TWO_PI / 3600));
  //circles.add(new Circle(10, null, false, TWO_PI / 1200));
  for (int i = 1; i < circles.size(); i++) circles.get(i).parent = circles.get(i-1);


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
  circles.get(circles.size()-1).drawtrace(tracepts.get(tracepts.size() - 1));

  stroke(TRACE);
  strokeWeight(1);
  noFill();
  beginShape();
  for (PVector pt : tracepts) {
    vertex(pt.x, pt.y);
  }
  endShape();
}