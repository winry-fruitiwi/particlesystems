# This is based on Daniel's coding example from The Nature of Code about particle systems.
# These are my versions:
#
# v0.00:   Version comments, code comments, shell
# v0.01:   Particle.py comments and function shells
# v0.02:   Making the particle class actually work
# v0.03:   Bursts of particles!
# v0.04:   Addition. Plan: make the burst follow the mouse and disappear in random colors.

from Particle import *
from Emitter import *

def setup():
    global emitters
    
    # We're going to append to particles, but append only works on a list, not a NoneType.
    emitters = []
    #emitters.append(Emitter(width/2, height/2))
    
    colorMode(HSB, 360, 100, 100)
    
    size(945, 1000) # do not change!
    
    #noCursor() # TODO: add this later for the addition
    # now we need to make the particles.
    strokeWeight(2)


def draw():
    global emitters
    background(220, 79, 35)
    gravity = PVector(0, 0.1)
    
    noStroke()
    fill(120, 100, 100, 100)
    rect(-10, 7*height/8, width+20, height/8)
    fill(0, 100, 100, 100)
    rect(width/3, 7 * height/8 - 50, width/25, 50)
    triangle(width/3 - 8, 7 * height/8 - 50,
             width/3 + 18, 7*height/8-80,
             width/3 + 44, 7 * height/8 - 50)
    
    # let's operate on all of the particles. I'm preparing to remove particles later.
    for e in emitters:
        e.show()
        e.update(gravity)
        e.emit()
    
    #fill(100, 100, 100, 100)
    text(len(emitters), 10, 10)


def mousePressed():
    global emitters
    emitters.append(Emitter(mouseX, mouseY))
    if len(emitters) > 150:
        noLoop()
