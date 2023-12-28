import pygame

pygame.init()

screen = pygame.display.set_mode((768, 512))

pygame.display.set_caption("Mars Rover Game")
icon = pygame.image.load("../assets/mars-rover-logo.jpg")
pygame.display.set_icon(icon)

# Esquina inferior izquierda
rover_x = 0
rover_y = 512 - 64

# Esquina superior izquierda
# rover_x = 0
# rover_y = 0

# Esquina superior derecha
# rover_x = 768 - 64
# rover_y = 0


# Esquina inferior derecha
# rover_x = 768 - 64
# rover_y = 512 - 64


def rover(x, y, rotation=0):
    rover_img = pygame.transform.rotate(pygame.image.load("../assets/mars-rover.png"), rotation)
    screen.blit(rover_img, (x, y))


exec = True
rotation = 0
while exec:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exec = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if rover_x - 64 >= 0:
                    rover_x -= 64
                else:
                    rover_x = 768 - 64
                rotation = 90
            if event.key == pygame.K_RIGHT:
                if rover_x + 64 <= 768 - 64:
                    rover_x += 64
                else:
                    rover_x = 0
                rotation = -90
            if event.key == pygame.K_UP:
                if rover_y - 64 >= 0:
                    rover_y -= 64
                else:
                    rover_y = 512 - 64
                rotation = 0
            if event.key == pygame.K_DOWN:
                if rover_y + 64 <= 512 - 64:
                    rover_y += 64
                else:
                    rover_y = 0
                rotation = 180

    screen.blit(pygame.image.load("../assets/mars-surface.jpg"), (0, 0))
    rover(rover_x, rover_y, rotation)

    pygame.display.update()