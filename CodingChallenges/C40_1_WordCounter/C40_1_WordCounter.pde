String filename = "eclipse.txt";
IntDict counter;

void setup() {
  size(700, 600);

  String file = join(loadStrings(filename), "\n");
  String[] words = splitTokens(file, "\n .,?!:;");
  counter = countWords(words);
}




void draw() {
  background(51);

  noStroke();
  fill(255);
  textSize(14);
  text(filename, 10, 20);


  float wordcount = counter.size();
  float ts = (height-20) / wordcount;

  strokeWeight(ts/3.0);
  textSize(ts);
  float maxwidth = maxTextWidth(counter.keyArray());
  translate(width-maxwidth, height-5);
  for (int i = 0; i < wordcount; i++) {
    float y = -i*ts;

    noFill();
    stroke(255);
    float end = PI+HALF_PI*(counter.value(i)/(counter.maxValue()*1.03));
    float r = i*ts+ts/4;
    arc(-15, 0, 2*r, 2*r, PI, end);

    fill(255);
    noStroke();
    text(counter.key(i), -10, y);
    
    end+=PI/(r/2);
    text(counter.value(i), -15 + r*cos(end) - ts/2, r*sin(end)); 
  }
}











IntDict countWords(String[] words) {
  IntDict counter = new IntDict();

  for (String w : words) {
    if (!counter.hasKey(w)) {
      counter.add(w, 0);
    }
    counter.increment(w);
  }

  counter.sortValues();
  return counter;
}



float maxTextWidth(String[] texts) {
  float max = 0;
  for (String t : texts) {
    float tw = textWidth(t);
    if (tw > max) max = tw;
  }
  return max;
} 