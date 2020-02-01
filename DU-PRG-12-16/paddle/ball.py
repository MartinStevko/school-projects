import math

import pyglet
from quad import Quad

class Ball(Quad):

    def __init__(self, x, y, width = 15, height = 15, colors = (1,1,1, 1,1,1, 1,1,1, 1,1,1), speed = 200, direction = (0, -1)):
        super().__init__(x, y, width, height, colors)
        self.speed = speed
        self.direction = direction

        self.collided = False

    def tick(self, dt):        
        self.x += self.direction[0] * self.speed * dt
        self.y += self.direction[1] * self.speed * dt

        self.collided = False
            
    # COLLISION HANDLERS

    def on_collision_enter_Paddle(self, paddle, coll):
        if self.collided:
            return
        self.collided = True

        (_, north, _, _, _) = coll
        if north > 0: # collided on the north-side of the paddle
            # range: -0.5;0.5
            pos = ((self.x + self.width / 2) - (paddle.x + paddle.width / 2)) / paddle.width
            angleDeg = 90 + 80 + 80 * pos
            angleRad = angleDeg / 180 * math.pi
            self.direction = (-math.sin(angleRad), -math.cos(angleRad))

    def on_collision_enter_Wall(self, wall, coll):
        self._resolve_wall_collision(wall, coll)

    def _resolve_wall_collision(self, wall, coll):
        (_, north, east, south, west) = coll
        if north > 0 or south > 0: # collided on the north/south-side of the wall
            self.direction = ( self.direction[0], -self.direction[1])
        elif east > 0 or west > 0: # collided on the east/west-side of the wall
            self.direction = (-self.direction[0],  self.direction[1])

    def on_collision_enter_Brick(self, brick, coll):
        # handle the ball bounce the same as with a wall
        if not self.collided:
            self.collided = True
            self._resolve_wall_collision(brick, coll)
        # hit the brick!
        brick.hit()
    