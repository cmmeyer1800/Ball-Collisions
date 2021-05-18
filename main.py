import pygame
from object import ball
import random

def main():
    frametiming = 30
    pygame.init()
    back = (192,192,192)
    gameDisplay = pygame.display.set_mode((1900,800))
    pygame.display.set_caption('Physics of collisions')
    gameDisplay.fill(back)
    running = True
    clock = pygame.time.Clock()
    objectList = []
    for x in range(6): # For loop to initialize all ball objects
        randXVelo = random.randint(-200, 200)
        newObject = ball(gameDisplay, (0,0,0), 50, float(randXVelo))
        objectList.append(newObject)
    for x in range(6): # For loop to set random positions of all balls
        objectList[x].changePos(float(random.randint(100, 1800)), float(random.randint(60, 200)))
    while running: # Overall while loop to display and update screen
        for event in pygame.event.get(): # Check for clicking x on window
            if event.type == pygame.QUIT:
                running = False
        gameDisplay.fill(back)
        for x in range(6): # Call drawing circles and update locations according to gravity and collisions
            temp = objectList[x]
            pygame.draw.circle(temp.surface, temp.color , temp.xy, temp.radius)
            temp.grav(frametiming, objectList)
        pygame.display.update()
        clock.tick(frametiming)
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()