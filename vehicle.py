import pygame

clock = pygame.time.Clock()

resolution = (600, 300)
green = (0, 255, 75)
red = (255, 0, 0)
yellow = (120, 120, 0)
black = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode(resolution)

running = True

class Circle:
    def __init__(self, x, y, radius, color, screen):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

class Rectangle:
    def __init__(self, x, y, height, width, color, screen):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

        self.speed_x = 1
        self.speed_y = 0
        
        self.color = color
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


cir1  = Circle(x = 300, y = 150, radius=50, color=red, screen=screen)
rect1 = Rectangle(x = 100, y = 150, height= 30, width=20, color = yellow, screen=screen)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    cir1.draw()
    rect1.move()
    rect1.draw()

    pygame.display.flip()
    clock.tick(60)


pygame.quit()