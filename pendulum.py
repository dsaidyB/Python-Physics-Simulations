import pygame
import pygame.gfxdraw
import math

pygame.init()
surface = pygame.display.set_mode((800, 800))

paused = False
game_over = False

m = 6
g = 9.81
gamma = 0.02
theta = math.pi/2
pendulum_length = 400
pendulum_width = 20
t = 0

a = 0
v = 0
v_prev = 0
px = 0
py = 0

limitL = -math.pi/2
limitR = math.pi/2

left = False

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
        pend_px1 = -round(pendulum_width/2*math.cos(theta)) + 400
        pend_py1 = round(pendulum_width/2*math.sin(theta)) + 10

        pend_px2 = round(pendulum_width/2*math.cos(theta)) + 400
        pend_py2 = -round(pendulum_width/2*math.sin(theta)) + 10

        pend_px3 = round(pendulum_length * math.sin(theta)) + 400 + round(pendulum_width/2*math.cos(theta))
        pend_py3 = round(pendulum_length * math.cos(theta)) + 10 - round(pendulum_width/2*math.sin(theta))

        pend_px4 = round(pendulum_length * math.sin(theta)) + 400 - round(pendulum_width/2*math.cos(theta))
        pend_py4 = round(pendulum_length * math.cos(theta)) + 10 + round(pendulum_width/2*math.sin(theta))

        ball_px = round(pendulum_length * math.sin(theta)) + 400
        ball_py = round(pendulum_length * math.cos(theta)) + 10

        a = -m*g*math.sin(theta)
        air = gamma*v
        v += a - air
        vx = v*math.cos(theta)
        vy = v*math.sin(theta)

        # print(pend_px1, pend_py1)
        # print(pend_px2, pend_py2)
        # print(pend_px3, pend_py3)
        # print(pend_px4, pend_py4)
        pygame.draw.circle(surface, (255, 155, 0), (400, 0), 15)
        pygame.gfxdraw.filled_polygon(surface, [(pend_px1, pend_py1), (pend_px2, pend_py2), (pend_px3, pend_py3), (pend_px4, pend_py4)], (255, 80, 0))
        pygame.draw.circle(surface, (255, 155, 155), (ball_px, ball_py), 20)


        pygame.display.update()
        surface.fill((0, 0, 0))

        # if (theta >= limitR): # -0.5 < vx < 0.5
        #     left = True
        #     # limitL += math.pi/32
        #
        # if (theta <= limitL):
        #     left = False
        #     # limitR -= math.pi/32

        if (vx <= 0 and ball_px >= 400 and left == False):
            left = True
            # limitL += math.pi/32

        if (vx >= 0 and ball_px < 400 and left == True):
            left = False
            # limitR -= math.pi/32

        tempx = ball_px
        tempy = ball_py
        px = ball_px - vx
        py = ball_py + vy
        dl = math.sqrt((tempx - px) ** 2 + (tempy - py) ** 2)
        dtheta = math.acos(1 - dl ** 2 / (2 * pendulum_length ** 2))

        if left:
            dtheta = -1*dtheta
        if not left:
            dtheta = abs(dtheta)
        theta += dtheta

        t += 1

        # print("Acceleration:", round(a, 1))
        # print("Air Resistance:", round(air, 1))
        # print("Velocity:", round(v, 1))
        # print("vx:", vx)
        # print("vy:", round(vy, 1))
        # # print("x1:", round(tempx, 1))
        # # print("x2: ", round(px, 1))
        # # print("y1:", round(tempy, 1))
        # # print("y2:", round(py, 1))
        # print("ball x:", round(ball_px, 1))
        # print("ball y:", round(ball_py, 1))
        # print("dl:", round(dl, 1))
        # print("dtheta:", round(dtheta, 1))
        # print("theta:", round(theta, 1))
        # print("Left:", left)
        # print()

        pygame.time.delay(100)

        v_prev = v

        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('Tangential acceleration: ' + str(round(a-air, 1)) + "m/s²", True, (255, 125, 0))
        textRect = text.get_rect()
        textRect.center = (400, 500)
        surface.blit(text, textRect)

        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('Tangential velocity: ' + str(round(v, 1)) + "m/s", True, (255, 125, 0))
        textRect = text.get_rect()
        textRect.center = (400, 540)
        surface.blit(text, textRect)

        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('Ball X: ' + str(round(ball_px, 1)) + "m", True, (255, 125, 0))
        textRect = text.get_rect()
        textRect.center = (400, 580)
        surface.blit(text, textRect)

        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('Ball Y: ' + str(round(800 - ball_py, 1)) + "m", True, (255, 125, 0))
        textRect = text.get_rect()
        textRect.center = (400, 620)
        surface.blit(text, textRect)

        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('Theta (radians): ' + str(round(theta, 4)) + " = " + str(round(theta/math.pi, 2)) + " π", True, (255, 125, 0))
        textRect = text.get_rect()
        textRect.center = (400, 660)
        surface.blit(text, textRect)

        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('Theta (degrees): ' + str(round(theta*180/math.pi, 2)) + "°", True, (255, 125, 0))
        textRect = text.get_rect()
        textRect.center = (400, 700)
        surface.blit(text, textRect)

        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('Time: ' + str(t/10) + " seconds", True, (255, 125, 0))
        textRect = text.get_rect()
        textRect.center = (400, 740)
        surface.blit(text, textRect)



pygame.quit()
