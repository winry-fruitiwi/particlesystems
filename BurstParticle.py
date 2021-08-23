# BParticles are particles used in Fireburst.
from Particle import *


class BurstParticle(Particle):
    def __init__(self, x, y, h, s, b):
        super(BurstParticle, self).__init__(x, y, h, s, b)
        self.decrement_rate = 0.1
