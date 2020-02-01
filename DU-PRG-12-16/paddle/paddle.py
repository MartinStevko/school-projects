import pyglet
from quad import Quad

class Paddle(Quad):

    def __init__(self, keyboard, x, y, width = 100, height = 20, colors = (1,0,0, 0,1,0, 0,0,1, 1,1,0), speed = 100):
        super().__init__(x, y, width, height, colors)
        self.keyboard = keyboard
        self.speed = speed

    def tick(self, dt):
        if self.keyboard.left():
            self.x -= self.speed * dt
        if self.keyboard.right():
            self.x += self.speed * dt

    
            
    