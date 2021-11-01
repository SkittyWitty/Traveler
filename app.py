import pygame
from pygame.locals import *

class App:
    # common colors
    _white  = (255, 255, 255)
    _grass  = ( 55, 177,  33)
    _ground = (177, 107,  32)
    _street = (120, 120, 120)
    _water  = ( 32,  54, 177)

    def __init__(self):
        self._running = True
        self._displaySurf = None
        self._screenSurf = pygame.display
        self.size = self.width, self.height = 640, 480 # Size is a tuple containing width and height

    def onInit(self):
        pygame.init()
        self._displaySurf = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        self._screenSurf.set_caption("The Traveler")
        self._running = True
        self._imageSurf = pygame.image.load("./resources/characters/traveler.png").convert()

    def onEvent(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def onLoop(self):
        pass
    def onRender(self):
        self._displaySurf.blit(self._imageSurf, (0,0))
        self._screenSurf.update()
        pygame.display.flip()

    def onCleanup(self):
        pygame.quit()

    def onExecute(self):
        if self.onInit() == False:
            self._running = False
        
        while self._running:
            for event in pygame.event.get():
                self.onEvent(event)
                self.onLoop()
                self.onRender()
        self.onCleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.onExecute()