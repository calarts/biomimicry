smoothness = 0.5; #Default 0.5: How smooth the movement is. Larger numbers for more smooth lines and smaller numbers for more wiggly lines.
speed = 3; #Default 3: How fast the line moves.
fade = 0; #Default 0 (Must be 0-1): How quickly the trails fade into the background. 0 for no fade and 1 for no trails.

def setup():
    global distance, xvel, yvel, fade, x,y
    distance = 1
    xacc = 0
    yacc = 0
    xvel = 1
    yvel = 1
    # fullScreen()
    size(400,400)
    background(255)  
    fade *= 255
    fill(255, fade)
    x = width/2
    y = 0
    
def draw():
    global xvel, yvel, x,y
    noStroke()
    rect(0,0,width,height)
    stroke(0)
    xangle = random(360)
    yangle = random(360)
    xacc = distance*cos(xangle)
    yacc = distance*sin(yangle)
    xvel += xacc
    yvel += yacc
    xvel *= speed
    yvel *= speed
    
    line(x,y,x+xvel/smoothness,y+yvel/smoothness)
    
    x += xvel/smoothness
    y += yvel/smoothness
    if(x>width):
        x-=width
        line(x,y,x-xvel/smoothness,y-yvel/smoothness)
    elif (x<0):
        x+=width
        line(x,y,x-xvel/smoothness,y-yvel/smoothness)
    
    if (y>height):
        y-=height
        line(x,y,x-xvel/smoothness,y-yvel/smoothness)
    elif (y<0):
        y+=height
        line(x,y,x-xvel/smoothness,y-yvel/smoothness)
    
    xvel /= speed
    yvel /= speed
    xvel = constrain(xvel,-speed*smoothness,speed*smoothness)
    yvel = constrain(yvel,-speed*smoothness,speed*smoothness)
    if mousePressed:
        background(255)
    