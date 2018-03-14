# simple button: let's change the color of a square 
# when the mouse is pressed within its bounds 

def setup():
    global mystate, mylum
    size(400,400)
    mylum = 200
    fill(mylum)
    textSize(20)
    mystate = "released"
    text(mystate, 12, 45, -30)

def draw():
    global mystate, mylum
    background(100)
    fill(mylum)
    text(mystate, 12, 45, -30)
    rect(150,150,100,100)

def mousePressed(): 
    global mystate, mylum
    mystate = "click on mouseX:%s, mouseY:%s" %(mouseX,mouseY)
    text(mystate, 12, 45, -30)
    if (150 < mouseX < 250) and (150 < mouseY < 250):
        print("woo!")
        mylum = 0
    
def mouseReleased():
    global mystate, mylum
    mystate = "release"
    mylum = 200