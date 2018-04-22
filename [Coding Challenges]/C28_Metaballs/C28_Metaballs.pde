//https://www.gamedev.net/resources/_/technical/graphics-programming-and-theory/exploring-metaballs-and-isosurfaces-in-2d-r2556


Metaball[] blobs;
float scl = 5;

void setup() {
  size(640, 480);
  colorMode(HSB);
  blobs = new Metaball[3];
  for (int i = 0; i < blobs.length; i++) { blobs[i] = new Metaball(); }
}



void draw() {
  for(Metaball b : blobs) { b.move(); }
  
  loadPixels();
  for (int x = 0; x < width; x++) {
    for (int y = 0; y < height; y++) {
      float val = 0;
      for(Metaball b : blobs) { val += b.func(x, y) * b.radius; }
      
      int index = y * width + x;
      pixels[index] = color(val * scl, 255, 255);
    }
  }
  updatePixels();
}