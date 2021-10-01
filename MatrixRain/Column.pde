class Column {

  Symbol[] symbols;
  int index;

  int tip, len;
  int totalrows;
  boolean showtip;



  Column(int i, int rows) {
    index = i;
    totalrows = rows;
    showtip = floor(random(0, 4)) == 0;

    symbols = new Symbol[rows+1];
    for (int r = 0; r <= rows; r++) {
      symbols[r] = new Symbol(index, r);
    }
    reset(true);
  }



  void reset(boolean init) {
    tip = init ? floor(random(-totalrows, 0)) : 1;
    len = floor(random(10, totalrows - 8));
  }



  void move() {
    tip++;
    if (tip - len > totalrows) reset(false);
  }


  void change() {
    for (Symbol s : symbols)
      if (random(1) < 0.5)
        s.change();
  }


  void display(float size) {
    for (Symbol s : symbols) {
      if (s.j <= tip && s.j > tip - len) {
        s.display(size, map(tip-s.j, 0, len, 1, 0), showtip && s.j == tip);
      }
    }
  }
}
