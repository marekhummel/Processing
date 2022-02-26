class Ball {
 int x, y;
 private int r;
 double speedx, speedy;
  
 public Ball(int x, int y) {
   this.x = x;
   this.y = y;
   this.r = 8;
   
   this.speedx = random(-1, 1);
   this.speedy = random(-1, 1);
   double scalar = 2.5 / Math.sqrt(speedx*speedx + speedy*speedy);
   this.speedx *= scalar;
   this.speedy *= scalar;
 }

 
 
 void update() {
   this.x += this.speedx;
   this.y += this.speedy;
 }
 

 
 
 void draw() {
   noStroke();
   fill(255);
   ellipse(x, y, r<<1, r<<1);
 }
 
}
