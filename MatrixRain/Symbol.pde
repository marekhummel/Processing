class Symbol {

  int i, j;
  String value;


  Symbol(int i_, int j_) {
    i = i_;
    j = j_;

    int charval = 0x30A0 + floor(random(0, 96));
    value = new String(Character.toChars(charval));
  }


  void change() {
    int charval = 0x30A0 + floor(random(0, 96));
    value = new String(Character.toChars(charval));
  }


  void display(float size, float alpha, boolean hl) {
    if (hl) fill(230, 255, 230, alpha*255) ; 
    else fill(0, 255, 70, alpha*255);
    textSize(size);
    text(value, i * size, j * size);
    textSize(size+2);
    fill(200, 100);
    text(value, i * size - 1, j * size - 1);
  }
}