float da = 1;
float db = 0.5;
float feed = 0.055;
float kill = 0.062;
float dt = 1;
int upf = 5; // updates per frame

Tuple[][] _cells;
Tuple[][] _laplace;


void setup() {
  size(300, 300);

  _cells = new Tuple[width][height];
  _laplace = new Tuple[width][height];
  for (int x = 0; x < width; x++) {
    for (int y = 0; y < height; y++) {
      _cells[x][y] = new Tuple(1, 0);
      _laplace[x][y] = new Tuple(1, 0);
    }
  }

  for (int i = 0; i < 10; i++) {
    int cx = floor(random(width-10));
    int cy = floor(random(height-10));
    for (int xoff = 0; xoff < 10; xoff++) {
      for (int yoff = 0; yoff < 10; yoff++) {
        _cells[cx+xoff][cy+yoff] = new Tuple(1, 1);
      }
    }
  }
  updateLaplace();
}


void draw()
{
  //Update
  for (int i = 0; i < upf; i++) {
    for (int x = 0; x < width; x++) {
      for (int y = 0; y < height; y++) {
        _cells[x][y] = calcNewValues(x, y);
      }
    }
    updateLaplace();
  }

  //Draw
  loadPixels();
  for (int x = 1; x < width-1; x++) {
    for (int y = 1; y < height-1; y++) {
      int index = x + y * width;
      pixels[index] = color((_cells[x][y].a - _cells[x][y].b) * 255);
    }
  }
  updatePixels();
  println(frameRate);
}





Tuple calcNewValues(int x, int y) {
  Tuple old = _cells[x][y];
  Tuple lp = _laplace[x][y];
  float a = old.a + (da*lp.a - old.a*old.b*old.b + feed*(1-old.a)) * dt; 
  float b = old.b + (db*lp.b + old.a*old.b*old.b - (kill+feed)*old.b) * dt; 
  return new Tuple(constrain(a, 0, 1), constrain(b, 0, 1));
}




void updateLaplace() {
  //"The Laplacian is performed with a 3x3 convolution with center weight -1, adjacent neighbors .2, and diagonals .05"
  for (int x = 1; x < width-1; x++) {
    for (int y = 1; y < height-1; y++) {
      float a = _cells[x][y].a * -1;
      a += _cells[x+1][y].a * 0.2;
      a += _cells[x-1][y].a * 0.2;
      a += _cells[x][y+1].a * 0.2;
      a += _cells[x][y-1].a * 0.2;
      a += _cells[x+1][y+1].a * 0.05;
      a += _cells[x+1][y-1].a * 0.05;
      a += _cells[x-1][y+1].a * 0.05;
      a += _cells[x-1][y-1].a * 0.05;

      float b = _cells[x][y].b * -1;
      b += _cells[x+1][y].b * 0.2;
      b += _cells[x-1][y].b * 0.2;
      b += _cells[x][y+1].b * 0.2;
      b += _cells[x][y-1].b * 0.2;
      b += _cells[x+1][y+1].b * 0.05;
      b += _cells[x+1][y-1].b * 0.05;
      b += _cells[x-1][y+1].b * 0.05;
      b += _cells[x-1][y-1].b * 0.05;

      _laplace[x][y] = new Tuple(a, b);
    }
  }
}