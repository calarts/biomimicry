def gridlines(blocksize=50):    
    for x in range(0,width,blocksize):
        line(x,0,x,height)
        text(x, x, 10)
    
    for y in range(0,height,blocksize):
        line(0,y,width,y)
        text(y, 2, y)