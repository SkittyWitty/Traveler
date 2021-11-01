import pygame
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._displaySurf = None
        self.size = self.width, self.height = 640, 480 # Size is a tuple containing width and height

    def onInit(self):
        pygame.init()
        self._displaySurf = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        self._running = True

    def onEvent(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def onLoop(self):
        pass
    def onRender(self):
        pass

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