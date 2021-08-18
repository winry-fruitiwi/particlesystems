# this is the bright thing that goes up in the sky
from Particle import *


class Firestarter(Particle):
    def __init__(self, x, y):
        super(Firestarter, self).__init__(x, y)
        self.vel = PVector(0, -2)
    
    
    def update(self):
        self.pos.add(self.vel)
        self.vel.add(self.acc)
        self.acc = PVector(0, 0)
        self.lifetime -= random(2)
    
    
    def show(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        fill(0, 0, 100, 100)
        ellipse(0, 0, 8, 16)
        
        popMatrix()
