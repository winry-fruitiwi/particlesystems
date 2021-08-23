# after a firestarter dies, we turn it into a flash of particles in a pattern!
from Emitter import *
from BurstParticle import *


class Fireburst(Emitter):
    def __init__(self, x, y, h, s, b):
        super(Fireburst, self).__init__(x, y)
        self.vel = PVector.random2D()
        self.lifetime = 100
        self.h = h
        self.s = s
        self.b = b
    
    
    def emit_update(self):
        self.lifetime -= .2
    
    
    def emit(self):
        for i in range(int(random(35, 40))):
            self.particles.append(BurstParticle(self.pos.x, self.pos.y, self.h, self.s, self.b))
    
    
    def finished(self):
        return self.lifetime <= 0
    
    
    def ellipse_burst(self):
        angle = 0
        bursts = []
        for i in range(len(self.particles) - 1):
            bursts.append(PVector(100*cos(angle) + self.pos.x, 200*sin(angle) + self.pos.y))
            angle += TAU/len(self.particles)
        
        return bursts
    
    
