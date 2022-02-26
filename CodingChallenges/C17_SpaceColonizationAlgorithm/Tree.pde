class Tree {

  float killDisSq;
  float attractDisSq;
  float branchLen;

  ArrayList<AttractionPoint> aps;
  ArrayList<Branch> branches;

  boolean fullyGrown;


  Tree(float kd, float ad, float bl) {
    killDisSq = kd*kd;
    attractDisSq = ad*ad;
    branchLen = bl;
    fullyGrown = false;

    aps = new ArrayList<AttractionPoint>();
    branches = new ArrayList<Branch>();

    branches.add(new Branch(new PVector(0, 0), new PVector(0, -1)));
  }


  void genAPs(int amount) {
    for (int i = 0; i < amount; i++) {
      aps.add(new AttractionPoint());
    }

    //Pull the trunk upwards
    for (float y = 0; -y < CrownArea.minHeight * height; y -= sqrt(attractDisSq)/4) {
      aps.add(new AttractionPoint(0, y));
    }
  }


  void grow() {
    //Attract branches
    for (AttractionPoint a : aps) {
      if (a.reached) continue;

      //Find closest branch
      float lowestDisSq = 0;
      Branch closestBranch = null;

      for (Branch b : branches) {
        float disSq = PVector.sub(a.pos, b.pos).magSq();

        //AP reached 
        if (disSq <= killDisSq) {
          a.reached = true;
          break;
        }     

        //Ignore
        if (disSq > attractDisSq) continue;

        //Check if closest
        if (closestBranch == null || disSq < lowestDisSq) {
          closestBranch = b;     
          lowestDisSq = disSq;
        }
      }


      //Save attraction;
      if (closestBranch == null) continue;
      PVector aDir = PVector.sub(a.pos, closestBranch.pos);
      closestBranch.attracDir.add(aDir.normalize());
    }

    //Create new branches
    ArrayList<Branch> newbs = new ArrayList<Branch>();
    for (Branch b : branches) {
      if (b.attracDir.magSq() == 0) continue;    //Ignore if unattracted

      Branch newB = new Branch(b, b.attracDir.normalize(), branchLen);
      newbs.add(newB);
      b.attracDir.mult(0);  //Reset attraction
      b.children.add(newB);
    }

    for (Branch b : newbs) branches.add(b);

    if (newbs.size() == 0) fullyGrown = true;
  }



  void display() {
    if (!fullyGrown) {
      for (AttractionPoint ap : aps) {
        ap.display();
      }
    }
    
    for (Branch b : branches) {
      b.display();
    }
  }
}