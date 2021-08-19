# this is the particle that's much smaller and actually has a radius, but no death sparkle
from Particle import *


class Trail(Particle):
    def __init__(self, x, y, r):
        super(Trail, self).__init__(self, x, y)
        self.r = r
    
    
    def show(self):
        stroke(0, 00, 100, self.lifetime)
        fill(0, 0, 100, self.lifetime)
        circle(self.pos.x, self.pos.y, self.r)
