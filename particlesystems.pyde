# This is based on Daniel's coding example from The Nature of Code about particle systems.
# These are my versions:
#
# v0.00: Version comments, code comments, shell
# v0.01: Particle.py comments and function shells
# v0.02: Making the particle class actually work
# v0.03: Bursts of particles!
# v0.04: Addition. Plan: make the burst follow the mouse and disappear in random colors.

from Particle import *

def setup():
    global particles
    
    # We're going to append to particles, but append only works on a list, not a NoneType.
    particles = []
    
    colorMode(HSB, 360, 100, 100)
    size(800, 800)
    # noCursor() # TODO: add this later for the addition
    # now we need to make the particles.
    for i in range(100):
        particles.append(Particle(width/2, height/2))


def draw():
    global particles
    background(220, 79, 35)
    gravity = PVector(0, 0.2)
    
    # let's operate on all of the particles. I'm preparing to remove particles later.
    for i in range(len(particles)-1, 0, -1):
        p = particles[i]
        p.show()
        p.update()
        p.apply_force(gravity)
