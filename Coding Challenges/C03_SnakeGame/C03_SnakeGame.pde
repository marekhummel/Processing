int SQUARE_SIZE = 10;

PVector[] _snake;
int _snakelength;
PVector _fruit;

int _dir; //UP RIGHT DOWN LEFT
boolean _dirchanged;
boolean _gamerunning;

PVector _maxindex;



void setup() {
  size(600, 400);
  frameRate(8);
  
  _maxindex = new PVector(int(width/SQUARE_SIZE)-1, int(height/SQUARE_SIZE)-1);
  
  _snake = new PVector[int((_maxindex.x+1) * (_maxindex.y+1))];
  for (int i = 0; i < _snake.length; i++) { _snake[i] = new PVector(-1, -1); }
  
  _snake[0] = new PVector(int(_maxindex.x / 2), int(_maxindex.y / 2));
  _snake[1] = new PVector(int(_maxindex.x / 2) - 1, int(_maxindex.y / 2));
  _snake[2] = new PVector(int(_maxindex.x / 2) - 2, int(_maxindex.y / 2));
  _snakelength = 3;
  _dir = 0;
  
  _fruit = new PVector(int(random(_maxindex.x)), int(random(_maxindex.y))); 
  
  _gamerunning = true;
}



void draw() {
  background(0);
  

  
  //Update snake
  if (_gamerunning) {
    PVector next = get_next_square();
    
    if (out_of_bounds(next) || hit_itself(next))
    {
      _gamerunning = false;
    }
    else 
    {
      if (next.x == _fruit.x && next.y == _fruit.y) {
        _snakelength += 3;
        _fruit = new PVector(int(random(_maxindex.x)), int(random(_maxindex.y)));
      }
      
      
      for (int i = _snakelength - 1; i > 0; i--) {
        _snake[i] = _snake[i-1];
      }
      _snake[0] = next;
      _dirchanged = false;
    }  
  }
  
  
  //Draw fruit
  fill(127, 0, 0);
  rect(_fruit.x * SQUARE_SIZE, _fruit.y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE);
  
  
  //Draw snake
  stroke(255);
  fill(0, 0, 255);
  for (int i = 0; i < _snakelength; i++) {
    rect(_snake[i].x * SQUARE_SIZE, _snake[i].y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE);
  }
  fill(255);
  rect(_snake[0].x * SQUARE_SIZE, _snake[0].y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE);
}




PVector get_next_square() {
  PVector last = _snake[0];
  PVector next = new PVector(-1, -1);
  
  switch (_dir) {
    case 0:
      next = new PVector(last.x, last.y-1);
      break;
    case 1:
      next = new PVector(last.x+1, last.y);
      break;
    case 2:
      next = new PVector(last.x, last.y+1);
      break;
    case 3:
      next = new PVector(last.x-1, last.y);
      break;     
  }
  
  return next;
}





boolean out_of_bounds(PVector next) {
  return next.x == -1 || next.y == -1 || next.x == _maxindex.x+1 || next.y == _maxindex.x+1;
}


boolean hit_itself(PVector next) {
  for (int i = 0; i < _snakelength; i++) {
    if (next.x == _snake[i].x && next.y == _snake[i].y) { return true; }
  }
  return false;
}





void keyPressed() {
  if (_dirchanged) { return; }
  
  if (keyCode == UP && _dir != 2) {
    _dir = 0;
  } else if (keyCode == RIGHT && _dir != 3) {
    _dir = 1;
  } else if (keyCode == DOWN && _dir != 0) {
    _dir = 2;
  } else if (keyCode == LEFT && _dir != 1) {
    _dir = 3;
  }
  _dirchanged = true;
}