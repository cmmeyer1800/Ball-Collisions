import math

class ball:
    def __init__(self, surface, color, radius, xVelo): # Init all object variables
        self.radius = radius
        self.surface = surface
        self.color = color
        self.xy = (0.0, 0.0)
        self.yVelo = 0.0
        self.xVelo = xVelo
        self.acceleration = 0.0
        self.gravity = 500.0
    def changePos(self, newX, newY): # Setter method for setting x and y position
        self.xy = (newX, newY)

    def collision(self, otherList): # Function used for detecting collisions between self and all other objects
        for x in range(len(otherList)):
            otherObject = otherList[x]
            if otherObject == self: continue
            distance = math.sqrt(((self.xy[0] - otherObject.xy[0])**2) + ((self.xy[1]-otherObject.xy[1])**2))
            if distance <= self.radius * 2:
                tempX = self.xVelo
                tempY = self.yVelo
                self.xVelo = otherObject.xVelo
                self.yVelo = otherObject.yVelo
                otherObject.xVelo = tempX
                otherObject.yVelo = tempY
        
    def grav(self, frametime, otherList): # Gravity function using the frametiming as a time variable in a physics mechanics formula
        seconds = 1/float(frametime)
        self.collision(otherList)
        if self.xy[1] >= 750.0:
            self.yVelo *= -.94
            self.xVelo *= .94
            self.xy = (self.xy[0], 749.9)
        if self.xy[0] >= 1850.0:
            self.xVelo *= -.94
            self.xy = (1849.9, self.xy[1])
        if self.xy[0] <= 50.0:
            self.xVelo *= -.94
            self.xy = (50.0, self.xy[1])
        self.yVelo += (self.gravity * seconds)
        curY = self.xy[1]
        curY += self.yVelo * seconds
        curX = self.xy[0]
        curX += self.xVelo * seconds
        self.xy = (curX, curY)