"""
cell map class for keeping track of cells for game of life
"""

# Import copy library since we need to deep copy the current cell map into the next cell map
import copy

class cellmap:
    ADJACENT = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    # cellmap constructor
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0]*width for i in range(height)]

    # deep copies the cells from the source map to the current map
    def copy_cells(self, source_map):
        self.cells = copy.deepcopy(source_map.cells)
    
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
        next_map = cellmap(self.width, self.height)
        next_map.copy_cells(self)

        for x in range(self.width):
            for y in range(self.height):
                neighbor_count = self.count_on_neighbors(x, y)
                # if the cell is on, turn it off if it has too many or too few on neighbors
                if self.cell_state(x, y):
                    if neighbor_count < 2 or neighbor_count > 3:
                        next_map.turn_cell_off(x, y)
                # if the cell is off, turn it on if it has enough on neighbors
                else:
                    if neighbor_count == 3:
                        next_map.turn_cell_on(x, y)
        return next_map