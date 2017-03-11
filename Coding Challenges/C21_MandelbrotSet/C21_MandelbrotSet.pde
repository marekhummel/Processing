int iter = 256;

float oxmin = -2.5;
float oxmax = 1;
float oymin = -1;
float oymax = 1;
float xmin, xmax, ymin, ymax;

PVector zoompt;
float zoom = 1;

int[][] pts;
int[] gradient;



void setup() {
  size(700, 400);
  pts = new int[width+1][height+1];
  zoompt = new PVector(-.75, 0.1);
  setGradient();

  xmin = oxmin; 
  xmax = oxmax;
  ymin = oymin; 
  ymax = oymax;
  calc();
}


void draw() {
  //float zx = map(mouseX, 0, width, xmin, xmax);
  //float zy = map(mouseY, 0, height, ymax, ymin);
  //zoompt = new PVector(zx, zy);
  zoomIn();

  noStroke();
  for (int x = 0; x < width; x++) {
    for (int y = 0; y < height; y++) {
      int rgb = gradient[pts[x][y]];
      int r = (rgb >> 16) & 0xFF, g = (rgb >> 8) & 0xFF, b = rgb & 0xFF;
      fill(r, g, b);
      rect(x, y, 1, 1);
    }
  }
}


void mousePressed() {
  zoomIn();
}


void setGradient() {
  gradient = new int[16];
  gradient[0] = toInt(0, 0, 0);
  gradient[1] = toInt(25, 7, 26);
  gradient[2] = toInt(9, 1, 47);
  gradient[3] = toInt(4, 4, 73);
  gradient[4] = toInt(0, 7, 100);
  gradient[5] = toInt(12, 44, 138);
  gradient[6] = toInt(24, 82, 177);
  gradient[7] = toInt(57, 125, 209);
  gradient[8] = toInt(134, 181, 229);
  gradient[9] = toInt(211, 236, 248);
  gradient[10] = toInt(241, 233, 191);
  gradient[11] = toInt(248, 201, 95);
  gradient[12] = toInt(255, 170, 0);
  gradient[13] = toInt(204, 128, 0);
  gradient[14] = toInt(153, 87, 0);
  gradient[15] = toInt(106, 52, 3);
}


int toInt(int r, int g, int b) {
  return (r<<16) | (g<<8) | b;
}



void calc() {
  for (float x = xmin; x < xmax; x+=(xmax - xmin)/width) {
    for (float y = ymin; y < ymax; y+=(ymax - ymin)/height) {

      int i;
      float re = x, im = y;
      for (i = 0; i < iter; i++) {
        float nre = re*re - im*im + x; 
        float nim = 2 * re * im + y;
        re = nre;
        im = nim;
        if (re*re + im*im > 4) break;
      }

      int scx = floor(map(x, xmin, xmax, 0, width));
      int scy = floor(map(y, ymin, ymax, height, 0));
      pts[scx][scy] = i % gradient.length;
    }
  }
}


void zoomIn() {
  zoom *= 1.5;

  xmin = zoompt.x - (oxmax - oxmin)/(2 * zoom);
  xmax = zoompt.x + (oxmax - oxmin)/(2 * zoom);
  ymin = zoompt.y - (oymax - oymin)/(2 * zoom);
  ymax = zoompt.y + (oymax - oymin)/(2 * zoom);
  calc();
}