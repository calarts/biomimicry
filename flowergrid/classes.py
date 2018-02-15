import random 
    
class Peaplant:
    def __init__(self,x=40,y=40, father=None,mother=None):
        self.genotype = {}
        self.report = ""
        self.x = x
        self.y = y
        # the genotype is a dictionary of alleles
        # what is the minimum list to make a pea? should this be more flexible? 
        # do we want to create alien species?
        if father is not None and mother is not None:
            # father is pollen, mother is pistil
            # we won't need the parents after birth!
            self.genotype = self.selectGenes(father,mother)
        else:
            self.genotype = self.parthenogenesis()
        self.expressGenes()
        
    def selectGenes(self,father,mother):
        # select a random allele from each pair
        # mix 'em up!
        flower = (
            random.choice(father.genotype['flower']), 
            random.choice(mother.genotype['flower'])
        )
        pea = (
            random.choice(father.genotype['pea']), 
            random.choice(mother.genotype['pea'])
        )
        stem = (
            random.choice(father.genotype['stem']), 
            random.choice(mother.genotype['stem'])
        )
        
        genotype = {
            'flower':flower, # red or white flowers? red flowers are dominant
            'pea':pea,    # smooth or wrinkled? smooth skins are dominant
            'stem':stem,   # tall or short stems? long stems are dominant
        }
        return genotype
        
    def parthenogenesis(self):
        print("PARTHENOGENESIS!")
        # reproduction from an ovum without fertilization
        # this is a hack! normally it would come from the parent
        flower = random.choice(['F','f']), random.choice(['f','F'])
        pea = random.choice(['S','s']), random.choice(['s','S'])
        stem = random.choice(['L','l']), random.choice(['l','L'])

        genotype = {
            'flower':flower, # red or white flowers? red flowers are dominant
            'pea':pea,    # smooth or wrinkled? smooth skins are dominant
            'stem':stem,   # tall or short stems? long stems are dominant
        }
        println(genotype)
        return genotype
        
    def contributeGenes(self):
        return self.genotype
    
    def expressGenes(self):
        # generate the phenotypes!
        
        # red flowers are dominant
        if (self.genotype['flower'] == ('f', 'f')):
            self.flowerColor = color(255, 255, 255)
            self.report = "White flower, "
        else:
            self.flowerColor = color(255, 0, 0)
            self.report = "Red flower, "
    
        # smooth skins are dominant
        if (self.genotype['pea'] == ('s', 's')):
            self.skinTexture = 'wrinkled'
            self.report += "wrinkled pea, "
        else:
            self.skinTexture = 'smooth'
            self.report += "smooth pea, "
    
        # long stems are dominant
        if (self.genotype['stem'] == ('l', 'l')):
            self.stemLength = -8
            self.report += "short stem."
        else:
            self.stemLength = 8
            self.report += "long stem."
            
    def display(self):
        fill(self.flowerColor)
        noStroke() # Don't draw a stroke around shapes
        pushMatrix()
        translate(self.x, self.y)
        fill(self.flowerColor)
        for i in range(0,5):
            # sneak in that stemlength here
            ellipse(0, -10, 20+self.stemLength, 20+self.stemLength)
            rotate(radians(72))
        # center circle
        # fill(self.centerColor)
        stroke(150)
        ellipse(0, 0, 20, 20)
        if (self.skinTexture == 'wrinkled'):
            fill(128)
            textSize(12)
            textAlign(CENTER)
            text("W", 0, 5)
        # textAlign(LEFT,BOTTOM)
        # report = "I have %s skin and a %s cm stem" %(self.skinTexture, self.stemLength)
        # textSize(14)
        # text(report, 66,66)
        popMatrix()
        
# class Flower(object):
#     def __init__(self, myx, myy):
#         self.lifespan = 255
#         self.myx = myx
#         self.myy = myy
#         self.petalColor = color(255,200,50)
#         self.centerColor = color(255,100,50)
#         self.drawFlower()
    
#     def drawFlower(self):
#         # read this: https://processing.org/tutorials/transform2d/
#         pushMatrix()
#         translate(self.myx, self.myy)
#         fill(self.petalColor)
#         for i in range(0,5):
#             ellipse(0, -10, 20, 20)
#             rotate(radians(72))
#         # center circle
#         fill(self.centerColor)
#         ellipse(0, 0, 20, 20)
#         popMatrix()

