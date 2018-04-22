Ball b;
Paddle pl, pr;
int scoreL, scoreR;


void setup() {
  size(400, 400);
  
  rectMode(CENTER);
  b = new Ball(width>>1, height>>1);
  pl = new Paddle((int)(0.05 * width), height>>1);
  pr = new Paddle((int)(0.95 * width), height>>1);
}




void draw() {
  // Update
  b.update();
  updatePaddles();
  deflectBall();
  score();

  
  // Draw
  background(51);
  b.draw();
  pl.draw();
  pr.draw();
  
  textAlign(LEFT, TOP);
  text(scoreL, 0, 0);
  textAlign(RIGHT, TOP);
  text(scoreR, width, 0);
}



void updatePaddles() {
  if (key == CODED) {
    switch (keyCode) {
      case UP:
        pl.y--;
        break;
      case DOWN:
        pl.y++;
        break;
    }
  }
}

void deflectBall() {
  // Walls
  if (b.y + b.r >= height || b.y - b.r <= 0)
    b.speedy *= -1;
    
    
  // Paddles
  if (b.x - b.r <= pl.x + (pl.width>>1)) {
    if (b.y <= pl.y + (pl.height>>1) && b.y >= pl.y - (pl.height>>1))
      b.speedx *= -1;
  }
  else if (b.x + b.r >= pr.x - (pr.width>>1)) {
    if (b.y <= pr.y + (pr.height>>1) && b.y >= pr.y - (pr.height>>1))
      b.speedx *= -1;
  }
}



void score() { 
  if (b.x + b.r >= width)
    scoreL++;
  if (b.x - b.r <= 0)
    scoreR++;
    
  if (b.x + b.r >= width || b.x - b.r <= 0)
    b = new Ball(width>>1, height>>1);
}
