int _w = 1600, _h = 1200;
int _rows, _cols;
float _scl = 20;
float[][] z;

void setup() {
  size(600, 300, P3D);

  _rows = int(_h / _scl);
  _cols = int(_w / _scl);

  z = new float[_cols][_rows];
}

float _off;
void draw() {
  _off += 0.04;
  for (int j = 0; j < _rows; j++) {
    for (int i = 0; i < _cols; i++) {
      z[i][j] = map(noise(0.1 * i, 0.1 * j + _off), 0, 1, -100, 100);
    }
  } 





  background(0);
  
  translate(width/2, height/2);
  rotateX(PI/2);
  translate(0, 0, -height/2 - 50);

  stroke(255);
  fill(10);


  for (int j = 1; j < _rows; j++) {
    float y = - j * _scl;

    beginShape(TRIANGLE_STRIP);
    for (int i = 0; i < _cols; i++) {
      float x = i * _scl - _w / 2;

      vertex(x, y, z[i][j]);
      vertex(x, y + _scl, z[i][j-1]);
    } 
    endShape();
  }
}