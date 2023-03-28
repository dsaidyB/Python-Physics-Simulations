import pygame
import pygame.gfxdraw

pygame.init()
surface = pygame.display.set_mode((800, 800))

paused = False
game_over = False

#v_r = (h/2)**2 / (4*mu) * p / L * (1 - r**2/(h/2)**2)

class particle:
    def __init__(self, x_i1, y_i1, x_i2, y_i2, flow_rate):
        self.x1 = x_i1
        self.y1 = y_i1
        self.x2 = x_i2
        self.y2 = y_i2
        self.r = abs(400 - y_i1)
        self.speed = flow_rate
        self.mu = 2
        self.L = 1
        self.p = 1
        self.h = abs(600 - 200) / 2

        pygame.gfxdraw.filled_polygon(surface, [(x_i1, y_i1), (x_i1, y_i2), (x_i2, y_i2), (x_i2, y_i1)], (125, 125, 0))

    def update(self):
        self.speed = abs(self.h**2 / (4*self.mu) * self.p / self.L * (1 - self.r**2 / self.h**2) / 800)
        if (self.x1 > 800):
            self.x2 = self.x2 - self.x1
            self.x1 = 0

        self.x1 += self.speed
        self.x2 += self.speed
        #print(self.speed)
        pygame.gfxdraw.filled_polygon(surface, [(self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1)], (100, round(self.speed*20), round(self.speed*20)))

particle_list = []
for y in range(200, 620, 20):
    for x in range(0, 800, 20):
        particle_list.append(particle(x,y,x+10,y+10,0.5))

print(particle_list)

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
        for i in range(len(particle_list)):
            particle_list[i].update()

    pygame.display.update()
    surface.fill((0, 0, 0))

pygame.quit()
