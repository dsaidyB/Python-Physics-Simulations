import matplotlib.pyplot as plt
import math
import pygame


def equation(spot, time):
    return math.cos(spot) * math.e ** (-time)


x_g = 0
t = 0

x_values = [0]
y_values = []

while x_g <= 2 * math.pi:
    x_g += math.pi / 16
    x_values.append(x_g)

for xn in x_values:
    y_values.append(equation(xn, t))

pygame.init()
surface = pygame.display.set_mode((800, 800))
x, y = 10, 10
intensity = 0
game_over = False

while not (game_over):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_over = True

    if t < 40:
        # pygame.time.delay(100)
        # surface.fill((0, 0, 0))
        # pygame.display.update()

        y_values.clear()
        for xn in x_values:
            y_values.append(equation(xn, t/10))

        for y_g in y_values:

            intensity = (y_g + 1) / 2
            r = round(intensity * 255)
            g = 0
            b = round((1 - intensity) * 255)
            color = (r, g, b)

            pygame.draw.rect(surface, color, pygame.Rect(x, y, 40, 40))
            pygame.display.update()

            if x < 640:
                x += 20

        x = 10
        # y += 25
        t += 0.25

pygame.quit()
