WINDOW = 800
CELL_COUNT = 61

cell_size = WINDOW // CELL_COUNT
grid_size = CELL_COUNT * cell_size 
border = cell_size
grid = [[0 for _ in range(CELL_COUNT)] for _ in range(CELL_COUNT)]
light_counter = 0
current_front = []
lightning = None
maze = None


def settings():
    # randomSeed(65536)
    size(grid_size + 2 * border, grid_size + int(1.5*border))
    

def setup():
    global maze
    frameRate(CELL_COUNT // 2)
    maze = compute_maze()
    
    
def draw():     
    global light_counter
    translate(border, border)
    draw_maze_bg()
    
    if not lightning:
        light_counter += 1
        if light_counter == 1:
            start_lightning()
        else:
            update_front()
            check_finished()
        draw_front()
    else:
        frameRate(frameRate * 2)
        update_lightning()
        draw_lightning()
        
    draw_maze(maze)
    
    
def compute_maze():
    # ** Vertical walls between cells in each row / horizontal walls between rows (initially all walls are set)
    verts = [[True for _ in range(CELL_COUNT - 1)] for _ in range(CELL_COUNT)]
    horis = [[True for _ in range(CELL_COUNT)] for _ in range(CELL_COUNT - 1)]
    
    # ** Compute path by connecting cell clusters until there's only one cluster
    maze = {x * CELL_COUNT + y: {(x, y)} for y in range(CELL_COUNT) for x in range(CELL_COUNT)}
    while len(maze) > 1:
        # Pick random cell and random neighbor
        x, y = int(random(CELL_COUNT)), int(random(CELL_COUNT))
        neighbors = get_neighbors(x, y)
        nx, ny = neighbors[int(random(len(neighbors)))]
        
        # Find clusters of both cells (only continue if different clusters)
        cluster = next(idx for idx, cells in maze.items() if (x, y) in cells)
        if (nx, ny) in maze[cluster]:
            continue        
        ncluster = next(idx for idx, cells in maze.items() if (nx, ny) in cells)

        
        # Remove wall of the path connecting both cells
        if y == ny:
            verts[y][min(x, nx)] = False
        elif x == nx:
            horis[min(y, ny)][x] = False
        
        # Update dict to keep track of clusters
        maze[cluster] |= maze[ncluster]
        del maze[ncluster]
    
    # ** Return walls
    return verts, horis


def draw_maze_bg():
    background(30)
    strokeWeight(1)
    fill(60)
    rect(0, 0, grid_size, grid_size)
    
    
def draw_maze(maze):
    # ** Walls
    strokeWeight(1)
    stroke(200)
    verts, horis = maze
    
    # Vertical
    pushMatrix()
    for row in verts:
        pushMatrix()
        for wall in row:
            translate(cell_size, 0)
            if wall:
                line(0, 0, 0, cell_size)
        popMatrix()
        translate(0, cell_size)
    popMatrix()
    
    # Horizontal
    pushMatrix()
    for row in horis:
        translate(0, cell_size)
        pushMatrix()
        for wall in row:
            if wall:
                line(0, 0, cell_size, 0)
            translate(cell_size, 0)
        popMatrix()    
    popMatrix()
    
    # ** Border
    stroke(170)
    strokeWeight(4)
    noFill()
    rect(-2, -2, grid_size+4, grid_size+4)
    noStroke()
    fill(0, 100, 0)
    rect(-border, grid_size, grid_size + 2*border, border//2)
    
    # Cell values
    textAlign(CENTER, CENTER)
    textSize(cell_size // 2.5)
    fill(245, 245, 245, 150)
    for y in range(CELL_COUNT):
        for x in range(CELL_COUNT):
            if grid[x][y] != 0:
                text(grid[x][y], x * cell_size + cell_size // 2, y * cell_size + cell_size // 2)
        

def start_lightning():
    global current_front
    grid[CELL_COUNT // 2][0] = light_counter
    current_front = [(CELL_COUNT // 2, 0)]
    

def update_front():
    global current_front
    verts, horis = maze
    new_front = []
    for x, y in current_front:
        neighbors = get_neighbors(x, y)
        for nx, ny in neighbors:
            if x != nx:
                if not verts[y][min(x, nx)] and grid[nx][y] == 0:
                    grid[nx][y] = light_counter
                    new_front.append((nx, y))
            elif y != ny:
                if not horis[min(y, ny)][x] and grid[x][ny] == 0:
                    grid[x][ny] = light_counter
                    new_front.append((x, ny))
                
    current_front = new_front
    
    
def draw_front():
    if len(current_front) == 0:
        return
    
    min_y = min(y for x, y in current_front) - 1
    max_y = max(y for x, y in current_front)
    noStroke()
    for x, y in current_front:
        trans = map(y, min_y, max_y, 60, 250)
        
        fill(255, 220, 0, trans)
        draw_cell(x, y)
        
        
def check_finished():
    global lightning
    
    for x, y in current_front:
        if y == CELL_COUNT - 1:
            lightning = [(x, y)]
            return
        

def update_lightning():
    global lightning
    
    x, y = lightning[-1]
    counter = grid[x][y]
    if counter == 1:
        return
    
    next_cell = next((nx, ny) for nx, ny in get_neighbors(x, y) if grid[nx][ny] == counter - 1)
    lightning.append(next_cell)
    
    
        
def draw_lightning():
    fill(255, 220, 0)
    for x, y in lightning:
        draw_cell(x, y)
        

def get_neighbors(x, y):
    neighbors = []
    if x != 0: 
        neighbors.append((x - 1, y))
    if x != CELL_COUNT - 1: 
        neighbors.append((x + 1, y)) 
    if y != 0: 
        neighbors.append((x, y - 1))
    if y != CELL_COUNT - 1: 
        neighbors.append((x, y + 1))
        
    return neighbors



def draw_cell(x, y):
    rect(x * cell_size, y * cell_size, cell_size, cell_size, 7, 7, 7, 7)
