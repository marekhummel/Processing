float symbolsize = 15;
int cols, rows;
Column[] columns;


void setup() {
  size(600, 450);
  //fullScreen();
  smooth();
  cols = floor(width / symbolsize);
  rows = floor(height / symbolsize);

  columns = new Column[cols];
  for (int c = 0; c < cols; c++) {
    columns[c] = new Column(c, rows);
  }

  textFont(createFont("Arial Unicode MS", symbolsize, false));
}




void draw() {
  background(0);
  for (Column c : columns) c.display(symbolsize);


  for (Column c : columns) {
    if (frameCount % 2 == 0) c.move();
    if (frameCount % 3 == 0) c.change();
  }
}