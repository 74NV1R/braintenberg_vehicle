import pygame

pygame.init()


WIDTH, HEIGHT = 1300, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Braitenberg Vehicle')

clock = pygame.time.Clock

RED  = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)


class Vehicle:
    def __init__(self, position, direction, radius = 50, color = RED):
        self.position = position
        self.direction = direction


        self.radius = radius
        self.color = color 


        #sensor

        self.sensor_radius = 15
        self.sensor_offset = self.radius + self.sensor_radius
        self.sensor_position = self.position - self.sensor_offset
        self.sensor_color = GREEN

        

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius)

        pygame.draw.circle(surface, self.censor_color, self.censor_position, self.censor_radius)

        


    def move(self):
        direction = pygame.math.Vector2(0, -1).rotate(self.direction)
        distance = 1 
        self.position += direction * distance
        self.censor_position = self.position + pygame.math.Vector2(0, -self.censor_offset).rotate(self.direction+1)


class Circle:

    def __init__(self, position, radius = 50, color = RED):
        self.position = pygame.math.Vector2(position)
        self.radius = radius
        self.color = color 


    """ def move(self):
        self.position.y = self.position.y +1
        self.position.x = self.position.x +1 """
        

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius)

sun = Circle((600, 300), radius = 50, color=YELLOW)
running = True

circle = Circle((600, 300))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    #circle.move()
    circle.draw(screen)
    pygame.display.flip()


    clock.tick(60)


pygame.quit()