# after a firestarter dies, we turn it into a flash of particles in a pattern!
from Emitter import *


class Fireburst(Emitter):
    def __init__(self, x, y):
        super(Fireburst, self).__init__(x, y)
        self.vel = PVector.random2D()
        self.lifetime = 100
    
    
    def emit_update(self):
        self.lifetime -= 2
    
    
    def finished(self):
        return self.lifetime <= 0
