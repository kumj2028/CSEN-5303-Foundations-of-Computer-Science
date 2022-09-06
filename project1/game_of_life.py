# https://www.jagregory.com/abrash-black-book/#chapter-17-the-game-of-life

"""
Basic Game of Life program in Python using the Pygame library to draw
"""

# Import and initialize the pygame library
import pygame

pygame.init()

# Set up the clock for keep track of generation frame rate
clock = pygame.time.Clock()

# How quickly should the next generation be created? Time in milliseconds
GEN_INTERVAL = 100

# Create a custom event for next cell generation
NEXTGEN = pygame.USEREVENT + 1
pygame.time.set_timer(NEXTGEN, GEN_INTERVAL)

# cell map displaying constants
CELLMAP_WIDTH = 100
CELLMAP_HEIGHT = 100
CELL_PIXEL_SIZE = 3

# Set the width and height of the output window, in pixels
WIDTH = (CELLMAP_WIDTH + 2) * (CELL_PIXEL_SIZE + 1)
HEIGHT = (CELLMAP_HEIGHT + 2) * (CELL_PIXEL_SIZE + 1)

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Game of Life')

# Import random library since we need to randomly generate a cell map at the start
import random

from cell_map import cellmap

current_map = cellmap(CELLMAP_WIDTH, CELLMAP_HEIGHT)

for x in range(CELLMAP_WIDTH):
    for y in range(CELLMAP_HEIGHT):
        if random.random() > 0.5:
            current_map.turn_cell_on(x, y)

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Should the next generation be displayed?
        elif event.type == NEXTGEN:
            current_map = current_map.next_generation()
            # Stop the previous timer by setting the interval to 0
            pygame.time.set_timer(NEXTGEN, 0)
            # Start a new timer
            pygame.time.set_timer(NEXTGEN, GEN_INTERVAL)

    for x in range(CELLMAP_WIDTH):
        for y in range(CELLMAP_HEIGHT):
            if current_map.cell_state(x, y):
                pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(4 * (x + 1), 4 * (y + 1), CELL_PIXEL_SIZE, CELL_PIXEL_SIZE))
            else:
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(4 * (x + 1), 4 * (y + 1), CELL_PIXEL_SIZE, CELL_PIXEL_SIZE))

    # Flip the display to make everything appear
    pygame.display.flip()

    # Ensure you maintain a 30 frames per second rate
    clock.tick(30)

# Done! Time to quit.
pygame.quit()
