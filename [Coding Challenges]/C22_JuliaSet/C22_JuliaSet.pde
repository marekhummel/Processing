float cre, cim;

int iter = 100;
int[][] pts;
color[] gradient;



void setup() {
  size(600, 400);
  pts = new int[width+1][height+1];
  setGradient();
}


void draw() {
  cre = map(mouseX, 0, width, -2, 2);
  cim = map(mouseY, 0, height, 1, -1);

  
  loadPixels(); 
  for (float x = -2; x < 2; x += 4.0/width) {
    for (float y = -1; y < 1; y += 2.0/height) {
      int i;
      float re = x, im = y;
      for (i = 0; i < iter; i++) {
        float nre = re*re - im*im + cre; 
        float nim = 2 * re * im + cim;
        re = nre;
        im = nim;
        if (re*re + im*im > 4) break;
      }

      int scx = floor(map(x, -2, 2, 0, width-1));
      int scy = floor(map(y, -1, 1, height-1, 0));
      pixels[scy * width + scx] = color(sqrt(float(i) / iter) * 255); //gradient[i % gradient.length];
    }
  }
  updatePixels();
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