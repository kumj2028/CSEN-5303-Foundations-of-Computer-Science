# https://www.jagregory.com/abrash-black-book/#chapter-17-the-game-of-life

"""
Basic Game of Life program in Python using the Pygame library to draw
"""

# Import libraries
import pygame
import pygame_menu
import random
from cell_map import cellmap

pygame.init()

# States of the game:
MAIN_MENU = 0
ABOUT = 1
SETTINGS = 2
PLAYING = 3

# Initial state should be on the main menu
game_state = MAIN_MENU

# How quickly should the next generation be created? Time in milliseconds
GEN_INTERVAL = 100

# Create a custom event for next cell generation
NEXTGEN = pygame.USEREVENT + 1
pygame.time.set_timer(NEXTGEN, GEN_INTERVAL)

# cell map displaying variables
cellmap_width = random.randint(1, 100)
cellmap_height = random.randint(1, 100)
cell_pixel_size = 3

# cell colors
LIVE_COLOR = (0, 200, 0)
DEAD_COLOR = (100, 0, 100)

# Set up the drawing window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Game of Life')

# generates a random cell map
current_map = cellmap(cellmap_width, cellmap_height, rand=True)

# writing the current_map to a file for debugging purposes
f = open('current_map.txt', 'w')
f.writelines([str(cellmap_width), '\n', str(cellmap_height), '\n'])
for y in range(cellmap_height):
    for x in range(cellmap_width):
        f.write(str(current_map.cell_state(x, y)))
    f.write('\n')
f.close()

# what happens when the user clicks the play button on the main menu
def start_the_game():
    global game_state
    global main_menu
    global current_map
    global cellmap_width
    global cellmap_height
    game_state = PLAYING
    main_menu.disable()
    screen.fill((0, 0, 0))
    current_map = cellmap(cellmap_width, cellmap_height, rand=True)

# what happens when the user clicks the about button on the main menu
def about_the_game():
    # Do the job here !
    pass

# what happens when the user clicks the settings button on the main menu
def set_the_game():
    # Do the job here !
    pass

main_menu = pygame_menu.Menu('Conway\'s Game of Life', 800, 600,
                       theme=pygame_menu.themes.THEME_DARK)

main_menu.add.button('Play', start_the_game)
main_menu.add.button('About', about_the_game)
main_menu.add.button('Settings', set_the_game)
main_menu.add.button('Quit', pygame_menu.events.EXIT)

# state for checking whether the user wants the next generation to be generated automatically
auto_state = False

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Should the next generation be displayed?
        elif event.type == NEXTGEN:
            if game_state == PLAYING and auto_state:
                current_map = current_map.next_generation()
                # Stop the previous timer by setting the interval to 0
                pygame.time.set_timer(NEXTGEN, 0)
                # Start a new timer
                pygame.time.set_timer(NEXTGEN, GEN_INTERVAL)
    if game_state == MAIN_MENU:
        main_menu.mainloop(screen)

    if game_state == PLAYING:
        # Check every cell of the entire cell map if it's the first 10 iterations
        if current_map.generation == 0:
            for x in range(current_map.width):
                for y in range(current_map.height):
                    if current_map.cell_state(x, y):
                        pygame.draw.rect(screen, LIVE_COLOR, pygame.Rect(4 * (x + 1), 4 * (y + 1), cell_pixel_size, cell_pixel_size))
                    else:
                        pygame.draw.rect(screen, DEAD_COLOR, pygame.Rect(4 * (x + 1), 4 * (y + 1), cell_pixel_size, cell_pixel_size))
        # Else only draw cells that have changed
        else:
            for x, y in current_map.changed:
                if current_map.cell_state(x, y):
                    pygame.draw.rect(screen, LIVE_COLOR, pygame.Rect(4 * (x + 1), 4 * (y + 1), cell_pixel_size, cell_pixel_size))
                else:
                    pygame.draw.rect(screen, DEAD_COLOR, pygame.Rect(4 * (x + 1), 4 * (y + 1), cell_pixel_size, cell_pixel_size))

    # Flip the display to make everything appear
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
