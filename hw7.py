#################################################
# hw7.py: Tetris!
#
# Your name: Yo-Lei Chen
# Your andrew id: yoleic
#
# Your partner's name: Jackie Yang
# Your partner's andrew id: jacliny
#################################################

import cs112_f19_week7_linter
import math, copy, random
import random

from cmu_112_graphics import *
from tkinter import *

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

def playTetris():
    rows, cols, cellSize, margin = gameDimensions()
    width = cols * cellSize + 2 * margin
    height = rows * cellSize + 2 * margin
    runApp(width= width, height=height)

def gameDimensions():
    rows = 15
    cols = 10
    cellSize = 20
    margin = 25

    return (rows, cols, cellSize, margin)

def appStarted(app):
    app.rows, app.cols, app.cellSize, app.margin = gameDimensions()
    app.width = 2*app.margin + app.cellSize*app.cols
    app.height = 2*app.margin + app.cellSize*app.rows

    app.emptyColor = 'blue'
    app.board = [[app.emptyColor]*app.cols for r in range (app.rows)]

    # pre-load a few cells with known colors for testing purposes


        # Seven "standard" pieces (tetrominoes)

    iPiece = [
        [  True,  True,  True,  True ]
    ]

    jPiece = [
        [  True, False, False ],
        [  True,  True,  True ]
    ]

    lPiece = [
        [ False, False,  True ],
        [  True,  True,  True ]
    ]

    oPiece = [
        [  True,  True ],
        [  True,  True ]
    ]

    sPiece = [
        [ False,  True,  True ],
        [  True,  True, False ]
    ]

    tPiece = [
        [ False,  True, False ],
        [  True,  True,  True ]
    ]

    zPiece = [
        [  True,  True, False ],
        [ False,  True,  True ]
    ]

    app.tetrisPieces = [ iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, 
    zPiece ]
    app.tetrisPieceColors = [ "red", "yellow", "magenta", "pink", "cyan", 
    "green", "orange" ]
    newFallingPiece(app)
    app.isGameOver = False
    app.timerDelay = 200
    app.score = 0
    

def keyPressed(app, event):
    if event.key == 'r':
        appStarted(app)
    elif event.key == 'Up':
        rotateFallingPiece(app)
    elif app.isGameOver:
        return
    else:
        if event.key == 'Left':
            drow, dcol = 0, -1
        elif event.key == 'Right':
            drow, dcol = 0, 1
        elif event.key == 'Down':
            drow, dcol = 1, 0
        moveFallingPiece(app, drow, dcol)

def timerFired(app):
    if not app.isGameOver:
        if not moveFallingPiece(app, +1, 0):
            placeFallingPiece(app)
            if app.fallingPieceRow == 0:
                app.isGameOver = True
                return
            newFallingPiece(app)

def removeFullRows(app):
    count = 0
    rowCount = 0
    result = copy.deepcopy(app.board)
    for r in range(app.rows):
        for c in range(app.cols):
            if app.board[r][c] != app.emptyColor:
                count+=1
        if count == app.cols:
            result.pop(r)
            result.insert(0, [app.emptyColor]*app.cols)
            rowCount += 1
        count = 0
    app.board = result
    app.score += (rowCount)**2
    
def placeFallingPiece(app):

    for r in range(len(app.fallingPiece)):
        for c in range(len(app.fallingPiece[0])):
            if app.fallingPiece[r][c]:
                color = app.fallingPieceColor
                app.board[app.fallingPieceRow+r][app.fallingPieceCol+c] = color
    removeFullRows(app)

def newFallingPiece(app):
    randomIndex = random.randint(0, len(app.tetrisPieces) - 1)
    app.fallingPiece = app.tetrisPieces[randomIndex]
    app.fallingPieceColor = app.tetrisPieceColors[randomIndex]
    app.fallingPieceRow = 0
    app.fallingPieceCol = app.cols//2 - len(app.fallingPiece[0])//2

def moveFallingPiece(app, drow, dcol):
    app.fallingPieceCol += dcol
    app.fallingPieceRow += drow

    if not fallingPieceIsLegal(app, app.fallingPieceRow, 
        app.fallingPieceCol):

        app.fallingPieceCol -= dcol
        app.fallingPieceRow -= drow

        return False

    return True

def fallingPieceIsLegal(app, pieceRow, pieceCol):

    x0 = app.margin + pieceCol*app.cellSize
    y0 = app.margin + app.fallingPieceRow*app.cellSize
    x1 = app.margin + (pieceCol + len(app.fallingPiece[0]))*app.cellSize
    y1 = app.margin + (pieceRow + len(app.fallingPiece))*app.cellSize

    upperBound = y0 <= app.margin
    lowerBound = y1 > (app.height - app.margin)
    leftBound = x0 < app.margin
    rightBound = x1 > (app.width - app.margin)

    if(lowerBound or leftBound or rightBound):
        return False

    for r in range(len(app.fallingPiece)):
        for c in range(len(app.fallingPiece[0])):
            if app.fallingPiece[r][c]:
                if app.board[pieceRow + r][pieceCol + c] != app.emptyColor:
                    return False   
    return True

def rotateFallingPiece(app):
    piece = app.fallingPiece
    dimensionRow = len(app.fallingPiece)
    dimensionCol = len(app.fallingPiece[0])
    oldCol = app.fallingPieceCol
    oldRow = app.fallingPieceRow   

    newPiece = [[None]*dimensionRow for c in range(dimensionCol)]

    for r in range(dimensionRow):
        for c in range(dimensionCol):
            
            newPiece[(dimensionCol-1-c)][r] = piece[r][c] 

    app.fallingPiece = newPiece
    newRow = oldRow + dimensionRow//2 - len(newPiece)//2
    newCol = oldCol + dimensionCol//2 - len(newPiece[0])//2
    app.fallingPieceRow = newRow
    app.fallingPieceCol = newCol

    if not fallingPieceIsLegal(app, app.fallingPieceRow,app.fallingPieceCol): 
        app.fallingPiece = piece
        app.fallingPieceRow, app.fallingPieceCol = oldRow, oldCol
        return False
    

def drawFallingPiece(app, canvas):

    for r in range(len(app.fallingPiece)):
        for c in range(len(app.fallingPiece[0])):
            if app.fallingPiece[r][c] == True:
                drawCell(app, canvas, app.fallingPieceRow + r, 
                app.fallingPieceCol + c, app.fallingPieceColor)

def drawBoard(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = 'orange')
    for r in range(app.rows):
        for c in range(app.cols):
            drawCell(app, canvas, r, c, app.board[r][c])

def drawGameOver(app, canvas):
    canvas.create_rectangle(app.margin, app.height//4 - 30, app.width-app.margin
    , app.height//4 +30, fill = 'black')
    canvas.create_text(app.width/2, app.height//4, text='Game over!',
                           font='Arial 30 bold', fill = 'yellow')

def drawScore(app, canvas):
    canvas.create_text(app.width//2, app.margin//2, 
    text= "Score: " + str(app.score), font='Arial 15 bold', fill = 'blue')

def drawCell(app, canvas, r, c, color):

    canvas.create_rectangle(app.margin + c*app.cellSize, app.margin + 
        r*app.cellSize, app.margin + (c+1)*app.cellSize, app.margin + 
        (r+1)*app.cellSize, fill = color, width = 3)

def redrawAll(app, canvas):
    
    drawBoard(app, canvas)
    drawFallingPiece(app, canvas)
    drawScore(app, canvas)
    if app.isGameOver:
        drawGameOver(app, canvas)

#################################################
# main
#################################################

def main():
    cs112_f19_week7_linter.lint()
    playTetris()

if __name__ == '__main__':
    main()
