# IMPORT PYTHON MODULES
import random

# IMPORT THE FRAMEWORK
import pyglet

# IMPORT GAME CONTEXT
import game

# IMPORT GAME CLASSES
from paddle import Paddle
from brick import Brick
from ball import Ball
from wall import Wall

# DECLARE GAME SCENE

class Scene:

    def __init__(self):
        self.lblScore = pyglet.text.Label('Score: 0',
                          font_name='Arial',
                          font_size=12,
                          x=15, y=5,
                          anchor_x='left', anchor_y='bottom')

        self.lblLevel = pyglet.text.Label('Level: 1',
                          font_name='Arial',
                          font_size=12,
                          x=game.window.width-15, y=5,
                          anchor_x='right', anchor_y='bottom')

        self.setup()

    def setup(self, score = 0, level = 1):
        # SETUP GAME OBEJCTS
        self.paddle = Paddle(game.keyboard, game.window.width / 2 - 50, 40, width = 100, height = 20, speed = 400)

        self.ball = Ball(game.window.width / 2 - 8, 200, width = 16, height = 16, speed = 200, direction = (0, -1) )

        self.wall_w = Wall(0, 0, width = 10, height = game.window.height)
        self.wall_e = Wall(game.window.width-10, 0, width = 10, height = game.window.height)
        self.wall_n = Wall(0, game.window.height-10, width = game.window.width, height = 10)
        self.wall_s = Wall(0, 0, width = game.window.width, height = 10)

        self.walls = [self.wall_w, self.wall_n, self.wall_e, self.wall_s]

        self.score = score
        self.lblScore.text = "Score: " + str(self.score)

        self.level = level
        self.lblLevel.text = "Level: " + str(self.level)

        # bricks setup

        BRICK_WIDTH = 60
        BRICK_HEIGHT = 40
        MARGIN = 10

        self.bricks = []

        brickX = MARGIN
        brickY = game.window.height - MARGIN - BRICK_HEIGHT
        while brickY > game.window.height / 2:
            while brickX + BRICK_WIDTH < game.window.width - MARGIN:
                self.bricks.append(Brick(brickX, brickY, BRICK_WIDTH, BRICK_HEIGHT))
                brickX += BRICK_WIDTH + MARGIN
            brickX = MARGIN
            brickY -= MARGIN + BRICK_HEIGHT            

        # appear
        #for brick in self.bricks:
        #    brick.appear(0.25 + random.random() * 0.5)

    def draw(self):
        for brick in self.bricks:
            brick.draw()

        self.paddle.draw()
        self.ball.draw()

        self.wall_w.draw()
        self.wall_e.draw()
        self.wall_n.draw()

        self.lblScore.draw()
        self.lblLevel.draw()

    def tick(self, dt):
        # update tweens
        game.tween.tick(dt)

        # update game objects
        self.paddle.tick(dt)
        self.ball.tick(dt)

        # compute collisions and raise collision events
        game.physics.collide_prepare()

        game.physics.collide( [self.ball], [self.paddle] )  # collides ball against the paddle
        game.physics.collide( [self.ball], self.walls )     # collides ball against walls
        game.physics.collide( [self.ball], self.bricks)     # collides ball against bricks

        game.physics.collide_finish() # this raises collision events gathered during "physics.collide(...)"

        # remove dead bricks
        i = 0
        while i < len(self.bricks):
            if not self.bricks[i].alive:
                self.bricks.pop(i)
                self.score += 1
                self.lblScore.text = "Score: " + str(self.score)
            else:
                i += 1

        # check ball off-screen
        if self.ball.x < -self.ball.width or self.ball.x > game.window.width + self.ball.width or self.ball.y > game.window.height + self.ball.height or self.ball.y < -self.ball.height:
            self.restart()

        # check all bricks down
        new_level = True
        for brick in self.bricks:
            if brick.destroyable and brick.alive:
                new_level = False
                break
        if new_level:
            self.next_level()

    def restart(self):
        self.setup()

    def next_level(self):
        self.setup(score = self.score, level = self.level + 1)

scene = Scene()

@game.window.event
def on_draw():
    game.window.clear()
    
    # THIS IS A WAY HOW TO DRAW A QUAD OUT OF TWO TRIANGLES
    # pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
    #     [0, 1, 2, 0, 2, 3],
    #     ('v2i', (0, 0,
    #              50, 0,
    #              50, 50,
    #              0, 50)),
    #     ('c3f', (1,0,0,
    #              0,1,0,
    #              0,0,1,
    #              1,1,0))
    # )

    scene.draw()

frame = 0
def tick(dt):
    global frame
    frame += 1
    #print(f"[F{frame}] dt = {dt}\n") # this prints current frame number and the "delta time" == elapsed seconds since the last frame

    scene.tick(dt)

# SCHEDULE PERIODICK TICK EXECUTION ~ 100 FPS    
pyglet.clock.schedule_interval(tick, 1 / 100)

# RUN THE GAME!
pyglet.app.run()
