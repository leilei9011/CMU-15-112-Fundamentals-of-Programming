###############################################################################
# Writing Session 7, Coding Portion: [19 pts]
                                  
# Do not edit these lines:
#   user: 'yoleic@andrew.cmu.edu' (do not edit this!)
#   downloaded at: '2019-10-11 15:36:09' (do not edit this!)
#   downloaded ip: '128.237.157.147' (do not edit this!)
#   security code: '323021152668429521YSNEMDDCRERGZ1ENY1GGY' (do not edit this!)
                
# Note #1: If you are not in a proctored writing-session lab, close this file
# immediately and email koz@cmu.edu and mdtaylor@andrew.cmu.edu to let
# us know that this occurred.
        
# Note #2: Do not edit this header, only edit the code below the header.
                               
# Note #3: Select-all and copy this entire file, all of it, exactly as it
# is here, paste it into your ws7.py starter file, then edit it, and submit
# that edited file to Autolab while you are still in the proctored
# writing-session lab.
         
# Starting from the starter code below, write an animation
# according to these rules:
             
# 1. Moving a Dot with Arrows and Wraparound
# Add a blue dot of radius 10, initially in the middle of the canvas
# that moves vertically in response to
# up and down arrows (not left and right arrows), 13 pixels per arrow press,
# and uses wraparound, so if any part of the dot would extend beyond an edge,
# instead the entire dot appears just inside the opposite edge.
                 
# 2. Bouncing Square
# Add a yellow bouncing 20x20 square.  It should start anyhwere you wish on
# the canvas, moving with dx=5 and dy=10.  The square should bounce
# back-and-forth in both the x and y dimensions.  Here, the square may extend
# partly beyond an edge, at which point it should bounce back in the opposing
# direction (so you do not have to adjust the square to exactly sit against an
# edge, just bounce when it extends beyond an edge).  Do not use OOP here to
# store the square or its location.
              
# 3. Adding and Deleting Shapes with OOP
# Note: for this part only, you need to use a class Dot that stores the cx, cy
# locations of each green dot.  With that, each time the user clicks the mouse,
# draw a new green dot of radius 10 in that location (so there are more green
# dots as the user repeatedly presses the mouse).  To do this, add a Dot
# instance to the list app.dots.  Note that you do not have to delete any
# green dots.
            
###############################################################################
                                  
from cmu_112_graphics import *
from tkinter import *
        
class Dot(object):
    
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.r = 10

def appStarted(app):
    app.cx = app.width/2
    app.cy = app.height/2
    app.r = 10

    app.squareLeft = app.width/2
    app.squareTop = app.height/2
    app.squareSize = 20
    app.dx = 5
    app.dy = 10

    app.dots = []
                               
def keyPressed(app, event):
    if event.key == 'Up':
        app.cy -= 13
        if (app.cy + app.r) <= 0:
            app.cy = app.height + app.r
    elif event.key == 'Down':
        app.cy += 13
        if (app.cy - app.r) >= app.height:
            app.cy = 0 - app.r
    
def mousePressed(app, event):
    cx = event.x
    cy = event.y

    dot = Dot(cx, cy)
    app.dots.append(dot)
            
def timerFired(app):
    app.squareLeft += app.dx
    app.squareTop += app.dy

    if ((app.squareLeft + app.squareSize) < 0) or (app.squareLeft > app.width):
        app.dx = (-app.dx)
    if ((app.squareTop + app.squareSize) < 0) or (app.squareTop > app.height):
        app.dy = (-app.dy)
                    
def redrawAll(app, canvas):
    canvas.create_oval(app.cx-app.r, app.cy-app.r, app.cx+app.r, app.cy+app.r, 
    fill = 'blue')
    canvas.create_rectangle(app.squareLeft, app.squareTop, app.squareLeft +
    app.squareSize, app.squareTop + app.squareSize, fill = 'yellow')
    for circs in app.dots:
        canvas.create_oval(circs.cx - circs.r, circs.cy - circs.r, 
        circs.cx + circs.r, circs.cy + circs.r, fill = 'green')
                 
runApp(width=400, height=150) # 400x150