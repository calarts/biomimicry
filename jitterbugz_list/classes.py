class JitterBug(object):

    def __init__(self, name="b",x=100, y=100, diameter=5, clr=color(100, 0, 0)):
        self.name = name
        self.x = x
        self.y = y
        self.diameter = diameter
        self.speed = 3.0
        self.clr = clr

    def move(self):
        self.x = self.x + random(-self.speed, self.speed)
        self.y = self.y + random(-self.speed, self.speed)

    def display(self):
        fill(self.clr)
        ellipse(self.x, self.y, self.diameter, self.diameter)

    def rollover(self, px, py):
        d = dist(px,py,self.x,self.y)
        if (d < self.diameter/2):
            self.over = True
            print(self.name)
            # textSize(14)
            # text(self.name, 100,100)
        else:
            self.over = False

    