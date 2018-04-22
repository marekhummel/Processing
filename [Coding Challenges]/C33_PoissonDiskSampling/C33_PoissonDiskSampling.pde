//http://www.cs.ubc.ca/~rbridson/docs/bridson-siggraph07-poissondisk.pdf

float r = 15;
int k = 30;
float cs = r / sqrt(2);

int rows, cols;
PVector[] grid;
ArrayList<PVector> active;



void setup() {
  size(600, 600);

  cols = ceil(width / cs);
  rows = ceil(height / cs);

  grid = new PVector[cols * rows];
  active = new ArrayList<PVector>();  

  PVector x0 = new PVector(width/2, height/2);
  grid[gridindex(x0)] = x0;
  active.add(x0);

  background(0);
  noFill();
  strokeWeight(0.5 * r);
  stroke(255);
}


void draw() {
  int idx = floor(random(active.size()));
  PVector apt = active.get(idx);

  boolean foundnew = false;
  for (int i = 0; i < k; i++) {
    PVector npt = PVector.add(apt, PVector.random2D().setMag(random(r, 2*r)));
    if (npt.x > cs * cols || npt.x < 0 || npt.y < 0 || npt.y > cs * rows) continue;
    if (grid[gridindex(npt)] != null) continue;

    ArrayList<PVector> neighbors = getNeighbors(gridindex(npt));
    boolean tooclose = false;
    for (PVector n : neighbors) { 
      tooclose |= (PVector.dist(npt, n) < r);
    }

    if (!tooclose) {
      point(npt.x, npt.y);
      grid[gridindex(npt)] = npt;
      active.add(npt);
      foundnew = true;
      break;
    }
  }

  if (!foundnew) active.remove(idx);

  if (active.size() == 0) { 
    noLoop();
    println("FINISHED");
  }
}


int gridindex(PVector p) {
  return floor(p.x / cs) + floor(p.y / cs) * cols;
}



ArrayList<PVector> getNeighbors(int idx) {
  ArrayList<PVector> ret = new ArrayList<PVector>();

  boolean top = idx >= cols;
  boolean bottom = idx < (rows * cols - cols);
  boolean left = (idx % cols) != 0;
  boolean right = (idx % cols) != (cols-1);

  if (top && left)      ret.add(grid[idx - 1 - cols]);
  if (top && right)     ret.add(grid[idx + 1 - cols]);
  if (bottom && left)   ret.add(grid[idx - 1 + cols]);
  if (bottom && right)  ret.add(grid[idx + 1 + cols]); 
  if (top)              ret.add(grid[idx - cols]);
  if (left)             ret.add(grid[idx - 1]);
  if (bottom)           ret.add(grid[idx + cols]);
  if (right)            ret.add(grid[idx + 1]);

  for (int i = ret.size() - 1; i >= 0; i--) {
    if (ret.get(i) == null) ret.remove(i);
  }
  return ret;
}