import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Lab 6 Part 1")

#animal image
animal_image = pygame.image.load('red_panda.png')
sized_animal_img = pygame.transform.scale(animal_image, (100, 100))   
animal_rect = animal_image.get_rect()
x = 0
y = 500
change = .5



# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (RGB)
    screen.fill((0, 0, 0))


    # Draw the animal image
    if x == 700:
        change = -.5
    elif x == 0:
        change = .5
    x += change
    animal_rect.topleft = (x, y)
    screen.blit(sized_animal_img, animal_rect)

    # Update the display
    pygame.display.flip()