#################################################
# hw11.py
#
# Your name: Yo-Lei Chen
# Your andrew id: yoleic
#
# Your hw11 partner's name: Jackie Yang
# Your hw11 partner's andrew id: jaclyny
#
#################################################

import cs112_f19_week11_linter
import math 
import os
import string
import copy, time

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

def confirmPolicies():
    # Replace each 42 with True or False according to the course policies.
    # If you are unsure, testConfirmPolicies() below contains the answers.
    # This is just to be sure you understand those policies!
    # We very much encourage you to collaborate, but we also want
    # you to do it right.  Be sure both of you are working closely together,
    # and both of you are contributing and learning the material well.
    # Have fun!!!!! 
    return  {
    'I can work solo on hw11': True,
    'I can work with one partner on hw11': True,
    ("I must list my hw11 partner's name and andrewId at the top" +
     "of my hw11.py file that I submit"): True,
    'I can switch hw11 partners and then work with a new partner': False,
    'My hw11 partner must be in 112 this semester': True,
    'My hw11 partner must be in the same lecture or section as me': False,
    "I can look at my hw11 partner's code": True,
    "I can copy some of hw11 partner's code": False,
    "I can help my hw11 partner debug their code": True,
    "I can electronically transfer some of my code to my hw11 partner": False,
    ("I can tell my hw11 partner line-by-line, character-by-character " +
     "what to type so their code is nearly-identical to mine."): False,
    }

"""
returns the path to the largest file in the folder
"""
def findLargestFile(path): 

    return findLargestFileHelper(path, largestFile = '', largestSize = -1)

"""
helper: take in a list of file and current largest file 
to compare files with the current largets file 
"""
def findLargestFileHelper(path, largestFile, largestSize): 
    if os.path.isfile(path):
        return path
    else:
        for filename in os.listdir(path): #loop through the files in the folder

            curFile = findLargestFileHelper(os.path.join(path, filename),
            largestFile, largestSize) 

            if curFile.endswith('.DS_Store'): #ignore .DS_Store files
                continue
            elif curFile == '': #base case
                curSize = 0
            else:
                curSize = os.path.getsize(curFile)
            if curSize > largestSize:
                largestFile = curFile
                largestSize = curSize
        
        if largestSize == -1: #if there are no files, '' is returned
            return '' 
        return largestFile
 


#evaluate the value of a legal arithmetic expression in prefix notation
def evalPrefixNotation(L): 
    return evalPrefixNotationHelper(L, [])


def stri(a, b):
    result = 0
    while(result < len(a) and result < len(b)):
        if (a[result] != b[result]):
            print(result)
            return result
        else:
            result += 1
    print(result)
    return result;

def evalPrefixNotationHelper(L, numbers):

    if len(L) == 0: return numbers[0] 

    elif len(L) == 1 and type(L[0]) == int: return L.pop()

    operator = L.pop() #start with the last elem and work backwards
    if type(operator) == int:
        numbers.append(operator) #store operands in a list
        return evalPrefixNotationHelper(L, numbers)
    elif operator in ['+', '-', '*']:
        numbers.append(eval(str(numbers.pop()) + operator + str(numbers.pop())))
        # remove operands from list that has been calculated and put the newly 
        # calculated num into the list

        return evalPrefixNotationHelper(L, numbers)
    else:
        raise Exception('Unknown operator: ' + operator)

class State(object):
    def __eq__(self, other): return ((other != None) 
    and (self.__dict__ == other.__dict__))
    def __hash__(self): return hash(str(self.__dict__)) 
    def __repr__(self): return str(self.__dict__)

class BacktrackingPuzzleSolver(object):
    def solve(self, checkConstraints=True, printReport=False):
        self.moves = [ ]
        self.states = set()
        # If checkConstraints is False, then do not check the backtracking
        # constraints as we go (so instead do an exhaustive search)
        self.checkConstraints = checkConstraints
        # Be sure to set self.startArgs and self.startState in __init__
        self.startTime = time.time()
        self.solutionState = self.solveFromState(self.startState)
        self.endTime = time.time()
        if (printReport): self.printReport()
        return (self.moves, self.solutionState)

    def printReport(self):
        print()
        print('***********************************')
        argsStr = str(self.startArgs).replace(',)',')') # remove singleton comma
        print(f'Report for {self.__class__.__name__}{argsStr}')
        print('checkConstraints:', self.checkConstraints)
        print('Moves:', self.moves)
        print('Solution state: ', end='')
        if ('\n' in str(self.solutionState)): print()
        print(self.solutionState)
        print('------------')
        print('Total states:', len(self.states))
        print('Total moves: ', len(self.moves))
        millis = int((self.endTime - self.startTime)*1000)
        print('Total time:  ', millis, 'ms')
        print('***********************************')

    def solveFromState(self, state):
        if state in self.states:
            # we have already seen this state, so skip it
            return None
        self.states.add(state)
        if self.isSolutionState(state):
            # we found a solution, so return it!
            return state
        else:
            for move in self.getLegalMoves(state):
                # 1. Apply the move
                childState = self.doMove(state, move)
                # 2. Verify the move satisfies the backtracking constraints
                #    (only proceed if so)
                if ((self.stateSatisfiesConstraints(childState)) or
                    (not self.checkConstraints)):
                    # 3. Add the move to our solution path (self.moves)
                    self.moves.append(move)
                    # 4. Try to recursively solve from this new state
                    result = self.solveFromState(childState)
                    # 5. If we solved it, then return the solution!
                    if result != None:
                        return result
                    # 6. Else we did not solve it, so backtrack and
                    #    remove the move from the solution path (self.moves)
                    self.moves.pop()
            return None

    # You have to implement these:

class ABCStateSolver(BacktrackingPuzzleSolver):

    def __init__(self, constraints, aLocation):

        self.constraints = constraints
        self.aLocation = aLocation
        self.startArgs = (constraints, aLocation)
        self.startState = ABCState([aLocation])

        self.size = 5 # length of col/row
        self.movesMap = self.getMovesMap(constraints) 
        self.alphabets = list(string.ascii_uppercase) 

    '''
    crates a dictionary that stores all possible moves a letter can be placed
    ignoring the constraints
    '''
    def getMovesMap(self, constraints):
        movesMap = dict()
        lengthConstraints = len(constraints)
        colNum  = self.size
        rowNum = self.size

        self.getCol(movesMap, colNum, rowNum, constraints)
        self.getRow(movesMap, rowNum, colNum, constraints)
        self.getDiagnol(movesMap, rowNum, colNum, constraints)

        return movesMap

    '''
    store values of the letter on the same col in dict movesMap
    '''
    def getCol(self, movesMap, rowNum, colNum, constraints):

        for c in range(colNum):
            index0, index1 = c+1, (len(constraints)-1-self.size-1-c)
            char1 = self.constraints[index0]
            char2 = self.constraints[index1]
            movesSet = set()
            
            for r in range(rowNum):
                movesSet.add((r, c))

            movesMap[char1], movesMap[char2] = movesSet, movesSet
    
    '''
    store values of the letter on the same row in dict movesMap
    '''
    def getRow(self, movesMap, rowNum, colNum, constraints):

        for r in range(rowNum):
            index0, index1 = colNum+1+r+1, len(constraints)-1-r
            char1 = self.constraints[index0]
            char2 = self.constraints[index1]
            movesSet = set()
            
            for c in range(colNum):
                movesSet.add((r, c))

            movesMap[char1], movesMap[char2] = movesSet, movesSet
    
    '''
    store values of the letter on the same diagnol in dict movesMap
    '''
    def getDiagnol(self, movesMap, rowNum, colNum, constraints):

        #top-left and bottom-right diag 
        for c in range(colNum):
            index0, index1 = 0, 2*colNum + 1 + 1
            char1 = self.constraints[index0]
            char2 = self.constraints[index1]
            movesSet = set()
            
            for pos in range(rowNum): movesSet.add((pos, pos))

            movesMap[char1], movesMap[char2] = movesSet, movesSet

        #top-right and bottom-left diag
        for c in range(colNum):
            index0, index1 = len(constraints)-1-rowNum, colNum + 1
            char1 = self.constraints[index0]
            char2 = self.constraints[index1]
            movesSet = set()
            
            for pos in range(rowNum): movesSet.add((pos, colNum-1-pos))

            movesMap[char1], movesMap[char2] = movesSet, movesSet


    def stateSatisfiesConstraints(self, state):
        row1, col1 = state.letterLocationsList[-1]
        row2, col2 = state.letterLocationsList[-2]

        #check if the current letter is around the prev letter
        return abs(row1-row2)<=1 and abs(col1-col2)<=1

    def isSolutionState(self, state):
        resultLength = len(self.constraints)+1 #length of constraints + A
        return  resultLength == len(state.letterLocationsList)

    def getLegalMoves(self, state):
        nextIndex = len(state.letterLocationsList) #next elem index in list
        char = self.alphabets[nextIndex] 
        legalMoves = []
    
        for move in (self.movesMap[char]):
            if not(move in state.letterLocationsList): #add unused position
                legalMoves += [move]
        return legalMoves

    '''
    return a new state that results from applying the given
    move to the given state
    '''
    def doMove(self, state, move):
        newLetterLocationList = state.letterLocationsList + [move]
        return ABCState(newLetterLocationList)

class ABCState(State):
    
    def __init__(self, letterLocationsList):

        self.letterLocationsList = letterLocationsList
        self.size = 5

    def getBoard(self):
        alphaList = list(string.ascii_uppercase)
        board = [['-']*self.size for i in range(self.size)]

        for index in range(len(self.letterLocationsList)):
            r, c = self.letterLocationsList[index]
            board[r][c] = alphaList[index]
        
        return board

def solveABC(constraints, aLocation):
    move, solutionState =  ABCStateSolver(constraints, aLocation).solve()
    if solutionState == None:
        return None
    else:
        return solutionState.getBoard()
    


def flatten(L):
    # This is bonus!
    return 42

################################################
# ignore_rest:  place all your graphics and tests below here!
################################################

from cmu_112_graphics import *
from tkinter import *


class FreddyFractalViewer(App):

    def appStarted(self):
        self.level = 1
        scale = 7
        self.r = min(self.width/scale, self.height/scale)
        self.cx = self.width/2
        self.cy = self.height/2

    def keyPressed(self, event): 
        if event.key in ['Up', 'Right']: 
            self.level += 1
        elif event.key in ['Down', 'Right'] and self.level>0:
            self.level -= 1

    def drawFacialFeatures(self, canvas, cx, cy, r):

        self.drawMouthCirc(canvas, cx, cy, r)
        self.drawNose(canvas, cx, cy, r)
        self.drawEyes(canvas, cx, cy, r)
        self.drawMouth(canvas, cx, cy, r)
    
    def drawMouthCirc(self, canvas, cx, cy, r):
        #draw mouth circ
        scale2 = 2
        sclae3 = 3
        scale15 = 15

        radius = r//scale2
        centerX = cx
        centerY = cy + r//sclae3
        canvas.create_oval(centerX-radius, centerY-radius, 
        centerX+radius, centerY + radius, fill = 'tan', width = r//scale15)

    def drawNose(self, canvas, cx, cy, r):
        #draw nose 
        scale2 = 2
        scale3 = 3

        centerX = cx
        centerY = cy + r//scale3
        radius = r//scale2
        noseR = radius//scale3
        noseX = centerX
        noseY = centerY - radius//scale2
        canvas.create_oval(noseX-noseR, noseY-noseR, noseX+noseR, noseY+noseR, 
        fill = 'black')

    def drawMouth(self, canvas, cx, cy, r):
        #draw mouth
        scale3 = 3
        scale4 = 4
        scale5 = 5

        leftLipX, midLipX, rightLipX = cx - r / scale4, cx, cx + r / scale4
        topLipY, bottomLipY = cy + r / scale4, cy + scale3*r/scale5
        lipWid = r//13

        canvas.create_arc(leftLipX, topLipY,
                          midLipX, bottomLipY,
                          fill="black", start=180, extent=180,
                          style=ARC, width=lipWid)

        canvas.create_arc(midLipX, topLipY,
                          rightLipX, bottomLipY,
                          fill="black", start=180, extent=180,
                          style=ARC, width=lipWid)
        
    def drawEyes(self, canvas, cx, cy, r):
        #draw eyes

        scale3 = 3
        eyesR1 = r//scale3
        eyesX1, eyesY1 = cx-eyesR1, cy-eyesR1
        eyesX2, eyesY2 = cx + eyesR1, cy - eyesR1
        eyesR2 = r//6

        canvas.create_oval(eyesX1-eyesR2, eyesY1-eyesR2, eyesX1+eyesR2, 
        eyesY1+eyesR2, fill = 'black')
        canvas.create_oval(eyesX2-eyesR2, eyesY2-eyesR2, eyesX2+eyesR2, 
        eyesY2+eyesR2, fill = 'black')

    def teddyFace(self, canvas, cx, cy, r):
        scale15 = 15
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = 'brown', 
        width = r//15) #draw face
        self.drawFacialFeatures(canvas, cx, cy, r) #draw facial features

    '''
    draw n level of Freddies using recursion
    '''
    def fractalFreddy(self, canvas, cx, cy, r, level):
        
        if level == 0:
            return 
        elif level == 1:
            self.teddyFace(canvas, cx, cy, r)
        else:
            scale = 1.5
            angle = 45
            scale2 = 2
            dx = scale*r*math.cos(math.radians(angle))
            dy = scale*r*math.sin(math.radians(angle))
            self.fractalFreddy(canvas, cx-dx, cy-dy, r//scale2, level-1)
            self.fractalFreddy(canvas, cx+dx, cy-dy, r//scale2, level-1)
            self.teddyFace(canvas, cx, cy, r)
        

    def redrawAll(self, canvas):
        self.fractalFreddy(canvas, self.cx, self.cy, self.r, self.level)

def runFreddyFractalViewer():
    FreddyFractalViewer(width=1000, height=1000)

#################################################
# Test Functions
#################################################

def testConfirmPolicies():
    print('Testing confirmPolicies()...', end='')
    truePolicies = [ 
        'I can work solo on hw11',
        'I can work with one partner on hw11',
        ("I must list my hw11 partner's name and andrewId at the top" +
         "of my hw11.py file that I submit"),
        'My hw11 partner must be in 112 this semester',
        "I can look at my hw11 partner's code",
        "I can help my hw11 partner debug their code",
    ]
    falsePolicies = [
        'I can switch hw11 partners and then work with a new partner',
        'My hw11 partner must be in the same lecture or section as me',
        "I can copy some of hw11 partner's code",
        "I can electronically transfer some of my code to my hw11 partner",
        ("I can tell my hw11 partner line-by-line, character-by-character " +
         "what to type so their code is nearly-identical to mine."),
    ]
    policies = confirmPolicies()
    # True policies:
    for policy in truePolicies:
        assert(policies[policy] == True)
    # False policies (the opposite of these are actually policies)
    for policy in falsePolicies:
        assert(policies[policy] == False)
    print('Passed!')

def testFindLargestFile():
    print('Testing findLargestFile()...', end='')
    assert(findLargestFile('sampleFiles/folderA') ==
                           'sampleFiles/folderA/folderC/giftwrap.txt')
    assert(findLargestFile('sampleFiles/folderB') ==
                           'sampleFiles/folderB/folderH/driving.txt')
    assert(findLargestFile('sampleFiles/folderB/folderF') == '')
    print('Passed!')

def testEvalPrefixNotation():
    print('Testing evalPrefixNotation()...', end='')
    assert(evalPrefixNotation([42]) == 42)
    assert(evalPrefixNotation(['+', 3, 4]) == 7)
    assert(evalPrefixNotation(['-', 3, 4]) == -1)
    assert(evalPrefixNotation(['-', 4, 3]) == 1)
    assert(evalPrefixNotation(['+', 3, '*', 4, 5]) == 23)
    assert(evalPrefixNotation(['+', '*', 2, 3, '*', 4, 5]) == 26)
    assert(evalPrefixNotation(['*', '+', 2, 3, '+', 4, 5]) == 45)
    assert(evalPrefixNotation(['*', '+', 2, '*', 3, '-', 8, 7,
                               '+', '*', 2, 2, 5]) == 45)
  
    raisedAnError = False
    try:
        evalPrefixNotation(['^', 2, 3])
    except:
        raisedAnError = True
    assert(raisedAnError == True)
    print('Passed.')

def testSolveABC():
    print('Testing solveABC()...', end='')
    constraints = 'CHJXBOVLFNURGPEKWTSQDYMI'
    aLocation = (0,4)
    board = solveABC(constraints, aLocation)
    solution = [['I', 'J', 'K', 'L', 'A'],
                ['H', 'G', 'F', 'B', 'M'],
                ['T', 'Y', 'C', 'E', 'N'],
                ['U', 'S', 'X', 'D', 'O'],
                ['V', 'W', 'R', 'Q', 'P']
               ]
    assert(board == solution)

    constraints = 'TXYNFEJOQCHIMBDSUWPGKLRV'
    aLocation = (2,4)
    board = solveABC(constraints, aLocation)
    solution = [['V', 'U', 'S', 'O', 'P'],
                ['W', 'T', 'N', 'R', 'Q'],
                ['X', 'L', 'M', 'C', 'A'],
                ['K', 'Y', 'H', 'D', 'B'],
                ['J', 'I', 'G', 'F', 'E'],
               ]
    assert(board == solution)

    constraints = 'TXYNFEJOQCHIMBDSUPWGKLRV' # swapped P and W
    aLocation = (2,4)
    board = solveABC(constraints, aLocation)
    solution = None
    assert(board == solution)
    print('Passed!')

def testFlatten():
    print('Testing bonus flatten()...', end='')
    assert(flatten([1,[2]]) == [1,2])
    assert(flatten([1,2,[3,[4,5],6],7]) == [1,2,3,4,5,6,7])
    assert(flatten(['wow', [2,[[]]], [True]]) == ['wow', 2, True])
    assert(flatten([]) == [])
    assert(flatten([[]]) == [])
    assert(flatten(3) == 3)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    #testConfirmPolicies()
    #testFindLargestFile()
    #testEvalPrefixNotation()
    #testSolveABC()
    #runFreddyFractalViewer()
    stri("abc", "abcd")
    #testFlatten() # bonus

def main():
    cs112_f19_week11_linter.lint()
    testAll()

if (__name__ == '__main__'):
    main()
