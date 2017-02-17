class LSystem {
  
  String currentState;
  StringDict rules;
  int n;
  
  LSystem(String axiom, StringDict rules_) {
    currentState = axiom;
    rules = rules_;
    n = 0;  
  }

  
  void produce() {
    String newState = "";
    for (int i = 0; i < currentState.length(); i++) {
      String c = str(currentState.charAt(i));
      
      boolean found = false;
      for(String k : rules.keyArray()) {
        if (c.equals(k)) {
          newState += rules.get(k);
          found = true;
          break;
        }
      }
      if (!found) newState += c;
    }
  
    currentState = newState;
    n++;
  }





}