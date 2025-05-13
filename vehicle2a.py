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

    def accelarate(self, circle):
        distance = max(1, ((circle.x - self.x)**2 + (circle.y - self.y)**2)**0.5)

        step = (circle.x - self.x) / distance
            
        if abs(distance) < 5:  
            self.speed_x = 0
            return
        
        self.speed_x += step * (5/distance)
        

    def move(self):
        self.rect.x += self.speed_x
        self.x = abs(self.rect.x)


def speedometer(screen, speed):
    text = f"Speed: {abs(speed): .4f}"
    text_surface = font.render(text, True, (255, 0, 0))
    screen.blit(text_surface, (10, 10))

source  = Circle(x = 600, y = 350, radius=50, color=red, screen=screen)
car = Rectangle(x = 0, y = 100, height= 30, width=50, color = yellow, circle=source, screen=screen)
sensor1 = Rectangle(x = 40, y = 110, height= 10, width=10, color = red, circle=source, screen=screen)
sensor2 = Rectangle(x = 100, y = 110, height= 10, width=10, color = red, circle=source, screen=screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    source.draw()

    car.accelarate(source)
    car.move()


    #sensor.accelarate(source)
    
    #sensor.move()

    sensor1.rect.x = car.rect.x + 40   
    sensor1.rect.y = car.rect.y + 20   
    sensor2.rect.x = car.rect.x + 40  
    sensor2.rect.y = car.rect.y + 0 


    car.draw()
    sensor1.draw()
    sensor2.draw()
    
    speedometer(screen, car.speed_x)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()