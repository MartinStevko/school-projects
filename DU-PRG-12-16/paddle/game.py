import pyglet

from keyboard import Keyboard
from physics import Physics
from tweening import Tween

# INITIALIZE THE WINDOW
window = pyglet.window.Window()

# INITIALIZE SUBSYSTEMS
physics = Physics()
keyboard = Keyboard(window)
tween = Tween()