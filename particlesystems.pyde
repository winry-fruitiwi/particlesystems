# This is based on Daniel's coding example from The Nature of Code about particle systems.
# These are my versions:
#
# v0.00: Version comments, code comments, shell
# v0.01: Particle.py comments
# v0.02: Making the particle class actually work
# v0.03: Bursts of particles!
# v0.04: Addition. Plan: make the burst follow the mouse and disappear in random colors.


def setup():
    global particles
    
    # We're going to append to particles, but append only works on a list, not a NoneType.
    particles = []
    
    colorMode(HSB, 360, 100, 100)
    size(800, 800)
    # noCursor() # TODO: add this later for the addition
    # now we need to make the particles.


def draw():
    global particles
    background(220, 79, 35)
    
    # let's operate on all of the particles. I'm preparing to remove particles later.
    # for i in range(len(particles), 0, -1):
