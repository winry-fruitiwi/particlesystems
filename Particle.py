# This creates a single small, white orb that disappears as time goes on.
# My addition will make the particle flourish and make a new color before disappearing.

class Particle(object):
    def __init__(self, x, y, h, s, b):
        # lifetime is the instance field that determines the alpha of the fill in show.
        # Later, when lifetime gets to zero, I will pop it from the list of particles.
        self.lifetime = 100
        # pos is a PVector that determines the starting position. Based on x and y.
        self.pos = PVector(x, y)
        # vel is a PVector that determines how fast the object is.
        self.vel = PVector(0, 0) #PVector.random2D().mult(6)
        
        # acc is a PVector that dictates how the object's velocity is changing.
        self.acc = PVector(0, 0)
        # c is the color I'll use to show these particles.
        self.h = h
        self.s = s
        self.b = b
        self.max_speed = 5
        self.max_force = 0.1
        
        
        self.decrement_rate = 10
    
    
    # shows this particle using its lifetime instance field.
    # note that I learned the term "instance field" from Java and it may not apply here.
    def show(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        
        if self.finished():
            strokeWeight(2)
            stroke(random(360), random(60, 100), 100, 100)
            fill(random(360), random(60, 100), 100, 100)
            line(0, -2, 0, 2)
            line(-2, 0, 2, 0)
            
            # stroke(random(360), random(60, 100), 100, 100)
            # fill(random(360), random(60, 100), 100, 100)
            # line(self.pos.x, self.pos.y - 2, self.pos.x, self.pos.y + 2)
            # line(self.pos.x - 2, self.pos.y, self.pos.x + 2, self.pos.y)
            # strokeWeight(1)
            
        
        else:
            stroke(self.h, self.s, self.b, self.lifetime)
            fill(self.h, self.s, self.b, self.lifetime)
            circle(0, 0, 10)
        
        popMatrix()
        
            
    
    
    # apply a force to the particle. A classic example of Newton's Second Law, F = ma.
    def apply_force(self, force):
        # F = ma, so a = F/m. However, m = 1, so a = F.
        self.acc.add(force)
    
    
    # this updates the particle's position, velocity, and acceleration.
    def update(self):
        self.pos.add(self.vel)
        self.vel.add(self.acc)
        self.acc = PVector(0, 0)
        self.lifetime -= random(self.decrement_rate)
    
    
    # if the particle is dead, return true.
    # In my addition, before departing for the graveyard, my particle will burst in color!
    def finished(self):
        return self.lifetime <= 0
    
    
    # adding seek can make the sprint easier if I can make it work. I just want an ellipse!
    def seek(self, target): # target is a PVector!
        # we need to find the difference between the target's and our positions, which will
        # help us find the desired velocity.
        desired = PVector.sub(target, self.pos) # we don't want to modify target.
        desired.setMag(self.max_speed)
        desired.sub(self.vel)
        desired.limit(self.max_force)
        return desired
