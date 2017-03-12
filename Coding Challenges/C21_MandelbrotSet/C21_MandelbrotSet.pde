int iter = 256;

float oxmin = -2.5;
float oxmax = 1;
float oymin = -1;
float oymax = 1;
float xmin, xmax, ymin, ymax;

PVector zoompt;
float zoom = 1;

int[][] pts;
color[] gradient;



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
  //zoomIn();

  loadPixels();
  for (int x = 0; x < width; x++) {
    for (int y = 0; y < height; y++) {
      pixels[y * width + x] = color(pts[x][y]);//gradient[pts[x][y]];
    }
  }
  updatePixels();
}


void mousePressed() {
  zoomIn();
}


void setGradient() {
  gradient = new color[16];
  gradient[0] = color(0, 0, 0);
  gradient[1] = color(25, 7, 26);
  gradient[2] = color(9, 1, 47);
  gradient[3] = color(4, 4, 73);
  gradient[4] = color(0, 7, 100);
  gradient[5] = color(12, 44, 138);
  gradient[6] = color(24, 82, 177);
  gradient[7] = color(57, 125, 209);
  gradient[8] = color(134, 181, 229);
  gradient[9] = color(211, 236, 248);
  gradient[10] = color(241, 233, 191);
  gradient[11] = color(248, 201, 95);
  gradient[12] = color(255, 170, 0);
  gradient[13] = color(204, 128, 0);
  gradient[14] = color(153, 87, 0);
  gradient[15] = color(106, 52, 3);
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
      pts[scx][scy] = floor(sqrt(float(i) / iter) * 255);//i % gradient.length;
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