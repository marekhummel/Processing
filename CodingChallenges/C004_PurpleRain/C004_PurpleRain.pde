RainDrop[] _drops;


void setup() {
  size(600, 400);
  
  _drops = new RainDrop[500];
  for (int i = 0; i < _drops.length; i++) {
    _drops[i] = new RainDrop();
  } 
  
  
  colorMode(HSB, 360, 100, 100);
}


void draw() {
  background(270, 15, 80);
  translate(width/2, height/2);
  
  for (int i = 0; i < _drops.length; i++) {
    _drops[i].display();
    _drops[i].update();
    
    if (_drops[i].y > height/2) {
      _drops[i] = new RainDrop();
    }
  }
}