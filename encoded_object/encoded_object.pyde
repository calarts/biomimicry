# Doug's spontaneous encoded object
from utils import gridlines

size(350,350)
background(255)

# 0. lay down a coarse grid
stroke(160, 220, 280)
fill(120, 200, 240)
gridlines(blocksize=50)

noFill()
stroke(60)
strokeWeight(2)

# 1. draw a square in the center of the window
rect(100,100, 100,100)

# # 2. draw another square of the same size starting in the center of the first rectangle
rect(150,150, 100,100)

# # 3. draw a line from the NW corner of the first square to the NW corner of the second square
line(100,100, 150,150)

# # 4. draw a third line from the NE corner of the first square to the NE corner of the second square
line(200,100, 250,150)

# # 5. draw another line from the SW corner of the first squre to the SW corner of the second square
line(100,200, 150,250)

# # 6. draw a final line from the SE corner of the first square to the SE corner of the second square
line(200,200, 250,250)

# # 7. identify this object
fill(0, 102, 153)
text("Necker Cube", 140, 330)