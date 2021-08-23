# this is the particle that's much smaller and actually has a radius, but no death sparkle
from Particle import *


class TrailParticle(Particle):
    def __init__(self, x, y, r):
        super(TrailParticle, self).__init__(x, y, 0, 0, 100)
        self.vel = PVector(random(-0.8, 0.8), 1)
        self.r = r
        self.decrement_rate = 10
    
    
    def show(self):
        stroke(0, 00, 100, self.lifetime)
        fill(0, 0, 100, self.lifetime)
        circle(self.pos.x, self.pos.y, self.r)
