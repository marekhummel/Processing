PVector _spaceship;

Invader[] _invaders;
int _rows = 4;
int _cols = 5;
float _inv_size = 40;
float _xoffset;

ArrayList<Bullet> _bullets;
int _lastbullet;

boolean[] _keys;

void setup() {
  size(500, 500);
  
  //Set spaceship
  _spaceship = new PVector(width/2, height - 15);
  
  
  //Create bullets
  _bullets = new ArrayList<Bullet>();
  
  
  //Create invaders
  _invaders = new Invader[_rows * _cols];
  
  float margin = 2 * _inv_size;
  for (int j = 0; j < _rows; j++) {
    float y = 50 + j * 0.5 * margin;
    for (int i = 0; i < _cols; i++) {
      float x = 50 + (j % 2 == 1 ? 0.5 * margin : 0) + i * margin;
      _invaders[j * _cols + i] = new Invader(x, y, _inv_size);
    }
  }
  
  
  //Set x offset (move range per tick)
  _xoffset = 20;
  
  
  //Init keys
  _keys = new boolean[3];
}





int _tickcount = 0;
void draw() {
  _tickcount++;
  
  //Update
  
  //Update invaders every 60th tick
  if (_tickcount % 60 == 0) {   
    float next_left_x = _invaders[0].x - _inv_size/2 + _xoffset;
    float next_right_x = _invaders[2 * _cols - 1].x + _inv_size/2 + _xoffset;
    if (next_left_x < 0 || next_right_x > width) {
      for (Invader inv : _invaders)  {inv.move(0, 20); }
      _xoffset = -_xoffset;
    }
    else {
      for (Invader inv : _invaders) { inv.move(_xoffset, 0); }
    }  
  }
  
  
  //Update bullet every second tick
  if (_tickcount % 2 == 0) {
    for (Bullet bul : _bullets) { bul.update(); }
  }
  
  
 
  //Check collisions
  boolean[] rm = new boolean[_bullets.size()];
  
  for (int ib = 0; ib < _bullets.size(); ib++) {
    for (Invader i : _invaders) {
      if (i.dead) { continue; }
      
      Bullet b = _bullets.get(ib);
      float d1 = dis(b.x - b.w/2, b.y - b.h/2, i.x, i.y);
      float d2 = dis(b.x + b.w/2, b.y - b.h/2, i.x, i.y);
      
      if (d1 < _inv_size/2 || d2 < _inv_size/2) {
        i.dead = true;
        rm[ib] = true;
      }
    }
  }
  
  for (int i = 0; i < rm.length; i++) {
    if (rm[i]) { _bullets.remove(i); }
  }
  
  
  //Update keyboard actions
  updateActions();
  
  
  
  //Display
  background(245);
  
  rectMode(CENTER);
  noStroke();
  fill(170, 0, 0);
  rect(_spaceship.x, _spaceship.y, 70, 30);
  
  for (Invader inv : _invaders) { inv.display(); }
  for (Bullet bul :  _bullets) { bul.display(); }
}





void keyPressed() {
  if (keyCode == LEFT) { _keys[0] = true; } 
  if (keyCode == RIGHT) { _keys[1] = true; }   
  if (key == ' ') { _keys[2] = true; } 
}

void keyReleased() {
  if (keyCode == LEFT) { _keys[0] = false; } 
  if (keyCode == RIGHT) { _keys[1] = false; }   
  if (key == ' ') { _keys[2] = false; } 
}


void updateActions() {
  if (_keys[0]) { _spaceship.x -= 7; } 
  
  if (_keys[1]) { _spaceship.x += 7; } 
  
  if (_keys[2]) {
     if (_tickcount - _lastbullet < 20) { return; }
   
    _bullets.add(new Bullet(_spaceship.x));
    _lastbullet = _tickcount;
  }
}



float dis(float x1, float y1, float x2, float y2) {
  return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
}