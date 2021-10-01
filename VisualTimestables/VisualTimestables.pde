float maxfactor = 10;
boolean allowFloatingFactor = true;




float _factor = 2;
int _modulus = 200;    // amount of points on circle

float _circlerad;
ArrayList<PVector> _points;


void setup() {
  size(500, 500);
  colorMode(HSB);
  _circlerad = 0.45 * min(width, height);
}




void draw() {
  background(255);
  translate(width/2, height/2);
  rotate(PI);  //so the point in the west is fixed rather than the one in the east
  
  
  //Catch mouse 
  _modulus = int(constrain(map(mouseX, 0, 0.8*width, 2, 200), 2, 200)); 
  _factor = map(mouseY, 0, height, 2, maxfactor);
  _factor = (allowFloatingFactor ? _factor : int(_factor));
  
  
  //Draw circle itself (the perimeter)
  noFill();
  strokeWeight(1);
  stroke(127,127,127);
  ellipse(0, 0, 2*_circlerad, 2*_circlerad); 


  int hue = int(map(_factor, 2, maxfactor, 0, 255));
  int sat = int(map(_modulus, 2, 200, 200, 255));
  
  
  //Draw points on perimeter
  noStroke();
  fill(hue, sat, 255);
  for (float angle = 0; angle < TWO_PI; angle += TWO_PI / _modulus) {
    ellipse(cos(angle) * _circlerad, sin(angle) * _circlerad, 5, 5);
  }


  //Draw lines
  strokeWeight(1);
  stroke(hue, sat, 255);
  noFill();
  for (int i = 0; i < _modulus; i++) {
    PVector start = angleToPoint(map(i, 0, _modulus, 0, TWO_PI));
    PVector end = angleToPoint(map((i * _factor) % _modulus, 0, _modulus, 0, TWO_PI));
    
    line(start.x, start.y, end.x, end.y);
  }
  


  //Plot text
  resetMatrix();
  noStroke();
  fill(0);
  textSize(13);
  textAlign(RIGHT, TOP);
  text(str(_factor), width - 5, 0);
  text(str(_modulus), width - 5 , 15);
}





PVector angleToPoint(float angle) {
  return new PVector(cos(angle) * _circlerad, sin(angle) * _circlerad);
}
