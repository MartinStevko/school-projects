import pyglet
from pyglet.window import key

class Keyboard():

    def __init__(self, window):
        self.keys = key.KeyStateHandler()
        window.push_handlers(self.keys)

    def is_pressed(self, key = key.SPACE):
        return self.keys[key]

    # KEYBOARD MAPPING ONTO GAME ACTIONS
    # Method name == game action

    def left(self):
        return self.is_pressed(key.A) or self.is_pressed(key.LEFT)

    def right(self):
        return self.is_pressed(key.D) or self.is_pressed(key.RIGHT)       

    def exit(self):
        return self.is_pressed(key.ESCAPE)

