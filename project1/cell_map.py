"""
cell map class for keeping track of cells for game of life
"""
# Import random library since we need to randomly generate a cell map at the start
import random

class cellmap:
    ADJACENT = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    # cellmap constructor
    def __init__(self, width, height, rand=False):
        self.width = width
        self.height = height
        self.cells = [[0]*height for i in range(width)]
        self.changed = []
        self.generation = 0
        self.steady_state = False
        if rand:
            for x in range(width):
                for y in range(height):
                    if random.random() > 0.5:
                        self.turn_cell_on(x, y)
    
    # turns cell on
    def turn_cell_on(self, x, y):
        self.cells[x][y] = 1
    
    # turns cell off
    def turn_cell_off(self, x, y):
        self.cells[x][y] = 0

    # returns the cell state
    def cell_state(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.cells[x][y]
        else:
            return 0
    
    # count the number of neighbors on of a given cell
    def count_on_neighbors(self, x, y):
        neighbor_count = 0
        for i, j in self.ADJACENT:
            neighbor_count += self.cell_state(x + i, y + j)
        return neighbor_count

    # returns the next generation cell map
    def next_generation(self):
        if self.steady_state:
            return self
        else:
            next_map = cellmap(self.width, self.height)

            for x in range(self.width):
                for y in range(self.height):
                    neighbor_count = self.count_on_neighbors(x, y)
                    # if the cell is on, turn it off if it has too many or too few on neighbors
                    if self.cell_state(x, y):
                        if neighbor_count < 2 or neighbor_count > 3:
                            next_map.turn_cell_off(x, y)
                            next_map.changed.append((x, y))
                        else:
                            next_map.turn_cell_on(x, y)
                    # if the cell is off, turn it on if it has enough on neighbors
                    else:
                        if neighbor_count == 3:
                            next_map.turn_cell_on(x, y)
                            next_map.changed.append((x, y))
            if len(next_map.changed) == 0:
                self.steady_state = True
                return self
            else:
                next_map.generation = self.generation + 1
                return next_map