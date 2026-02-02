class Cell:
    value: int = 0  # n > 0 = #Bombs in neighborhood, -1 = BOMB
    visible: bool = False
    flagged: bool = False
