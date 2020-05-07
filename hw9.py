
#################################################
# hw9.py
#
# Your name: Yo-Lei Chen
# Your andrew id: yoleic
#################################################

from cmu_112_graphics import *
from tkinter import *
from PIL import Image 
import random


def getLocalMethods(clss):
    import types
    # This is a helper function for the test function below.
    # It returns a sorted list of the names of the methods
    # defined in a class. It's okay if you don't fully understand it!
    result = [ ]
    for var in clss.__dict__:
        val = clss.__dict__[var]
        if (isinstance(val, types.FunctionType)):
            result.append(var)
    return sorted(result)

#copied from http://www.cs.cmu.edu/~112/notes/notes-oop-part3.html
def gcd(x, y):
    if (y == 0): return x
    else: return gcd(y, x%y)

class Bird(object):

    def __init__(self, bird):

        self.bird = bird
        self.eggs = 0
        g = gcd(self.bird, self.eggs)
        Bird.isMigrating = False
    
    # set all birds to be migrating
    @staticmethod
    def startMigrating():
        Bird.isMigrating = True

    #set all birds  tobe not migrating
    @staticmethod
    def stopMigrating():
        Bird.isMigrating = False 
    
    def fly(self):
        return "I can fly!"

    #count the amount of eggs a bird instance has
    def countEggs(self):
        return self.eggs

    #add one more egg
    def layEgg(self):
        self.eggs += 1
    
    #copied from http://www.cs.cmu.edu/~112/notes/notes-oop-part3.html
    #evaluate the equality of two bird objects
    def __eq__(self, other):
        return isinstance(other, Bird) and (self.bird == other.bird)
    
    #copied from http://www.cs.cmu.edu/~112/notes/notes-oop-part3.html
    #convert the object to a string, used inside lists
    def __repr__(self):
        if self.eggs == 0 or self.eggs>1:
            return '%s has %d eggs' % (self.bird, self.eggs)
        else:
            return '%s has %d egg' % (self.bird, self.eggs)

    #copied from http://www.cs.cmu.edu/~112/notes/notes-oop-part3.html
    #hash the bird object
    def __hash__(self):
        return hash((self.bird, self.eggs))
    

class Penguin(Bird):

    def fly(self):
        return "No flying for me."
  
    def swim(self): 
        return "I can swim!"


class MessengerBird(Bird):
    #add additional attribute message
    def __init__(self, mesBird, message):
        super().__init__(mesBird)
        self.message = message

    #return the message the bird is delivering
    def deliverMessage(self):
        return self.message

    
#################################################
# test Bird Class and Subclasses
#################################################

def getLocalMethods(clss):
    import types
    # This is a helper function for the test function below.
    # It returns a sorted list of the names of the methods
    # defined in a class. It's okay if you don't fully understand it!
    result = [ ]
    for var in clss.__dict__:
        val = clss.__dict__[var]
        if (isinstance(val, types.FunctionType)):
            result.append(var)
    return sorted(result)

def testBirdClasses():
    print("Testing Bird classes...", end="")
    # A basic Bird has a species name, can fly, and can lay eggs
    bird1 = Bird("Parrot")
    assert(type(bird1) == Bird)
    assert(isinstance(bird1, Bird))
    assert(bird1.fly() == "I can fly!")
    assert(bird1.countEggs() == 0)
    assert(str(bird1) == "Parrot has 0 eggs")
    bird1.layEgg()
    assert(bird1.countEggs() == 1)
    assert(str(bird1) == "Parrot has 1 egg")
    bird1.layEgg()
    assert(bird1.countEggs() == 2)
    assert(str(bird1) == "Parrot has 2 eggs")
    tempBird = Bird("Parrot")
    assert(bird1 == tempBird)
    tempBird = Bird("Wren")
    assert(bird1 != tempBird)
    nest = set()
    assert(bird1 not in nest)
    assert(tempBird not in nest)
    nest.add(bird1)
    assert(bird1 in nest)
    assert(tempBird not in nest)
    nest.remove(bird1)
    assert(bird1 not in nest)
    assert(getLocalMethods(Bird) == ['__eq__','__hash__','__init__', 
                                     '__repr__', 'countEggs', 
                                     'fly', 'layEgg'])
    
    # A Penguin is a Bird that cannot fly, but can swim
    bird2 = Penguin("Emperor Penguin")
    assert(type(bird2) == Penguin)
    assert(isinstance(bird2, Penguin))
    assert(isinstance(bird2, Bird))
    assert(not isinstance(bird1, Penguin))
    assert(bird2.fly() == "No flying for me.")
    assert(bird2.swim() == "I can swim!")
    bird2.layEgg()
    assert(bird2.countEggs() == 1)
    assert(str(bird2) == "Emperor Penguin has 1 egg")
    assert(getLocalMethods(Penguin) == ['fly', 'swim'])
    
    # A MessengerBird is a Bird that carries a message
    bird3 = MessengerBird("War Pigeon", "Top-Secret Message!")
    assert(type(bird3) == MessengerBird)
    assert(isinstance(bird3, MessengerBird))
    assert(isinstance(bird3, Bird))
    assert(not isinstance(bird3, Penguin))
    assert(not isinstance(bird2, MessengerBird))
    assert(not isinstance(bird1, MessengerBird))
    assert(bird3.deliverMessage() == "Top-Secret Message!")
    assert(str(bird3) == "War Pigeon has 0 eggs")
    assert(bird3.fly() == "I can fly!")

    bird4 = MessengerBird("Homing Pigeon", "")
    assert(bird4.deliverMessage() == "")
    bird4.layEgg()
    assert(bird4.countEggs() == 1)
    assert(getLocalMethods(MessengerBird) == ['__init__', 'deliverMessage'])

    # Note: all birds are migrating or not (together, as one)
    assert(bird1.isMigrating == bird2.isMigrating == bird3.isMigrating == False)
    assert(Bird.isMigrating == False)

    bird1.startMigrating()
    assert(bird1.isMigrating == bird2.isMigrating == bird3.isMigrating == True)
    assert(Bird.isMigrating == True)

    Bird.stopMigrating()
    assert(bird1.isMigrating == bird2.isMigrating == bird3.isMigrating == False)
    assert(Bird.isMigrating == False)
    print("Done!")

testBirdClasses()


# ignore_rest (The autograder ignores all code below here)

class SplashScreenMode(Mode):

    def drawBackground(mode, canvas):
    
        canvas.create_text(mode.width/2, mode.height/2, text= 
        '''


            You must score to 100 to win
            Hit red dots =  +5
            Put brown bricks into your backpack = +10
            Hit yellow dot = GAME OVER!!!

            Press up arrow to Jump. 
            Press L/R arrow to move L/R
        ''',font = f'Arial {mode.height//30} bold',fill = "dark blue",
        anchor = 'center') # 30 = adjusted font size according to screen size
    
    def redrawAll(mode, canvas):
        canvas.create_rectangle(0,0,mode.width, mode.height, fill = 
        "lightpink")
        canvas.create_text(mode.width/2, mode.height/4, text= "WELCOME!", font = 
        f'Arial {mode.height//10} bold')
        SplashScreenMode.drawBackground(mode, canvas)
        canvas.create_text(mode.width/2, mode.height-mode.height/6, text = 
        ' Press any key to start', font = f'Arial {mode.height//20} bold')
         # 8 and 20 = adjusted font size according to screen size

    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.gameMode)


class Player(object):

    def __init__(self, mode):
        self.mode = mode
        self.spriteCounter = 0
        self.imageRowNum = 12 # num of stripped images in each row
        self.sprites = []


class Dots(object): 

    def __init__(self, mode, cx):
        self.mode = mode
        self.cx = cx
        self.cy = mode.height/2 - 130
        """
        height that player can reach only if player jumped
        """
        self.r = 20 #radius
    
    def __hash__(self):
        return hash((self.cx))
    
    def __eq__(self, other):
        return (isinstance(other, Dots) and (self.cx == other.cx))
    
    
    def draw(self, canvas):

        cx = self.cx - self.mode.scrollX  
        canvas.create_oval(cx-self.r, self.cy - self.r, cx+self.r, 
        self.cy + self.r, fill= self.color) 
        
class yellowDots(Dots): 

    def __init__(self, mode, cx):
        super().__init__(mode, cx)
        self.color = 'yellow'
        self.score = 0

class redDots(Dots): 

    def __init__(self, mode, cx):
        super().__init__(mode, cx)
        self.color = 'red'
        self.score = 5

class Walls(object): 

    def __init__(self, mode, cx):
        self.mode = mode
        self.cx = cx
        self.cy = mode.height/2 #self-set position y to be placed on grass
        self.color = 'brown'
        self.score = 10
        self.recWidth = 100 #self-set rectangle Width
        self.recHeight = 30 #self-set rectangle Height
    
    def draw(self, canvas):
        cx = self.cx - self.mode.scrollX
        
        canvas.create_rectangle(cx-self.recWidth/2,self.cy-self.recHeight/2,
        cx+self.recHeight/2,self.cy+self.recHeight/2, fill = 'brown', width = 5)
    
    #check if cursor position is within the rectangle
    def containPoints(self, x, y):
        return (self.cx-self.recWidth/2 <= x <= self.cx+self.recWidth 
        and self.cy - self.recHeight/2 <= y <= self.cy + self.recHeight/2)
    
    #check if cursor position is within the backpack
    def containBackPack(self, x, y):

        bpDisX = 50
        bpDisY = 50
        #backapck is set to be 50 away from mode.width and mode.height

        x0 = (self.mode.width - bpDisX - self.recWidth/2 + 
        self.mode.scrollX) 
        x1 = self.mode.width + self.mode.scrollX
        return (self.mode.height - bpDisY - self.recWidth/2 <= y <= 
        self.mode.height and x0  <= x <= x1) 
  
    #new pos of walls when dragged
    def getWalls(self):
        wallsToKeep = []
        for walls in self.mode.walls:
            if not walls.containBackPack(walls.cx, walls.cy):
                wallsToKeep.append(walls)
            else: 
                self.mode.score += walls.score
        self.mode.walls = wallsToKeep
     
class GameMode(Mode):
    

    def appStarted(mode):

        mode.player = Player(mode)
        mode.stepsToTake = -1
        mode.prevKey = 'Right'
        mode.scrollX = 0
        mode.speed = 10
        mode.r = redDots(mode, random.randrange(mode.app.width))
        mode.dots = {(mode.r)}
        mode.w = Walls(mode, random.randrange(mode.app.width))
        mode.walls = [mode.w]
        mode.prevScrollXWalls, mode.prevScrollXDots = -1, -1
        mode.draggingWall = None
        mode.mouseX, mode.mouseY = mode.width/2, mode.height/2
        mode.score = 0
        mode.gameOver = False
        mode.win = False
        GameMode.spriteStripStarted(mode)
        GameMode.cursorStarted(mode)
        GameMode.backpackStarted(mode)
    
    def spriteStripStarted(mode):

        url1 = 'https://i.imgur.com/Ve9RVDj.png'
        mode.spritestrip1 = mode.loadImage(url1)
        mode.spritestrip2 = mode.spritestrip1.transpose(Image.FLIP_LEFT_RIGHT)
        mode.size = mode.spritestrip1.size

        mode.player.sprites.append(mode.spritestrip1.crop((0, 30, 160, 300)))
        #pos of the first stripped image
        
    def cursorStarted(mode):
        url2 = 'https://i.imgur.com/nURD1t0.png'
        mode.cursor1= mode.loadImage(url2)
        mode.cursor2 = mode.scaleImage(mode.cursor1, 1/10)
    
    def backpackStarted(mode):
        url3 = 'https://i.imgur.com/D9SEAg4.png'
        mode.backpack1 = mode.loadImage(url3)
        mode.backpack2 = mode.scaleImage(mode.backpack1, 1/10)

    
    def timerFired(mode):
        if mode.gameOver or mode.win:
            return
        elif mode.score >= 100:
            mode.win = True
            return
        else:
            if mode.stepsToTake > 0:
                GameMode.jump(mode)
                mode.stepsToTake -= 1
            elif mode.stepsToTake == 0:
                mode.player.sprites.insert(0, mode.spritestrip1.crop((170*
                mode.player.spriteCounter, 30, 
                160+170*mode.player.spriteCounter, 300)))
                #return to pos of stripped running character
                mode.stepsToTake = -1
            GameMode.placeNewDots(mode)
            GameMode.makeWalls(mode)
    

    def keyPressed(mode, event):
        if mode.gameOver or mode.win: return
        elif event.key == 'Right':
            mode.scrollX += mode.speed
            if mode.prevKey == 'Left': mode.player.spriteCounter = 1
            else:
                if (mode.player.spriteCounter < (mode.player.imageRowNum-1)*2):
                    mode.player.spriteCounter += 1
                else: mode.player.spriteCounter = 1
            GameMode.doStepRight(mode)
        elif event.key == "Left":
            mode.scrollX -= mode.speed
            if mode.prevKey == 'Right': mode.player.spriteCounter = 1
            else:
                if (mode.player.spriteCounter < (mode.player.imageRowNum-1)*2):
                    mode.player.spriteCounter += 1
                else: mode.player.spriteCounter = 1
            GameMode.doStepLeft(mode)
        elif event.key == "Up": mode.stepsToTake = 16
        elif (event.key == 'h'): mode.app.setActiveMode(mode.app.helpMode)
        elif (event.key == 'S'): GameMode.superHelp(mode)
    
    def superHelp(mode):
        s = '''
            You must score to 100 to win
            Hit red dots =  +5
            Put brown bricks into your backpack = +10
            Hit yellow dot = GAME OVER!!!

            Press up arrow to Jump. 
            Press L/R arrow to move L/R
        '''
        print(s)

    def doStepRight(mode):

        if mode.player.spriteCounter < (mode.player.imageRowNum-1):
            sprite = mode.spritestrip1.crop((165*
            (mode.player.spriteCounter), 30,165*(mode.player.spriteCounter+1), 
            300)) #pos of stripped character on the sprite sheet file
            mode.player.sprites.insert(mode.player.spriteCounter,sprite)

        elif mode.player.spriteCounter < (mode.player.imageRowNum*2)-1:
            sprite = mode.spritestrip1.crop(((165*
            (mode.player.spriteCounter-11), 
            300, 165+165*(mode.player.spriteCounter-11), 610)))
            mode.player.sprites.insert(mode.player.spriteCounter,sprite)
        mode.prevKey = 'Right'
    
    def doStepLeft(mode):

        if mode.player.spriteCounter < (mode.player.imageRowNum-1):
            sprite = mode.spritestrip2.crop((2048-
            (165*(mode.player.spriteCounter+1)), 30, 2048-(165*
            (mode.player.spriteCounter)), 300))
            #pos of stripped character on the flipped file
            mode.player.sprites.insert(mode.player.spriteCounter, sprite)
        elif mode.player.spriteCounter < (mode.player.imageRowNum*2)-1:
            sprite = mode.spritestrip2.crop((2048-165*
            (mode.player.spriteCounter-11+1), 
            300, 2048-165*(mode.player.spriteCounter-11), 610))
            mode.player.sprites.insert(mode.player.spriteCounter,sprite)
        mode.prevKey = 'Left'

    def jump(mode):

        if mode.prevKey == 'Right': 
            GameMode.jumpRight(mode)
            mode.scrollX += mode.speed
        elif mode.prevKey == "Left": 
            GameMode.jumpLeft(mode)   
            mode.scrollX -= mode.speed

        GameMode.hitDots(mode)

    def jumpRight(mode):

        #13 = first 4 stripped characters are in the last row 
        if mode.stepsToTake >= 13: 
            mode.sprite = mode.spritestrip1.crop((165*
            (16-mode.stepsToTake), 1515, 165*(16-mode.stepsToTake+1), 1760))
            #pos of stripped jumping characters
            mode.player.spriteCounter += 1
            mode.player.sprites.insert(mode.player.spriteCounter,mode.sprite)
        else: 
            mode.sprite = mode.spritestrip1.crop((165*
            (12-mode.stepsToTake), 
            1160, 165*(12-mode.stepsToTake+1), 1470))
            #pos of stripped jumping characters
            mode.player.spriteCounter += 1
            mode.player.sprites.insert(mode.player.spriteCounter,mode.sprite)
    
    def jumpLeft(mode):

        #13 = first 4 stripped characters are in the last row 
        if mode.stepsToTake >= 13: 
            mode.sprite = mode.spritestrip2.crop((2048-165*
            (16-mode.stepsToTake+1), 1510, 2048-165*(16-mode.stepsToTake), 
            1760)) #pos of stripped jumping characters (flipped)
            mode.player.spriteCounter += 1
            mode.player.sprites.insert(mode.player.spriteCounter,mode.sprite)
        else:
            mode.sprite = mode.spritestrip2.crop((2048-165*
                (12-mode.stepsToTake+1), 1160, 2048-165*(12-mode.stepsToTake), 
                1470)) #pos of stripped jumping characters (flipped)
            mode.player.spriteCounter += 1
            mode.player.sprites.insert(mode.player.spriteCounter,mode.sprite)

    def hitDots(mode):
        for elem in mode.dots:
            r = elem.r
            cx = elem.cx
            if cx-r <= 200+mode.scrollX <= cx+r and (
            mode.sprite.size[1] == 310): 
            #310 = height of stripped image that can reach the dot
                mode.dots.remove(elem)
                mode.score += elem.score
                if elem.color == 'yellow':
                    mode.gameOver = True
                break
        
    def mousePressed(mode, event):
        if mode.gameOver: return
        for walls in mode.walls:
            if walls.containPoints(event.x+mode.scrollX, event.y):
                mode.draggingWall = walls

    def mouseReleased(mode, event):
        mode.draggingWall = None

    def mouseDragged(mode, event):
        if mode.draggingWall is not None:
            mode.draggingWall.cx = event.x + mode.scrollX
            mode.draggingWall.cy = event.y 
            mode.draggingWall.getWalls()
        GameMode.mouseMoved(mode, event)
        
    def mouseMoved(mode, event):
        mode.mouseX = event.x
        mode.mouseY = event.y

    def placeNewDots(mode):

        #create new dot whenever player moved 200 pixels
        if mode.scrollX % 200 == 0 and mode.scrollX != 0:
            if mode.prevScrollXDots != mode.scrollX: #only create 1 dot
                while True:
                    num = random.randrange(mode.app.width)
                    if mode.scrollX < 0:
                            mode.x = (mode.scrollX-num)- mode.width
                    else:
                            mode.x = (mode.scrollX+num) + mode.width

                    mode.x1 = yellowDots(mode, mode.x)
                    mode.x2 = redDots(mode, mode.x)
                    L = [mode.x1, mode.x2]
                    mode.d = random.choice(L)
                    mode.dots.add((mode.d))
                    mode.prevScrollXDots = mode.scrollX
                    return

    def makeWalls(mode):
        
        #create new dot whenever player moved 300 pixels
        if mode.scrollX % 300 == 0 and mode.scrollX != 0:
            if mode.prevScrollXWalls != mode.scrollX: #only create 1 brick
                while True:
                    num = random.randrange(mode.app.width)
                    if mode.scrollX < 0:
                        mode.num = (mode.scrollX-num)- 400
                    else:
                        mode.num = (mode.scrollX+num) + 400
                    mode.w = Walls(mode, mode.num)
                    mode.walls.append((mode.w))
                    mode.prevScrollXWalls = mode.scrollX
                    return
    
    def drawGameOver(mode, canvas):
        canvas.create_rectangle(0,mode.height/2-50,mode.width,mode.height/2+50,
        fill = 'black')
        canvas.create_text(mode.width/2, mode.height/2,text = 'Game Over!'
        ,fill = 'white', font = 'Arial 60')
    
    def drawWin(mode, canvas):
        canvas.create_rectangle(00,mode.height/2-50,mode.width,mode.height/2+50,
        fill = 'blue')
        canvas.create_text(mode.width/2, mode.height/2,text = 'You won!'
        ,fill = 'white', font = 'Arial 60')

    def drawBackground(mode, canvas):
        
        canvas.create_rectangle(0,0,mode.width,mode.height,
        fill = 'light blue')
        canvas.create_rectangle(0,mode.height/2,mode.width,mode.height,fill = 
        'light green', outline = 'light green')
      

    def drawDots(mode, canvas):

        for dots in mode.dots:
            dots.draw(canvas)
    
    def drawWalls(mode, canvas):
        for wall in mode.walls:
            wall.draw(canvas)
    
    def drawSprite(mode, canvas):

        sprite = mode.player.sprites[mode.player.spriteCounter]
        canvas.create_image(mode.width/2, mode.height/2, image=
        ImageTk.PhotoImage(sprite))
    
    def drawBackPack(mode,canvas):

        canvas.create_image(mode.width-50, mode.height-50, 
        image=ImageTk.PhotoImage(mode.backpack2))
    
    def drawCursor(mode, canvas):

        canvas.create_image(mode.mouseX, mode.mouseY, 
        image=ImageTk.PhotoImage(mode.cursor2))
    
    def drawScore(mode, canvas):

        canvas.create_text(mode.width-30, 10, text = f"Score: {mode.score}", 
        anchor = 'ne', font = 'Arial 20 bold')

    def redrawAll(mode, canvas):

        GameMode.drawBackground(mode, canvas)
        GameMode.drawDots(mode, canvas)
        GameMode.drawWalls(mode, canvas)
        GameMode.drawSprite(mode, canvas)
        GameMode.drawBackPack(mode,canvas)
        GameMode.drawCursor(mode, canvas)
        GameMode.drawScore(mode, canvas)

        if mode.gameOver:
            GameMode.drawGameOver(mode, canvas)
        elif mode.win:
            GameMode.drawWin(mode, canvas)

class HelpMode(Mode):
    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, mode.width/2, 0, mode.height/2,fill = 'pink')
        font = f'Arial {mode.height//30} bold'
        canvas.create_text(mode.width/2, 50, text='This is the help screen!',
        font = font)
        SplashScreenMode.drawBackground(mode, canvas)
        canvas.create_text(mode.width/2, mode.height-50, text=
        'Press any key to return to the game!', font=font)

    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.gameMode)
        
class MyModalApp(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        app.gameMode = GameMode()
        app.helpMode = HelpMode()
        app.setActiveMode(app.splashScreenMode)


app = MyModalApp(width=400, height=400)


