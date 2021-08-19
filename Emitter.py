# this object represents a class that can emit particles from Particle.py
from Particle import *


class Emitter(object):
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.particles = [] # this is a list of all the particles this emitter has.
    
    
    # this shows the emitter, although the only thing it is doing is showing particles!
    def show(self):
        for particle in self.particles:
            particle.show()
            if particle.finished():
                self.particles.remove(particle)
    
    
    # emits a particle
    def emit(self):
        for i in range(int(random(35, 40))):
            self.particles.append(Particle(self.pos.x, self.pos.y))
    
    
    # updates every single particle. Yikes!
    def update(self, force):
        for particle in self.particles:
            particle.update()
            particle.apply_force(force)
