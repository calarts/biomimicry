from classes import *

# IMPROVEMENTS:
# pick the mother and father from the field

def setup():
    size(800, 800)
    background(0)
    noStroke()
    background(0)
    father = Peaplant(width/3,40)
    mother = Peaplant(2*width/3,40)
    
    father.display()
    mother.display()
    
    fill(255)
    textSize(12)
    textAlign(CENTER)
    text("father", width/3, 90)
    text("mother",  2*width/3, 90)
    text(father.report, width/3, 110)
    text(mother.report, 2*width/3, 110)
    
    for y in range(160,height+1,50):
        for x in range(0,2*width+1,50):
            # Flower(x,y)
            pea = Peaplant(x,y, father,mother)
            pea.display()
