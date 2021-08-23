# this is the bright thing that goes up in the sky
from Emitter import *
from TrailParticle import *


class Firestarter(Emitter):
    def __init__(self, x, y):
        super(Firestarter, self).__init__(x, y)
        self.vel = PVector(0, -2)
        self.acc = PVector(0, 0)
        self.lifetime = 100
    
    
    def update(self):
        self.pos.add(self.vel)
        self.vel.add(self.acc)
        self.acc = PVector(0, 0)
        self.lifetime -= random(0.5)
        for particle in self.particles:
            particle.update()
            
    
    
    def emit(self):
        for i in range(int(random(1, 2))):
            self.particles.append(TrailParticle(self.pos.x, self.pos.y, 1))
    
    
    def show(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        fill(0, 0, 100, 100)
        ellipse(0, 0, 4, 8)
        popMatrix()
        for particle in self.particles:
            particle.show()
            if particle.finished():
                self.particles.remove(particle)
    
    
    def finished(self):
        return self.lifetime <= 0
