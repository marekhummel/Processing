float cre, cim;

int iter = 100;
int[][] pts;
int[] gradient;



void setup() {
  size(600, 400);
  pts = new int[width+1][height+1];
  setGradient();
  calc();
}


void draw() {
  cre = map(mouseX, 0, width, -2, 2);
  cim = map(mouseY, 0, height, 1, -1);
  calc();
  
  noStroke();  
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

      int scx = floor(map(x, -2, 2, 0, width));
      int scy = floor(map(y, -1, 1, height, 0));

      int rgb = gradient[i % gradient.length];
      int r = (rgb >> 16) & 0xFF, g = (rgb >> 8) & 0xFF, b = rgb & 0xFF;
      fill(r, g, b);
      rect(scx, scy, 1, 1);
    }
  }
}




void calc() {

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