import pygame
import sys


pygame.init()
clock = pygame.time.Clock()
resolution = (1300, 600)
screen = pygame.display.set_mode(resolution)
font = pygame.font.SysFont('Arial', 16)


red = (255, 0, 0)
yellow = (128, 128, 0)
green = (0, 255, 0)
black = (0, 0, 0)

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
    def __init__(self, x, y, height, width, color, screen, behavior="repel"):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x + width//2 
        self.y = y + height//2 
        self.speed_x = 0
        self.speed_y = 0
        self.color = color
        self.screen = screen
        self.behavior = behavior

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def accelerate(self, circle):
        dx = circle.x - self.x if self.behavior == "attract" else self.x - circle.x
        dy = circle.y - self.y if self.behavior == "attract" else self.y - circle.y
        
        distance = max(0.1, (dx**2 + dy**2)**0.5)
        dir_x = dx / distance
        dir_y = dy / distance
        
        base_speed = 500
        self.speed_x = dir_x * (base_speed / distance)
        self.speed_y = dir_y * (base_speed / distance)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.x = self.rect.x + self.rect.width//2
        self.y = self.rect.y + self.rect.height//2

def speedometer(screen, speed, x=10, y=10, label="Speed"):
    text = f"{label}: {abs(speed):.2f}"
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y))


source = Circle(x=600, y=350, radius=50, color=red, screen=screen)
car_repel = Rectangle(x=300, y=300, height=30, width=50, color=green, 
                       screen=screen, behavior="attract")
car_attract = Rectangle(x=200, y=100, height=30, width=50, color=yellow, 
                     screen=screen, behavior="repel")

sensors_attract = [
    Rectangle(0, 0, 10, 10, red, screen) for _ in range(2)
]
sensors_repel = [
    Rectangle(0, 0, 10, 10, red, screen) for _ in range(2)
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    screen.fill(black)
    source.draw()


    car_attract.accelerate(source)
    car_attract.move()
    car_repel.accelerate(source)
    car_repel.move()

    sensors_attract[0].rect.x = car_attract.rect.x + 40
    sensors_attract[0].rect.y = car_attract.rect.y + 20
    sensors_attract[1].rect.x = car_attract.rect.x + 40
    sensors_attract[1].rect.y = car_attract.rect.y + 0

    sensors_repel[0].rect.x = car_repel.rect.x + 40
    sensors_repel[0].rect.y = car_repel.rect.y + 20
    sensors_repel[1].rect.x = car_repel.rect.x + 40
    sensors_repel[1].rect.y = car_repel.rect.y + 0


    car_attract.draw()
    car_repel.draw()
    for sensor in sensors_attract + sensors_repel:
        sensor.draw()

    speedometer(screen, car_attract.speed_x, 10, 10, "Attract Speed")
    speedometer(screen, car_repel.speed_x, 10, 30, "Repel Speed")

    pygame.display.flip()
    clock.tick(60)