import pygame

pygame.init()
surface = pygame.display.set_mode((800, 600))

paused = False
game_over = False
x, y = 0, 100
v = -12
g = 0.981
t = 0

while not (game_over):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_over = True
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_SPACE):
                if paused == False:
                    paused = True
                elif paused == True:
                    paused = False
    if paused:
        pass
    else:
        pygame.draw.circle(surface, (255, 0, 0), (x, y), 20)

        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('Velocity: ' + str(round(-v)) + "m/s", True, (255, 125, 0))
        textRect = text.get_rect()
        textRect.center = (700, 80)
        surface.blit(text, textRect)

        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('Height: ' + str(round((591-y))) + "m", True, (255, 125, 0))
        textRect = text.get_rect()
        textRect.center = (700, 40)
        surface.blit(text, textRect)

        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('Time: ' + str(round(t/25, 1)) + "s", True, (255, 125, 0))
        textRect = text.get_rect()
        textRect.center = (700, 120)
        surface.blit(text, textRect)

        pygame.display.update()
        surface.fill((0, 0, 0))

        t += 1

        if x < 800 and y + v < 590:
            v += g
            y += v
            x += 2
        else:
            v *= -0.7
        pygame.time.delay(40)

pygame.quit()
