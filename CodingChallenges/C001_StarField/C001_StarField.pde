Star[] _stars;


void setup() {
  size(600,600);
  _stars = new Star[800];
  
  for (int i = 0; i < _stars.length; i++) {
    _stars[i] = new Star();
  }
 
}



void draw() {
  background(0);
  translate(width/2, height/2);
  
  for (Star s : _stars) {
     s.update();
     s.show();
  }
}