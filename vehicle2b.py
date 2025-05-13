import pygame

clock = pygame.time.Clock()

resolution = (1300, 600)
green = (0, 255, 75)
red = (255, 0, 0)
yellow = (120, 120, 0)
black = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode(resolution)
font = pygame.font.SysFont('Arial', 16)


offset_x = 40
offset_y = 10
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
    def __init__(self, x, y, height, width, color, circle, screen):
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

    def accelerate(self, circle):
   
        dx = self.x - circle.x 
        dy = self.y - circle.y 
        distance = max(0.1, (dx**2 + dy**2)**0.5)  
        

        dir_x = dx / distance
        dir_y = dy / distance
        
        base_speed = 1000
        repulsion_strength = 2
        
        self.speed_x = dir_x * (base_speed / distance) * repulsion_strength
        self.speed_y = dir_y * (base_speed / distance) * repulsion_strength

        
        
        

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.x, self.y = self.rect.center


def speedometer(screen, speed):
    text = f"Speed: {abs(speed): .4f}"
    text_surface = font.render(text, True, (255, 0, 0))
    screen.blit(text_surface, (10, 10))

source  = Circle(x = 600, y = 350, radius=50, color=red, screen=screen)
car = Rectangle(x = 300, y = 300, height= 30, width=50, color = yellow, circle=source, screen=screen)
sensor1 = Rectangle(x = 40, y = 110, height= 10, width=10, color = red, circle=source, screen=screen)
sensor2 = Rectangle(x = 100, y = 110, height= 10, width=10, color = red, circle=source, screen=screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    source.draw()

    car.accelerate(source)
    car.move()

    sensor1.rect.x = car.rect.x + 40   
    sensor1.rect.y = car.rect.y + 20
    sensor2.rect.x = car.rect.x + 40 
    sensor2.rect.y = car.rect.y + 0 

    car.draw()
    sensor1.draw()
    sensor2.draw()
    

    speedometer(screen, car.speed_x)  # Show speed
    pygame.display.flip()
    clock.tick(60)