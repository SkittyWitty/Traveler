import pygame
from pygame.locals import *

class App:
    # common colors
    _white  = (255, 255, 255)
    _grass  = ()
    _ground = ()
    _street = ()
    _water  = ()

    def __init__(self):
        self._running = True
        self._displaySurf = None
        self._screen_display = pygame.display
        self.size = self.width, self.height = 640, 480 # Size is a tuple containing width and height

    def onInit(self):
        pygame.init()
        self._displaySurf = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        self._running = True
        self._imageSurf = pygame.image.load("./resources/characters/traveler.png").convert()

    def onEvent(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def onLoop(self):
        pass
    def onRender(self):
        self._displaySurf.blit(self._imageSurf, (0,0))
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