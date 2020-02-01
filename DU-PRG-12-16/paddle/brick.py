import random

import pyglet
from quad import Quad

import game
from tweening import TweenFunc

class Brick(Quad):

    def __init__(self, x, y, width = 50, height = 20, color = (1,1,1)):
        super().__init__(x, y, width, height)
        if random.random() > 0.94:
            self.destroyable = False
        else:
            self.destroyable = True

        if self.destroyable:
            self.set_color(color)
        else:
            self.set_color((1,0,0))

        self.alive = True

    def appear(self, time = 1, delay = 0):        
        self._appear_time = time
        self._appear_y = self.y        
        if delay > 0:            
            game.tween.tween(self, game.window.height + self.height * 2, self.y, delay, TweenFunc.ease_in_out_sine, None, self.delay_complete)
        else:            
            self.delay_complete()
        self.y = game.window.height + self.height * 2

    def delay_complete(self, target = None, progress = 0, value = 0):
        game.tween.tween(self, game.window.height + self.height * 2, self._appear_y, self._appear_time, TweenFunc.ease_in_out_sine, self._tween_y)

    def _tween_y(self, target, progress, value):
        self.y = value

    def hit(self):
        if self.destroyable:
            self.alive = False
