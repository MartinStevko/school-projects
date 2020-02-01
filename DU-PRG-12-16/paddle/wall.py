import pyglet
from quad import Quad

class Wall(Quad):

    def __init__(self, x, y, width = 50, height = 20, color = (0.5,0,0)):
        super().__init__(x, y, width, height)
        self.set_color(color)

    