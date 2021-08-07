# This creates a single small, white orb that disappears as time goes on.
# My addition will make the particle flourish and make a new color before disappearing.

class Particle:
    def __init__(self, x, y):
        # lifetime is the instance field that determines the alpha of the fill in show.
        # Later, when lifetime gets to zero, I will pop it from the list of particles.
        self.lifetime = 100
        # pos is a PVector that determines the starting position. Based on x and y.
        self.pos = PVector(x, y)
        # vel is a PVector that determines how fast the object is.
        self.vel = PVector.random2D().mult(random(0.1, 2))
        # acc is a PVector that dictates how the object's velocity is changing.
        self.acc = PVector(0, 0)
    
    
    # shows this particle using its lifetime instance field.
    # note that I learned the term "instance field" from Java and it may not apply here.
    def show(self):
        stroke(0, 0, 100, self.lifetime)
        fill(0, 0, 100, self.lifetime)
        circle(self.pos.x, self.pos.y, 8)
    
    
    # apply a force to the particle. A classic example of Newton's Second Law, F = ma.
    def apply_force(self, force):
        # F = ma, so a = F/m. However, m = 1, so a = F.
        self.acc.add(force)
    
    
    # this updates the particle's position, velocity, and acceleration.
    def update(self):
        self.pos.add(self.vel)
        self.vel.add(self.acc)
        self.acc = PVector(0, 0)
        self.lifetime -= random(6)
    
    
    # if the particle is dead, return true.
    # In my addition, before departing for the graveyard, my particle will burst in color!
    def finished(self):
        return self.lifetime <= 0
