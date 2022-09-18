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

# font for pygame
pygame_font = pygame.font.Font('WHITRABT.ttf', 30)

# States of the game:
MAIN_MENU = 0
ABOUT = 1
SETTINGS = 2
PLAYING = 3

# Window constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Text constants
WIDTH_TEXT_X = 520
WIDTH_TEXT_Y = 50
HEIGHT_TEXT_X = 520
HEIGHT_TEXT_Y = 100
GENERATION_TEXT_X = 520
GENERATION_TEXT_Y = 150
LIVE_TEXT_X = 520
LIVE_TEXT_Y = 200
DEAD_TEXT_X = 520
DEAD_TEXT_Y = 250
STEADY_TEXT_X = 520
STEADY_TEXT_Y = 300
TEXT_COLOR = (200, 200, 200)

# Button constants
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
NEXT_BUTTON_X = 50
NEXT_BUTTON_Y = 520
AUTO_BUTTON_X = 300
AUTO_BUTTON_Y = 520
BACK_BUTTON_X = 550
BACK_BUTTON_Y = 520
BUTTON_LIGHT = (170, 170, 170)
BUTTON_DARK = (100, 100, 100)
BUTTON_TEXT_COLOR = (0, 255, 0)
BUTTON_TEXT_OFFSET_X = 50
BUTTON_TEXT_OFFSET_Y = 10

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
cell_pixel_size = 4

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
    screen.fill((0, 0, 0))
    current_map = cellmap(cellmap_width, cellmap_height, rand=True)

main_menu.add.button('Play', start_the_game)
main_menu.add.button('About', about_menu)  # Add about submenu
main_menu.add.button('Settings', settings_menu) # Add settings submenu
main_menu.add.button('Quit', pygame_menu.events.EXIT)


# state for checking whether the user wants the next generation to be generated automatically
auto_state = False

def draw_next_button(mouse):
    if NEXT_BUTTON_X <= mouse[0] <= (NEXT_BUTTON_X + BUTTON_WIDTH) \
    and NEXT_BUTTON_Y <= mouse[1] <= (NEXT_BUTTON_Y + BUTTON_HEIGHT):
        pygame.draw.rect(screen, BUTTON_LIGHT, [NEXT_BUTTON_X, NEXT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT])
    else:
        pygame.draw.rect(screen, BUTTON_DARK, [NEXT_BUTTON_X, NEXT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT])
    text = pygame_font.render('NEXT', True, BUTTON_TEXT_COLOR)
    screen.blit(text, (NEXT_BUTTON_X + BUTTON_TEXT_OFFSET_X, NEXT_BUTTON_Y + BUTTON_TEXT_OFFSET_Y))

def draw_auto_button(mouse):
    if AUTO_BUTTON_X <= mouse[0] <= (AUTO_BUTTON_X + BUTTON_WIDTH) \
    and AUTO_BUTTON_Y <= mouse[1] <= (AUTO_BUTTON_Y + BUTTON_HEIGHT):
        pygame.draw.rect(screen, BUTTON_LIGHT, [AUTO_BUTTON_X, AUTO_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT])
    else:
        pygame.draw.rect(screen, BUTTON_DARK, [AUTO_BUTTON_X, AUTO_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT])
    text = pygame_font.render(f'AUTO: {auto_state}', True, BUTTON_TEXT_COLOR)
    screen.blit(text, (AUTO_BUTTON_X + 10, AUTO_BUTTON_Y + BUTTON_TEXT_OFFSET_Y))

def draw_back_button(mouse):
    if BACK_BUTTON_X <= mouse[0] <= (BACK_BUTTON_X + BUTTON_WIDTH) \
    and BACK_BUTTON_Y <= mouse[1] <= (BACK_BUTTON_Y + BUTTON_HEIGHT):
        pygame.draw.rect(screen, BUTTON_LIGHT, [BACK_BUTTON_X, BACK_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT])
    else:
        pygame.draw.rect(screen, BUTTON_DARK, [BACK_BUTTON_X, BACK_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT])
    text = pygame_font.render('BACK', True, BUTTON_TEXT_COLOR)
    screen.blit(text, (BACK_BUTTON_X + BUTTON_TEXT_OFFSET_X, BACK_BUTTON_Y + BUTTON_TEXT_OFFSET_Y))

def draw_width_text():
    text = pygame_font.render(f'Width: {cellmap_width}', True, TEXT_COLOR)
    screen.blit(text, (WIDTH_TEXT_X, WIDTH_TEXT_Y))

def draw_height_text():
    text = pygame_font.render(f'Height: {cellmap_height}', True, TEXT_COLOR)
    screen.blit(text, (HEIGHT_TEXT_X, HEIGHT_TEXT_Y))

def draw_generation_text():
    text = pygame_font.render(f'Generation: {current_map.generation}', True, TEXT_COLOR)
    screen.fill((0, 0, 0), [GENERATION_TEXT_X, GENERATION_TEXT_Y, 300, 300])
    screen.blit(text, (GENERATION_TEXT_X, GENERATION_TEXT_Y))

def draw_live_color():
    text = pygame_font.render('Live Color: ', True, TEXT_COLOR)
    pygame.draw.rect(screen, live_color, [LIVE_TEXT_X + 200, LIVE_TEXT_Y, 20, 20])
    screen.blit(text, (LIVE_TEXT_X, LIVE_TEXT_Y))

def draw_dead_color():
    text = pygame_font.render('Dead Color: ', True, TEXT_COLOR)
    pygame.draw.rect(screen, dead_color, [DEAD_TEXT_X + 200, DEAD_TEXT_Y, 20, 20])
    screen.blit(text, (DEAD_TEXT_X, DEAD_TEXT_Y))

def draw_steady_state():
    text = pygame_font.render(f'Finished: {current_map.steady_state}', True, TEXT_COLOR)
    screen.fill((0, 0, 0), [STEADY_TEXT_X, STEADY_TEXT_Y, 300, 100])
    screen.blit(text, (STEADY_TEXT_X, STEADY_TEXT_Y))

# Run until the user asks to quit
running = True
while running:
    # gets the current mouse position
    mouse = pygame.mouse.get_pos()

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == PLAYING:
                if NEXT_BUTTON_X <= mouse[0] <= (NEXT_BUTTON_X + BUTTON_WIDTH) \
                    and NEXT_BUTTON_Y <= mouse[1] <= (NEXT_BUTTON_Y + BUTTON_HEIGHT):
                    current_map = current_map.next_generation()
                elif AUTO_BUTTON_X <= mouse[0] <= (AUTO_BUTTON_X + BUTTON_WIDTH) \
                    and AUTO_BUTTON_Y <= mouse[1] <= (AUTO_BUTTON_Y + BUTTON_HEIGHT):
                    auto_state = not auto_state
                elif BACK_BUTTON_X <= mouse[0] <= (BACK_BUTTON_X + BUTTON_WIDTH) \
                    and BACK_BUTTON_Y <= mouse[1] <= (BACK_BUTTON_Y + BUTTON_HEIGHT):
                    game_state = MAIN_MENU
                    main_menu.enable()

    if game_state == MAIN_MENU:
        main_menu.mainloop(screen)

    if game_state == PLAYING:
        draw_next_button(mouse)
        draw_auto_button(mouse)
        draw_back_button(mouse)
        draw_width_text()
        draw_height_text()
        draw_generation_text()
        draw_live_color()
        draw_dead_color()
        draw_steady_state()

        # Check every cell of the entire cell map if it's the first 10 iterations
        if current_map.generation == 0:
            for x in range(current_map.width):
                for y in range(current_map.height):
                    if current_map.cell_state(x, y):
                        pygame.draw.rect(screen, live_color, 
                        [(cell_pixel_size + 1) * (x + 1), (cell_pixel_size + 1) * (y + 1), cell_pixel_size, cell_pixel_size])
                    else:
                        pygame.draw.rect(screen, dead_color, 
                        [(cell_pixel_size + 1) * (x + 1), (cell_pixel_size + 1) * (y + 1), cell_pixel_size, cell_pixel_size])
        # Else only draw cells that have changed
        else:
            for x, y in current_map.changed:
                if current_map.cell_state(x, y):
                    pygame.draw.rect(screen, live_color, 
                    [(cell_pixel_size + 1) * (x + 1), (cell_pixel_size + 1) * (y + 1), cell_pixel_size, cell_pixel_size])
                else:
                    pygame.draw.rect(screen, dead_color, 
                    [(cell_pixel_size + 1) * (x + 1), (cell_pixel_size + 1) * (y + 1), cell_pixel_size, cell_pixel_size])

    # Flip the display to make everything appear
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
