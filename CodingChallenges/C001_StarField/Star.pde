class Star {

  float x, y, z;
  float sx, sy;
  float px, py;
  float speed = 5;

  
  Star() {
    x = random(-width/2, width/2);
    y = random(-height/2, height/2);
    z = random(width/2);

    sx = map(x / z, 0, 1, 0, width/2);
    sy = map(y / z, 0, 1, 0, height/2);
  }




  void update() {
    z = z - speed;
    
    
    px = sx;
    py = sy;
    sx = map(x / z, 0, 1, 0, width/2);
    sy = map(y / z, 0, 1, 0, height/2);

    
    if (sx < -width/2 || sx > width/2 || sy < -height/2 || sy > height/2) {
      z = random(width/2);
      sx = map(x / z, 0, 1, 0, width/2);
      sy = map(y / z, 0, 1, 0, height/2);
      px = sx;
      py = sy;
    }
  }
  
  
  
  void show() {
   
    noStroke();
    fill(255);
    
    float r = map(z, width/2, 1, 0, 3);
    ellipse(sx, sy, r, r);
    
    stroke(255);
    line(sx, sy, px, py);
  }

}