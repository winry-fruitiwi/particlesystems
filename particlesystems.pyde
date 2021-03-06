# This is based on Daniel's coding example from The Nature of Code about particle systems.
# These are my versions:
#
# v0.00:   Version comments, code comments, shell
# v0.01:   Particle.py comments and function shells
# v0.02:   Making the particle class actually work
# v0.03:   firebursts of particles!
# v0.04:   Addition. Plan: make the fireburst follow the mouse and disappear in random colors.
# v0.05:   Emitter tab, Emitter class, make class work
# v0.06:   Fireworks: Firestarter and fireburst!

from Particle import *
from Emitter import *
from Firestarter import *
from Fireburst import *
from Trail import *


def setup():
    global firestarters, firebursts, emitters
    #blendMode(ADD)
    
    # We're going to append to particles, but append only works on a list, not a NoneType.
    emitters = []
    firestarters = []
    firebursts = []
    #emitters.append(Emitter(width/2, height/2))
    
    colorMode(HSB, 360, 100, 100, 100)
    
    size(945, 1000) # do not change!
    
    #noCursor() # TODO: add this later for the addition
    # now we need to make the particles.
    strokeWeight(2)
    background(220, 79, 35)


def draw():
    global firestarters, firebursts, emitters
    background(220, 79, 35)
    gravity = PVector(0, 0.1)
    
    noStroke()
    # fill(120, 100, 80, 80)
    # rect(-10, 7*height/8, width+20, height/8)
    # fill(0, 100, 80, 80)
    # rect(width/3, 7 * height/8 - 50, width/25, 50)
    # triangle(width/3 - 8, 7 * height/8 - 50,
    #          width/3 + 18, 7*height/8-80,
    #          width/3 + 44, 7 * height/8 - 50)
    
    # let's operate on all of the particles. I'm preparing to remove particles later.
    # for e in emitters:
    #     e.show()
    #     e.update(gravity)
    #     e.emit() # we will never use emitters.
    
    for i in range(len(firestarters) - 1, -1, -1):
        starter = firestarters[i]
        starter.show()
        starter.update()
        starter.emit()
        if starter.finished():
            # the firestarter is the tiny glob that goes into the sky with a small trail
            # but the burst is what produces the bright flourish. This simulates a firework.
            burst = Fireburst(starter.pos.x,
                              starter.pos.y, 
                              random(360), random(80, 100), 100)
            burst.emit()
            # delay(10)
            burst.emit()
            firebursts.append(burst)
            firestarters.remove(starter)
    
    for i in range(len(firebursts) - 1, -1, -1):
        fireburst = firebursts[i]
        fireburst.show()
        fireburst.emit_update()
        fireburst.pupdate(PVector(0, 0))
        
        burst_pattern = fireburst.ellipse_burst()
        # fireburst has an array of particles, and can have a force applied on them.
        # they also have a seek method that brings them towards their target.
        for i in range(len(fireburst.particles) - 1):
            fireburst.particles[i].apply_force(fireburst.particles[i].seek(burst_pattern[i]))
        
        if fireburst.finished():
            firebursts.remove(fireburst)
        
    
    # fill(100, 100, 100, 100)
    # text(len(emitters), 10, 10)


def mousePressed():
    global emitters, firestarters
    
    for i in range(5):
        firestarters.append(Firestarter(random(100, width - 100), height - 2))
    
