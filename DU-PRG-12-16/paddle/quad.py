import pyglet

class Quad():

    # (x,y) == (0,0) -> left-down corner!
    def __init__(self, x, y, width = 50, height = 20, colors = (1,1,1, 1,1,1, 1,1,1, 1,1,1)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colors = colors

    def draw(self):
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
            [0, 1, 2, 1, 2, 3],
            # beware, we're using v2i here => 'i' stands for integers and it is in pixels; for 2D game we usually want "pixel-perfect", hence the rounding
            ('v2i', (int(self.x),            int(self.y),
                     int(self.x+self.width), int(self.y),
                     int(self.x),            int(self.y+self.height),
                     int(self.x+self.width), int(self.y+self.height)
                    )
            ),
            ('c3f', self.colors)
        )

    def set_colors(self, colors = (1,1,1, 1,1,1, 1,1,1, 1,1,1)):
        self.colors = colors

    def set_color(self, color = (1,1,1)):
        self.set_colors( ( color[0], color[1], color[2], 
                           color[0], color[1], color[2],
                           color[0], color[1], color[2],
                           color[0], color[1], color[2] ) )

    