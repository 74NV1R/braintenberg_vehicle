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
blue = (0, 0, 255)
purple = (128, 0, 128)
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
        self.optimal_stimulus = 150
        self.threshold = 50

    def update_behavior(self, stimuli):
        if stimuli:
            closest = min(stimuli, key=lambda s: ((s.x-self.x)**2 + (s.y-self.y)**2)**0.5)
            if closest.color == red:
                self.behavior = "repel"
            elif closest.color == green:
                self.behavior = "attract"
            elif closest.color == yellow:
                self.behavior = "orbit"

    def accelerate(self, stimuli):
        total_x, total_y = 0, 0
        for stimulus in stimuli:
            if self.behavior == "orbit":

                dx = stimulus.x - self.x
                dy = stimulus.y - self.y
                distance = max(0.1, (dx**2 + dy**2)**0.5)

                dir_x = -dy / distance
                dir_y = dx / distance
                base_speed = 0.1 
                total_x += dir_x * base_speed * distance
                total_y += dir_y * base_speed * distance
            else:

                dx = stimulus.x - self.x if self.behavior == "attract" else self.x - stimulus.x
                dy = stimulus.y - self.y if self.behavior == "attract" else self.y - stimulus.y
                distance = max(0.1, (dx**2 + dy**2)**0.5)
                
                if distance > self.threshold:
                    response = 1 - abs(distance - self.optimal_stimulus)/self.optimal_stimulus
                    response = max(0, min(1, response))
                else:
                    response = 0

                dir_x = dx / distance
                dir_y = dy / distance
                base_speed = 0.05
                total_x += dir_x * (base_speed * distance * response)
                total_y += dir_y * (base_speed * distance * response)
        
        if len(stimuli) > 0:
            self.speed_x = total_x / len(stimuli)
            self.speed_y = total_y / len(stimuli)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.x = self.rect.x + self.rect.width//2
        self.y = self.rect.y + self.rect.height//2

def speedometer(screen, speed, x, y, label):
    text = f"{label}: {abs(speed):.2f}"
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y))


stimuli = [
    Circle(x=600, y=350, radius=50, color=red, screen=screen),
    Circle(x=200, y=200, radius=30, color=green, screen=screen),
    Circle(x=900, y=400, radius=40, color=yellow, screen=screen)
]


cars = [
    Rectangle(x=600, y=600, height=30, width=50, color=green, screen=screen, behavior="attract"),
    Rectangle(x=200, y=100, height=30, width=50, color=yellow, screen=screen, behavior="repel"),
    Rectangle(x=400, y=300, height=30, width=50, color=blue, screen=screen, behavior="attract"),
    Rectangle(x=800, y=200, height=30, width=50, color=purple, screen=screen, behavior="repel")
]


sensors = [[Rectangle(0, 0, 10, 10, red, screen) for _ in range(2)] for _ in range(4)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    screen.fill(black)
    

    for stimulus in stimuli:
        stimulus.draw()

    for i, car in enumerate(cars):
        car.update_behavior(stimuli)
        car.accelerate(stimuli)
        car.move()
        car.draw()

        for j, sensor in enumerate(sensors[i]):
            sensor.rect.x = car.rect.x + car.rect.width
            sensor.rect.y = car.rect.y + (j * car.rect.height//2)
            sensor.draw()
    
    for i, car in enumerate(cars):
        speedometer(screen, car.speed_x, 10, 10 + i*20, f"Car {i+1} Speed")
    
    pygame.display.flip()
    clock.tick(60)