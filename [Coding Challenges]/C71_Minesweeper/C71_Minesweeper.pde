final int WIDTH = 20;
final int HEIGHT = 10;
final double BOMBRATE = 0.13;

final int SQSIZE = 40;
final int MARGIN = 10;
final int[] TEXT_COLS = new int[] {#1d4991, #057f3a, #ce1208, #60035d, #800000, #42d7f4, #190018, #848484};

Cell[][] cells;
int bombcount;
int gamestate = 0;         // 0 = running, -1 = lost; 1 = won;



void setup() {
    textAlign(CENTER, CENTER);
    textFont(createFont("Snap ITC", 0.8*SQSIZE));
    surface.setSize(WIDTH * SQSIZE + 2 * MARGIN, HEIGHT * SQSIZE + 2 * MARGIN);
    cells = new Cell[WIDTH][HEIGHT];
        
    for (int xi = 0; xi < WIDTH; xi++) {
        for (int yi = 0; yi < HEIGHT; yi++) {
            cells[xi][yi] = new Cell();
            if (random(1) < BOMBRATE) {
                cells[xi][yi].value = -1;
                bombcount++;
            }
        }
    }
    for (int xi = 0; xi < WIDTH; xi++) {
        for (int yi = 0; yi < HEIGHT; yi++) {
            countBombNeighbors(xi, yi);
        }
    } 
                    
}




void draw() {
    background(51);
    textSize(0.8*SQSIZE);
    for (int xi = 0; xi < WIDTH; xi++) {
        for (int yi = 0; yi < HEIGHT; yi++) {
            drawCell(xi, yi);
        }
    }
    
    checkGameState();
    if (gamestate != 0) {
        textSize(0.8*SQSIZE);
        for (int xi = 0; xi < WIDTH; xi++) {
            for (int yi = 0; yi < HEIGHT; yi++) {
                cells[xi][yi].visible = true;
                drawCell(xi, yi);
            }
        }
        
        fill(#FFFFFF, 180);
        rect(0, 0, width, height);
        boolean won = (gamestate == 1);
        fill(won ? #00DD00 : #AA0000);
        textSize(95);
        text(won ? "WON" : "LOST", 0.5*width, 0.45*height);
        noLoop();
    }     
}



void mousePressed() {
    if (gamestate != 0)
        return;
    
    int xi = (int)((mouseX - MARGIN) / SQSIZE);
    int yi = (int)((mouseY - MARGIN) / SQSIZE);
    if (xi < 0 || xi >= WIDTH || yi < 0 || yi >= HEIGHT)
        return;
    
    if (mouseButton == LEFT) {
        reveal(xi, yi);
    } else if (mouseButton == RIGHT) {
        cells[xi][yi].flagged = !cells[xi][yi].flagged;
    }
}




void checkGameState() {
    int hiddencount = 0;
    int correctFlags = 0;
    for (int xi = 0; xi < WIDTH; xi++) {
        for (int yi = 0; yi < HEIGHT; yi++) {
            if (cells[xi][yi].visible && cells[xi][yi].value == -1) {
                gamestate = -1;
                return;
            }
            
            if (!cells[xi][yi].visible)
                hiddencount++;
                if (cells[xi][yi].flagged && cells[xi][yi].value == -1)
                    correctFlags++;
            }
    } 
    
    if (hiddencount == bombcount || correctFlags == bombcount)
        gamestate = 1;
}



void reveal(int x, int y) {
    cells[x][y].visible = true;
    if (cells[x][y].value != 0)
        return;
    
    for (int dx = -1; dx < 2; dx++) {
        if (x + dx < 0 || x + dx >= WIDTH)
            continue;
            
        for (int dy = -1; dy < 2; dy++) {
            if (y + dy < 0 || y + dy >= HEIGHT)
                continue;
            
            if (!cells[x+dx][y+dy].visible)
                reveal(x+dx, y+dy);
        }
    }
}







void drawCell(int x, int y) {
    if (cells[x][y].visible) {
        if (cells[x][y].value == -1) {
            fill(200);
            rect(x * SQSIZE + MARGIN, y * SQSIZE + MARGIN, SQSIZE, SQSIZE);
            fill(0);
            ellipse((x+0.5) * SQSIZE + MARGIN, (y+0.5) * SQSIZE + MARGIN, 0.7*SQSIZE, 0.7*SQSIZE);
        
        }
        else {
            fill(200);
            rect(x * SQSIZE + MARGIN, y * SQSIZE + MARGIN, SQSIZE, SQSIZE);
            if (cells[x][y].value != 0) {
                fill(TEXT_COLS[cells[x][y].value-1]);
                text(cells[x][y].value+"", (x+0.5) * SQSIZE + MARGIN, (y+0.4) * SQSIZE + MARGIN);
            }
        }
    }
    else {
        fill(100);
        rect(x * SQSIZE + MARGIN, y * SQSIZE + MARGIN, SQSIZE, SQSIZE);
        
        if (cells[x][y].flagged) {
                fill(200, 0, 0);
                ellipse((x+0.5) * SQSIZE + MARGIN, (y+0.5) * SQSIZE + MARGIN, 0.5*SQSIZE, 0.5*SQSIZE);
        }
    }
}



void countBombNeighbors(int x, int y) {
    if (cells[x][y].value == -1)
        return;
    
    for (int dx = -1; dx < 2; dx++) {
        if (x + dx < 0 || x + dx >= WIDTH)
            continue;
            
        for (int dy = -1; dy < 2; dy++) {
            if (y + dy < 0 || y + dy >= HEIGHT)
                continue;
            
            if (cells[x+dx][y+dy].value == -1)
                cells[x][y].value++;
        }
    }
}
