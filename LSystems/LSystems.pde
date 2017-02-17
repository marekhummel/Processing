LSystem ls;

void setup() {
  size(500, 500);

  //ls = new FractalTree();
  //ls = new KochCurve();
  //ls = new SierpinskiTriangle();
  //ls = new SierpinskiCurve();
  //ls = new DragonCurve();
  //ls = new FractalPlant();
  //ls = new HexagonalGosper();
  ls = new PenroseTiling();

  frameRate(1);
}


void draw() {
  background(0);
  println(ls.n);
  
  stroke(255, 100);
  
  ls.setMatrix();
  

  for (int i = 0; i < ls.currentState.length(); i++) {
    ls.interpretate(ls.currentState.charAt(i));
  }

  ls.produce();
}