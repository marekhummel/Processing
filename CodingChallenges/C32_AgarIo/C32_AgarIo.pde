Cell me;
ArrayList<Cell> food;
float res = 30;

void setup() {
  size(600, 600);
  colorMode(HSB);

  me = new Cell(0, 0, 32, true);

  food = new ArrayList<Cell>();
  for (int i = 0; i < 200; i++) {
    food.add(new Cell(random(-2 * width, 2 * width), random(-2*height, 2*height), 8, false));
  }
}



void draw() {
  me.move();
  translate(width/2, height/2);
  translate(-me.pos.x, -me.pos.y);

  background(245);
  stroke(0);
  strokeWeight(4);
  noFill();
  rect(-2*width, -2*height, 4*width, 4*height); 

  stroke(0, 100);
  strokeWeight(1);
  float ex = 5;
  float startx = me.pos.x - width/2 - me.pos.x % res - ex * res;
  float starty = me.pos.y - height/2 - me.pos.y % res - ex * res;
  for (int i = 0; i < width/res + 2*ex; i++) {
    line(startx, starty + i*res, startx + width + 2*ex*res, starty + i*res);
    line(startx + i*res, starty, startx + i*res, starty + height + 2*ex*res);
  }


  me.move();
  for (int i = food.size()-1; i >=0; i--) {
    Cell f = food.get(i);
    if (me.eat(f)) {
      food.remove(i);
      food.add(new Cell(random(-2 * width, 2 * width), random(-2*height, 2*height), 8, false));
      continue;
    }
    f.display();
  }
  me.display();
}