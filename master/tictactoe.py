#Written by Charlie Hughes. Since I can't stop you using this, do with it what you will. Also, I know it won't stop you, but don't delete this comment, because I did all the hard work and deserve at least this tiny bit of recognition. Thanks.

#import necessary libraries
import pygame
import random

#initiate pygame
pygame.init()

#setup display window
(width,  height) = (415,  415)
screen = pygame.display.set_mode((width, height))
running = True

#draw ze icon
icon = pygame.image.load('grid.png')
pygame.display.set_icon(icon)

#set colour variables
white = (255,  255,  255)
black = (0,  0,  0)
grey = (128,  128,  128)

#give the display window a title
pygame.display.set_caption('shitty 2048')

#import necessary images
background = pygame.image.load('grid.png')

#not needed at the moment:
coordinates_quoted = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2',  'B3',  'B4', 'C1',  'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4']


#######################################################################################################


#this function just pulls up the background image/the playboard
def draw_background():
    screen.fill(white)
    screen.blit(background,  (0, 0))
    pygame.display.update()
    
def start_game()
    player_tile = raw_input('Choose to be X or O, X goes first. Enter your choice here, by typing X or O:')

def make_move()
    
def sense_move()
    move = raw_input('Your Move: enter a square number, with A1 in the top left corner, and numbers climbing across, letters climbing downwards.')
def update_screen()

def check_win()



while True:
    draw_background()
