class ball:
    def __init__(self, velo, pos, size, color, timing, dispSize):
        self.velo = velo
        self.grav = 10000.0
        self.pos = pos
        self.size = size
        self.color = color
        self.timing = 1/float(timing)
        self.DISPLAYSIZE = dispSize
    def setPos(self, newX, newY):
        if newX > self.DISPLAYSIZE[0]:
            self.velo = (self.velo[0]*-.99, self.velo[1])
            self.pos = (self.DISPLAYSIZE[0], self.pos[1])
        elif newX < 0:
            self.velo = (self.velo[0]*-.99, self.velo[1])
            self.pos = (0, self.pos[1])
        elif newY >= self.DISPLAYSIZE[1]:
            self.velo = (self.velo[0], -100)
            self.pos = (self.pos[0], self.DISPLAYSIZE[1]-100)
        elif newY < 0:
            self.velo = (self.velo[0], self.velo[1]*-.99)
            self.pos = (self.pos[0], 0)
        else:
            self.pos = (newX, newY)
    def gravityMovement(self):
        self.velo = (self.velo[0], self.grav * self.timing)
        xChange = self.velo[0] * self.timing
        yChange = self.velo[1] * self.timing
        xPos = self.pos[0] + xChange
        yPos = self.pos[1] + yChange
        self.setPos(xPos, yPos)