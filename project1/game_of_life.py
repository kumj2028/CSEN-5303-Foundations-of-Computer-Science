# https://www.jagregory.com/abrash-black-book/#chapter-17-the-game-of-life

"""
Basic Game of Life program in Python using the Pygame library to draw
"""

# Import and initialize the pygame library
import pygame

pygame.init()

# How quickly should the next generation be created? Time in milliseconds
GEN_INTERVAL = 100

# Create a custom event for next cell generation
NEXTGEN = pygame.USEREVENT + 1
pygame.time.set_timer(NEXTGEN, GEN_INTERVAL)

# cell map displaying constants
CELLMAP_WIDTH = 100
CELLMAP_HEIGHT = 100
CELL_PIXEL_SIZE = 3

# cell colors
LIVE_COLOR = (0, 200, 0)
DEAD_COLOR = (100, 0, 100)

# Set the width and height of the output window, in pixels
WIDTH = (CELLMAP_WIDTH + 2) * (CELL_PIXEL_SIZE + 1)
HEIGHT = (CELLMAP_HEIGHT + 2) * (CELL_PIXEL_SIZE + 1)

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Game of Life')

from cell_map import cellmap

# generates a random cell map
current_map = cellmap(CELLMAP_WIDTH, CELLMAP_HEIGHT, rand=True)

# writing the current_map to a file for debugging purposes
f = open('current_map.txt', 'w')
f.writelines([str(CELLMAP_WIDTH), '\n', str(CELLMAP_HEIGHT), '\n'])
for y in range(CELLMAP_HEIGHT):
    for x in range(CELLMAP_WIDTH):
        f.write(str(current_map.cell_state(x, y)))
    f.write('\n')
f.close()

# keep track of iteration
iter = 0

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Should the next generation be displayed?
        elif event.type == NEXTGEN:
            iter += 1
            current_map = current_map.next_generation()
            # Stop the previous timer by setting the interval to 0
            pygame.time.set_timer(NEXTGEN, 0)
            # Start a new timer
            pygame.time.set_timer(NEXTGEN, GEN_INTERVAL)

    # Check every cell of the entire cell map if it's the first 10 iterations
    if iter < 10:
        for x in range(CELLMAP_WIDTH):
            for y in range(CELLMAP_HEIGHT):
                if current_map.cell_state(x, y):
                    pygame.draw.rect(screen, LIVE_COLOR, pygame.Rect(4 * (x + 1), 4 * (y + 1), CELL_PIXEL_SIZE, CELL_PIXEL_SIZE))
                else:
                    pygame.draw.rect(screen, DEAD_COLOR, pygame.Rect(4 * (x + 1), 4 * (y + 1), CELL_PIXEL_SIZE, CELL_PIXEL_SIZE))
    # Else only draw cells that have changed
    else:
        for x, y in current_map.changed:
            if current_map.cell_state(x, y):
                pygame.draw.rect(screen, LIVE_COLOR, pygame.Rect(4 * (x + 1), 4 * (y + 1), CELL_PIXEL_SIZE, CELL_PIXEL_SIZE))
            else:
                pygame.draw.rect(screen, DEAD_COLOR, pygame.Rect(4 * (x + 1), 4 * (y + 1), CELL_PIXEL_SIZE, CELL_PIXEL_SIZE))

    # Flip the display to make everything appear
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
