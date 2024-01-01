import pygame
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)

# Text values
TEXT_X = 300
TEXT_Y = 50

# PROBLEM CONSTS
CALCULATION_RATE = 1000  # number of physics frames per second
PUPPY_SPEED = 400/CALCULATION_RATE  # in pixels per second
HUNTRESS_SPEED = 200/CALCULATION_RATE  # in pixels per second
HUT_POS_X = WIDTH-80
HUT_POS_Y = 400
GRASS_POS_Y = 445

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Huntress and her Puppy")

# Load the image
puppy_img = pygame.image.load("images/puppy80x80.png")  # Image of the puppy
huntress_img = pygame.image.load("images/huntress100x200.png")  # Image of the huntress
hut_img = pygame.image.load("images/hut100x100.png")  # Image of the hut
grass1_img = pygame.image.load("images/grass1_60x80.png")  # Grass image for background
grass1f_img = pygame.transform.flip(grass1_img, True, False)  # Flipped grass image for background
grass2_img = pygame.image.load("images/grass2_60x80.png")  # Grass image for background
grass2f_img = pygame.transform.flip(grass2_img, True, False)  # Flipped grass image for background


# Get the image's rect (position and dimensions)
puppy_rect = puppy_img.get_rect()
huntress_rect = huntress_img.get_rect()
hut_rect = hut_img.get_rect()

# Initial position and speed
puppy_x = 50  # Start from left
puppy_y = 400  # Center vertically
puppy_speed = PUPPY_SPEED  # Adjust the speed as needed (above)

huntress_x = 50  # Start from left
huntress_y = 290  # Center vertically
huntress_speed = HUNTRESS_SPEED  # Adjust the speed as needed (above)

punch_sound = pygame.mixer.Sound("sounds/punch.mp3")

font = pygame.font.Font(None, 36)
text = font.render("UBC PHYS100 Tutorial (Musaab Faozi)", True, (0, 0, 0))

# Main game loop
running = True
next_collision_X = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for boundary collisions (left and right)
    if puppy_x >= HUT_POS_X:
        puppy_img = pygame.transform.flip(puppy_img, True, False)
        puppy_speed = -PUPPY_SPEED
        punch_sound.play()
    
    elif np.abs(puppy_x - huntress_x) <= 1 and puppy_speed < 0:
        puppy_img = pygame.transform.flip(puppy_img, True, False)
        puppy_speed = PUPPY_SPEED
        punch_sound.play()
    
    if huntress_x >= HUT_POS_X:
        huntress_speed = 0

    # Update the image's position
    puppy_x += puppy_speed
    huntress_x += huntress_speed

    # Fill the screen with a white background
    screen.fill(WHITE)

    # Blit (draw) the image onto the screen at the new position
    screen.blit(grass1_img, (50, GRASS_POS_Y))
    screen.blit(grass1_img, (0, GRASS_POS_Y))
    screen.blit(grass2f_img, (100, GRASS_POS_Y))
    screen.blit(grass2_img, (150, GRASS_POS_Y))
    screen.blit(grass1_img, (200, GRASS_POS_Y))
    screen.blit(grass2f_img, (250, GRASS_POS_Y))
    screen.blit(grass1f_img, (300, GRASS_POS_Y))
    screen.blit(grass2f_img, (350, GRASS_POS_Y))
    screen.blit(grass1f_img, (400, GRASS_POS_Y))
    screen.blit(grass2f_img, (450, GRASS_POS_Y))
    screen.blit(grass1_img, (500, GRASS_POS_Y))
    screen.blit(grass2_img, (550, GRASS_POS_Y))
    screen.blit(grass1f_img, (600, GRASS_POS_Y))
    screen.blit(grass2_img, (650, GRASS_POS_Y))
    screen.blit(grass1f_img, (700, GRASS_POS_Y))
    screen.blit(grass2f_img, (750, GRASS_POS_Y))
    screen.blit(grass1_img, (800, GRASS_POS_Y))
    screen.blit(grass2f_img, (850, GRASS_POS_Y))
    screen.blit(hut_img, (HUT_POS_X, HUT_POS_Y))
    
    screen.blit(puppy_img, (puppy_x, puppy_y))
    screen.blit(huntress_img, (huntress_x, huntress_y))
    screen.blit(text, (TEXT_X, TEXT_Y))

    # Capture the current frame
    pygame.display.flip()
    frame = pygame.surfarray.array3d(screen)

    # Update the display
    pygame.display.update()

    # Control the frame rate
    pygame.time.delay(1000//CALCULATION_RATE)


# Quit Pygame
pygame.quit()
sys.exit()
