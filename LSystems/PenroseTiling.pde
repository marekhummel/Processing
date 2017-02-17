class PenroseTiling extends LSystem {

  //Axiom: 
  //[N]++[N]++[N]++[N]++[N]
  //les:
  //M=OA++pA----NA[-OA----MA]++;
  //N=+OA--PA[---MA--NA]+;
  //O=-MA++NA[+++OA++PA]-;
  //P=;
  //A=
  //gle:36


  PenroseTiling() {
    StringDict r = new StringDict();
    r.set("m", "oa++pa----na[-oa----ma]++");
    r.set("n", "+oa--pa[---ma--na]+");
    r.set("o", "-ma++na[+++oa++pa]-");
    r.set("p", "--oa++++ma[+pa++++na]--na");
    r.set("a", "");

    super.init("[n]++[n]++[n]++[n]++[n]", r);
  }

  void setMatrix() {
    translate(width/2, height/2);
  }

  void interpretate(char k) {
    float len = 200 * pow(1/2.0, ls.n);

    switch(k) {
    case 'm':
    case 'n':
    case 'o':
    case 'p':
    case 'a':
      line(0, 0, len, 0);
      translate(len, 0);
      break;
    case '+':
      rotate(-radians(36));
      break;
    case '-':
      rotate(radians(36));
      break;
    case '[':
      pushMatrix();
      break;
    case ']':
      popMatrix();
      break;
    }
  }
}