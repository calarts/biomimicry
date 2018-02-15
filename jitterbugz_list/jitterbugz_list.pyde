
from classes import JitterBug

def setup():
    global buglist
    size(1000,1000)
    buglist = [
        JitterBug(
            name='bug', x=width / 2, y=height / 2, diameter=20, clr=color(222, 0, 0)),
        JitterBug(
            name='bop', x=width / 2, y=height / 2, diameter=10, clr=color(111)),
        JitterBug(
            name='jitterz', x=width / 2, y=height / 2, diameter=30, clr=color(255)),
        JitterBug(
            name='butter', x=width / 2, y=height / 2, diameter=5, clr=color(155)),
        JitterBug(
            name='tickles', x=width / 2, y=height / 2, diameter=2, clr=color(0)),
        JitterBug(
            name='crashy', x=width / 2, y=height / 2, diameter=1, clr=color(100)),
        JitterBug(
            name='pancake', x=width / 2, y=height / 2, diameter=38, clr=color(44)),
        JitterBug(
            name='hot', x=width / 2, y=height / 2, diameter=17, clr=color(90)),
        JitterBug(
            name='cold', x=width / 2, y=height / 2, diameter=17, clr=color(90)),
        JitterBug(
            name='cheese', x=width / 2, y=height / 2, diameter=3, clr=color(253)),
        JitterBug(
            name='bouncy', x=width / 2, y=height / 2, diameter=9, clr=color(254)),
        JitterBug(
            name='noodles', x=width / 2, y=height / 2, diameter=14, clr=color(1)),
        JitterBug(
            name='daddy', x=width / 2, y=height / 2, diameter=45, clr=color(50)),
        JitterBug(
            name='mommy', x=width / 2, y=height / 2, diameter=43, clr=color(124)),
        JitterBug(
            name='fatty', x=width / 2, y=height / 2, diameter=52, clr=color(206)),
        JitterBug(
            name='digs', x=width / 2, y=height / 2, diameter=32, clr=color(241)),
        JitterBug(
            name='kiddie', x=width / 2, y=height / 2, diameter=2, clr=color(2)),
        JitterBug(
            name='blue', x=width / 2, y=height / 2, diameter=10, clr=color(0,0,255)),
    ]

def draw():
    for b in buglist:
        b.move()
        b.rollover(mouseX, mouseY)
        b.display()