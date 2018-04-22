PVector[] cities;
int offset = 50;
int total;
int[] perm, best;
float bestdis = 10000000;


void setup() {
  size(600, 600);

  cities = new PVector[8];
  for (int i = 0; i < cities.length; i++) {
    cities[i] = new PVector(random(offset, width-offset), random(offset, height-offset));
  }


  perm = new int[cities.length];
  for (int i = 0; i < perm.length; i++) perm[i] = i;
  best = perm.clone();
  total = fact(perm.length);
}




void draw() {
  background(51);

  //Best Path
  stroke(255, 0, 0, 80);
  strokeWeight(12);
  noFill();
  beginShape();
  for (int i : best) vertex(cities[i].x, cities[i].y);
  endShape();

  //Path
  stroke(255);
  strokeWeight(3);
  noFill();
  beginShape();
  for (int i : perm) vertex(cities[i].x, cities[i].y);
  endShape();

  //Cities
  stroke(255);
  strokeWeight(2);
  fill(0);
  for (int i = 0; i < cities.length; i++) {
    ellipse(cities[i].x, cities[i].y, 20, 20);
  }



  //Update
  float dis = 0;
  for (int i = 0; i < perm.length-1; i++) dis += cities[perm[i]].dist(cities[perm[i+1]]); 

  if (dis < bestdis) {
    bestdis = dis;
    best = perm.clone();
  }


  stroke(255);
  fill(255);
  textSize(15);
  text(p(perm) + "    " + dis, 10, 20);
  text(p(best) + "    " + bestdis, 10, 40);

  if (frameCount == total) noLoop();
  else nextPerm();
}




void nextPerm() {
  //https://www.quora.com/How-would-you-explain-an-algorithm-that-generates-permutations-using-lexicographic-ordering
  int x, y;
  for (x = perm.length - 2; x >= 0; x--) {
    if (perm[x] < perm[x+1]) break;
  }
  for (y = perm.length - 1; y > x; y--) {
    if (perm[x] < perm[y]) break;
  }

  int temp = perm[y];
  perm[y] = perm[x];
  perm[x] = temp;

  for (int i = x+1; i <= floor((perm.length-x-1)/2) + x; i++) {
    temp = perm[perm.length-(i-x)];
    perm[perm.length-(i-x)] = perm[i];
    perm[i] = temp;
  }
}


int fact(int num) {
  return num == 1? 1 : fact(num - 1)*num;
}

String p(int[] a) {
  String s = "";
  for (int i : a) {
    s += i+" | ";
  }
  return s.substring(0, s.length()-3);
}