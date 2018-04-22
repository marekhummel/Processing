String token;
String[] filenames;
String[][] docs;

void setup() {
  size(600, 600);
  filenames = new File(sketchPath() + "\\data").list();
  loadDocs();

  for (int i = 0; i < 1; i++) {
    String[] doc = docs[i];

    FloatDict weights = new FloatDict();
    for (String word : doc) {
      if (weights.hasKey(word)) continue;

      float tfidf = tf(word, i) * idf(word);
      println(word +": " + tf(word, i ) );
      weights.add(word, tfidf);
    }
    weights.sortValues();
    println(filenames[i]);
    for (int k = 0; k < weights.size(); k++) {
      //println("\t" + weights.key(k) + ": " + nf(weights.value(k), 1, 9));
    }
    println();
  }
}


void loadDocs() {
  docs = new String[filenames.length][];
  for (int i = 0; i < filenames.length; i++) {
    String file = join(loadStrings(filenames[i]), "\n");
    String[] words = splitTokens(file, "\n .,?!:;()");
    docs[i] = words;
  }
}


float tf(String word, int docidx) {
  String[] words = docs[docidx];
  int count = 0;
  for (String w : words) {
    if (w == word) count++;
  }
  return float(count); ///words.length;
}




float idf(String word) {
  int count = 0;
  for (String[] doc : docs) {
    boolean contains = false;
    for (String w : doc) contains |= (w == word);
    if (contains) count++;
  }

  return log(docs.length / float(1 + count)) / log(10);
}