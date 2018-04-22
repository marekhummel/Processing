class Paddle {
 int x, y;
 private int width, height;
  
 public Paddle(int x, int y) {
   this.x = x;
   this.y = y;
   this.width = 10;
   this.height = 70;
 }
 
 
 
 
 void draw() {
   noStroke();
   fill(255);
   rect(x, y, width, height);
 }
 
}
