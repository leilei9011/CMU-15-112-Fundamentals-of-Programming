#################################################
# hw2.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_f19_week2_linter
import math
from tkinter import *
import random

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


def integral(f, a, b, N):
    area = 0
    barWidth = (b-a)/N
    for i in range(N):
        area += (f(a)+f(a+barWidth))/2*barWidth
        a += barWidth
    return area

def digitCount(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    num = n
    while(num>0):
        count+=1
        num= num//10
    return count

def isPrime(n): 
    if (n < 2):
        return False
    for factor in range(2,n):
        if (n % factor == 0):
            return False
    return True               


def primeFactorization(n):
    
    result = 0
    num = n
    if n == 2:
        return 0
    while(n>1):
        for x in range(2, num):
            if(isPrime(x) and (n/x)%1 ==0):
                result = result*(10**digitCount(x))+x
                break
        n /= x
    return result



def sumOfDigits(n):
    result = 0
    while(n>0):
        num = n%10
        n//=10
        result+=num
    return result

def isSmith(n):
    return sumOfDigits(n) == sumOfDigits(primeFactorization(n))

def nthSmithNumber(n):
    num = 0
    while (n>=0):
        num+=1
        if(isSmith(num)):
            n-=1
    return num

def printSmith(n):
    for x in range (n):
        print(nthSmithNumber(x))

def drawPattern1(points, canvas, width, height):
    Wbar = width/(points-1)
    Hbar = height/(points-1)

    for x in range(height):
        canvas.create_line(width,height-x*Hbar,x*Wbar, 0)
        canvas.create_line(0,height-x*Hbar,width-x*Wbar, 0)
        
    for y in range(width):
        canvas.create_line(width-y*Wbar,height,0, y*Hbar)
        canvas.create_line(y*Wbar,height,width, y*Hbar)


def drawPattern2(points, canvas, width, height):
    Wbar = width/((points-1)*2)
    Hbar = height/((points-1)*2)
    canvas.create_line(0, height/2, width, height/2)
    canvas.create_line(width/2, 0, width/2, height)

    n = 1
    while(n<(points-1)):
        canvas.create_line(n*Wbar, height/2, width/2, height/2-n*Hbar)
        canvas.create_line(n*Wbar, height/2, width/2, height/2+n*Hbar)
        n+=1

    n = 1
    while(n<(points-1)):
        canvas.create_line(width- n*Wbar, height/2, width/2, height/2-n*Hbar)
        canvas.create_line(width - n*Wbar, height/2, width/2, height/2+n*Hbar)
        n+=1
    
def drawPattern3(points, canvas, width, height):
    Wbar = width/(points-1)
    Hbar = height/(points-1)

    for x in range(points-1):
        canvas.create_line(0, x*Hbar, width,x*Hbar)

    for h in range(0, points, 2):
        for i in range(points-1):
            canvas.create_line(i*Wbar, h*Hbar, i*Wbar+Wbar/2, (h+1)*Hbar)
            canvas.create_line(i*Wbar+Wbar/2, (h+1)*Hbar, (i+1)*Wbar, h*Hbar)

    for w in range(1, points-1, 2):
        for z in range(points):
            canvas.create_line(z*Wbar, w*Hbar, z*Wbar, w*Hbar+Hbar)
              
def drawPattern4(canvas, width, height):

    points = 50
    Hbars = height/(points-1)
    Wbars = width/(points-1)

    for x in range(50):
        canvas.create_line(width/2, 0, 0, x*Hbars)
        canvas.create_line(width/2, 0, width, x*Hbars)

    for y in range(50):
        canvas.create_line(width/2, height, 0, y*Hbars)
        canvas.create_line(width/2, height, width, y*Hbars)

    for z in range(50):
        canvas.create_line(0, height/2, z*Wbars, 0)
        canvas.create_line(0, height/2, width-z*Wbars, height)
    
    for w in range(50):
        canvas.create_line(width, height/2, w*Wbars, 0)
        canvas.create_line(width, height/2, width-w*Wbars, height)


            
def playPig():
    start = input("press 0 to start game.")
    if start == "0":
        turn = 1
        total1 = 0
        total2 = 0
        while ((total1<100) and (total2<100)):

            if(turn%2!=0):          
                turn+=1
                end = 1
                while(end!=0 and total1<100):
                    command = input("Player1, please enter roll or hold")
                    if command=="hold":
                        end = 0
                    elif command=="roll" : 
                        dice = random.randint(1,6)
                        print(dice)
                        if(dice==1):
                            total1 = 0
                            end = 0
                        else:
                            total1 += dice
                            print(f'your score now is {total1}')
                    else:
                        print("Error. Enter roll or hold only")
            else:
                turn+=1
                end = 1
                while(end!=0 and total2<100):
                    command = input("Player2, please enter roll or hold")
                    if command=="hold":
                        end = 0
                    elif command == "roll":
                            
                        dice = random.randint(1,6)
                        print(dice)
                        if(dice==1):
                            total2=0
                            end = 0
                        else:
                            total2 += dice
                            print(f'your score now is {total2}')
                    else:
                        print("Error. Enter roll or hold only")
                        
        if(total1>total2):
            print ("Congrats Player 1! You are the winner!")
        else:
            print ("Congrats Player 2! You are the winner!")
    else:
        print("goodbye!")
        
                
                
    
    
    


#################################################
# Bonus/Optional functions for you to write
#################################################

def bonusCarrylessMultiply(x1, x2):
    return 42

def bonusPlay112(game):
    return 42

#################################################
# Test Functions
#################################################

def f1(x): return 42
def i1(x): return 42*x 
def f2(x): return 2*x  + 1
def i2(x): return x**2 + x
def f3(x): return 9*x**2
def i3(x): return 3*x**3
def f4(x): return math.cos(x)
def i4(x): return math.sin(x)
def testIntegral():
    print('Testing integral()...', end='')
    epsilon = 10**-4
    assert(almostEqual(integral(f1, -5, +5, 1), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f1, -5, +5, 10), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 1), 4,
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 250), (i2(2)-i2(1)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f3, 4, 5, 250), (i3(5)-i3(4)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f4, 1, 2, 250), (i4(2)-i4(1)),
                      epsilon=epsilon))
    print("Passed!")

def testNthSmithNumber():
    print('Testing nthSmithNumber()... ', end='')
    assert(nthSmithNumber(0) == 4)
    assert(nthSmithNumber(1) == 22)
    assert(nthSmithNumber(2) == 27)
    assert(nthSmithNumber(3) == 58)
    assert(nthSmithNumber(4) == 85)
    assert(nthSmithNumber(5) == 94)
    print('Passed.')

def runDrawPattern1(points, width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawPattern1(points, canvas, width, height)
    root.mainloop()
    print("bye!")

def runDrawPattern2(points, width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawPattern2(points, canvas, width, height)
    root.mainloop()
    print("bye!")

def runDrawPattern3(points, width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawPattern3(points, canvas, width, height)
    root.mainloop()
    print("bye!")

def runDrawPattern4(width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawPattern4(canvas, width, height)
    root.mainloop()
    print("bye!")

def testDrawPatterns():
    print('** Note: You need to manually test drawPatterns()')
    print('Calling runDrawPattern1(5, 400, 400):')
    runDrawPattern1(5, 400, 400)
    print('Calling runDrawPattern1(10, 800, 400):')
    runDrawPattern1(10, 800, 400)
    print('Calling runDrawPattern2(5, 400, 400):')
    runDrawPattern2(5, 400, 400)
    print('runDrawPattern2(10, 800, 400):')
    runDrawPattern2(10, 800, 400)
    print('runDrawPattern3(5, 400, 400):')
    runDrawPattern3(5, 400, 400)
    print('runDrawPattern3(10, 800, 400)')
    runDrawPattern3(10, 800, 400)
    print('runDrawPattern4(600, 600)')
    runDrawPattern4(600, 600)

def testPlayPig():
    print('** Note: You need to manually test playPig()')

def testBonusCarrylessMultiply():
    print("Testing bonusCarrylessMultiply()...", end="")
    assert(bonusCarrylessMultiply(643, 59) == 417)
    assert(bonusCarrylessMultiply(6412, 387) == 807234)
    print("Passed!")

def testBonusPlay112():
    print("Testing bonusPlay112()... ", end="")
    assert(bonusPlay112( 5 ) == "88888: Unfinished!")
    assert(bonusPlay112( 521 ) == "81888: Unfinished!")
    assert(bonusPlay112( 52112 ) == "21888: Unfinished!")
    assert(bonusPlay112( 5211231 ) == "21188: Unfinished!")
    assert(bonusPlay112( 521123142 ) == "21128: Player 2 wins!")
    assert(bonusPlay112( 521123151 ) == "21181: Unfinished!")
    assert(bonusPlay112( 52112315142 ) == "21121: Player 1 wins!")
    assert(bonusPlay112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(bonusPlay112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(bonusPlay112( 51211 ) == "28888: Player 2: occupied!")
    assert(bonusPlay112( 5122221 ) == "22888: Player 1: occupied!")
    assert(bonusPlay112( 51261 ) == "28888: Player 2: offboard!")
    assert(bonusPlay112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testIntegral()
    testNthSmithNumber()
    testDrawPatterns()
    testPlayPig()
    #testBonusCarrylessMultiply()
    #testBonusPlay112()

def main():
    cs112_f19_week2_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
