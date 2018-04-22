int ROWS = 20, COLS = 20;
int CELLSIZE = 15;

Cell[][] _cells;

Cell _current;
ArrayList<Cell> _path;
int _visited;



void settings() { size(COLS * CELLSIZE + 1, ROWS * CELLSIZE + 1); }

void setup() {
  frameRate(30);
  
  //Cells
  _cells = new Cell[COLS][ROWS];
  for (int i = 0; i < COLS; i++) {
    for (int j = 0; j < ROWS; j++) {
      _cells[i][j] = new Cell(i, j);
    }
  }
  
  _path = new ArrayList<Cell>();
  _current = _cells[0][0];
  _path.add(_current);
}


void draw() {
  //Update
  if (_visited != COLS * ROWS || _path.size() != 0) {
    ArrayList<Cell> neighbors = getUnvisitedNeighbors(_current.i, _current.j);
    
    if (neighbors.size() != 0) {
      Cell chosen = neighbors.get(floor(random(0, neighbors.size())));
      
      _path.add(_current);
      
      if (_current.i - chosen.i == 1) {
        _current.walls[3] = false;
        chosen.walls[1] = false;
      }
      if (_current.i - chosen.i == -1) {
        _current.walls[1] = false;
        chosen.walls[3] = false;
      }
      if (_current.j - chosen.j == 1) {
        _current.walls[0] = false;
        chosen.walls[2] = false;
      }
      if (_current.j - chosen.j == -1) {
        _current.walls[2] = false;
        chosen.walls[0] = false;
      }
      
      
      chosen.visited = true;
      _visited++;
      _current = chosen;
    }
    else if (_path.size() != 0) {
      int lasti = _path.size() - 1;
      _current = _path.get(lasti);
      _path.remove(lasti);
    }
  
    
  
  }
    
  
  //Draw
  background(245);
  for (int i = 0; i < COLS; i++) {
    for (int j = 0; j < ROWS; j++) {
      _cells[i][j].display(CELLSIZE, false, false);
    }
  }
  for (Cell c : _path)
    c.display(CELLSIZE, true, false);
  _current.display(CELLSIZE, true, true);
}



ArrayList<Cell> getUnvisitedNeighbors(int i, int j) {
  ArrayList<Cell> ret = new ArrayList<Cell>();
  
  if (i + 1 != COLS && !_cells[i+1][j].visited) { ret.add(_cells[i+1][j]); }
  if (i - 1 != -1 && !_cells[i-1][j].visited) { ret.add(_cells[i-1][j]); }
  if (j + 1 != ROWS && !_cells[i][j+1].visited) { ret.add(_cells[i][j+1]); }
  if (j - 1 != -1 && !_cells[i][j-1].visited) { ret.add(_cells[i][j-1]); }

  return ret;
}