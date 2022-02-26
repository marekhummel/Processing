class RainDrop {
  
  float ACC = 0.1;
  float HUE = 270;
  
  float x,y;
  float volume, len, thickness, brightness;
  float vel;
  
  
  RainDrop() {
    x = random(-width/2, width/2);
    y = random(-height/2 - 100, -height/2);
    
    vel = random(1, 10);
    
    volume = random(3, 15);  
    brightness = random(30, 65);
  }


  void update() {
    y += vel;
    vel += ACC;
    
    len = map(vel, 0, 15, sqrt(volume), volume);
    thickness = volume/len;
  }
  
  
  void display() {
    strokeWeight(thickness);
    stroke(HUE, 100, brightness);
    line(x, y, x, y - len);
  }


}