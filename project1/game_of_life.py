# https://www.jagregory.com/abrash-black-book/#chapter-17-the-game-of-life

"""
Basic Game of Life program in Python using the Pygame library to draw
"""

# Import libraries
from email import message
import pygame
import pygame_menu
import random
from cell_map import cellmap
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw() #to hide the main window

pygame.init()

# States of the game:
MAIN_MENU = 0
ABOUT = 1
SETTINGS = 2
PLAYING = 3

# Window constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

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
live_color = (0, 200, 0)
dead_color = (100, 0, 100)

# Set up the drawing window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
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

about_menu = pygame_menu.Menu('About', WINDOW_WIDTH, WINDOW_HEIGHT,
                       theme=pygame_menu.themes.THEME_DARK)
about_menu.add.label('This is a programming project for the course')
about_menu.add.label('Foundations of Computer Science at TAMUK.')
about_menu.add.label('The Game of Life is a 2D simulation of cells')
about_menu.add.label('that live or die in successive generations.')
about_menu.add.label('Only the starting state of the cells is needed')
about_menu.add.label('to produce the next generation, so this is not')
about_menu.add.label('very interactive beyond setting initial conditions.')
about_menu.add.label('The authors are Ameya Khot and Mengxiang Jiang.')

about_menu.add.label('')
about_menu.add.button('Back', pygame_menu.events.BACK)

settings_menu = pygame_menu.Menu('Settings', WINDOW_WIDTH, WINDOW_HEIGHT,
                       theme=pygame_menu.themes.THEME_DARK)
def check_cellmap_width(value):
    global cellmap_width
    if value < 0:
        messagebox.showerror('Invalid width', 'value must be positive')
    elif value > 100:
        messagebox.showerror('Invalid width', 'value must be less than 100')
    else:
        cellmap_width = value

settings_menu.add.text_input(
    'Width: ',
    default=cellmap_width,
    onchange=check_cellmap_width,
    input_type=pygame_menu.locals.INPUT_INT,
    textinput_id='cellmap_width'
)

def check_cellmap_height(value):
    global cellmap_height
    if value < 0:
        messagebox.showerror('Invalid height', 'value must be positive')
    elif value > 100:
        messagebox.showerror('Invalid height', 'value must be less than 100')
    else:
        cellmap_height = value

settings_menu.add.text_input(
    'Height: ',
    default=cellmap_height,
    onchange=check_cellmap_height,
    input_type=pygame_menu.locals.INPUT_INT,
    textinput_id='cellmap_height'
)

def check_live_color(value):
    global live_color
    global dead_color
    if value == dead_color:
        messagebox.showerror('Invalid live color', 'color must be different from dead color')
    else:
        live_color = value

settings_menu.add.color_input(
    'Live Color (R,G,B): ',
    default=live_color,
    color_type=pygame_menu.widgets.COLORINPUT_TYPE_RGB,
    onchange=check_live_color,
    color_id='live_color'
    )

def check_dead_color(value):
    global live_color
    global dead_color
    if value == live_color:
        messagebox.showerror('Invalid dead color', 'color must be different from livecolor')
    else:
        dead_color = value

settings_menu.add.color_input(
    'Dead Color (R,G,B): ',
    default=dead_color,
    color_type=pygame_menu.widgets.COLORINPUT_TYPE_RGB,
    onchange=check_dead_color,
    color_id='dead_color'
    )

settings_menu.add.button('Back', pygame_menu.events.BACK)

main_menu = pygame_menu.Menu('Conway\'s Game of Life', WINDOW_WIDTH, WINDOW_HEIGHT,
                       theme=pygame_menu.themes.THEME_DARK)

def start_the_game():
    global game_state
    global main_menu
    global game_menu
    global current_map
    global cellmap_width
    global cellmap_height
    game_state = PLAYING
    main_menu.disable()
    game_menu.enable()
    screen.fill((0, 0, 0))
    current_map = cellmap(cellmap_width, cellmap_height, rand=True)

main_menu.add.button('Play', start_the_game)
main_menu.add.button('About', about_menu)  # Add about submenu
main_menu.add.button('Settings', settings_menu) # Add settings submenu
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
                        pygame.draw.rect(screen, live_color, pygame.Rect(4 * (x + 1), 4 * (y + 1), cell_pixel_size, cell_pixel_size))
                    else:
                        pygame.draw.rect(screen, dead_color, pygame.Rect(4 * (x + 1), 4 * (y + 1), cell_pixel_size, cell_pixel_size))
        # Else only draw cells that have changed
        else:
            for x, y in current_map.changed:
                if current_map.cell_state(x, y):
                    pygame.draw.rect(screen, live_color, pygame.Rect(4 * (x + 1), 4 * (y + 1), cell_pixel_size, cell_pixel_size))
                else:
                    pygame.draw.rect(screen, dead_color, pygame.Rect(4 * (x + 1), 4 * (y + 1), cell_pixel_size, cell_pixel_size))

    # Flip the display to make everything appear
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
