# This creates a single small, white orb that disappears as time goes on.
# My addition will make the particle flourish and make a new color before disappearing.

class Particle:
    def __init__(self, x, y):
        # lifetime is the instance field that determines the alpha of the fill in show.
        # Later, when lifetime gets to zero, I will pop it from the list of particles.
        self.lifetime = 100
        # pos is a PVector that determines the starting position. Based on x and y.
        self.pos = PVector(x, y)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
    
    
    # shows this particle using its lifetime instance field.
    # note that I learned the term "instance field" from Java and it may not apply here.
    def show(self):
        pass
    
    
    # apply a force to the particle. A classic example of Newton's Second Law, F = ma.
    def apply_force(self, force):
        pass
    
    
    # this updates the particle's position, velocity, and acceleration.
    def update(self):
        pass
    
    
    # if the particle is dead, return true.
    # In my addition, before departing for the graveyard, my particle will burst in color!
    def finished(self):
        return self.lifetime <= 0
