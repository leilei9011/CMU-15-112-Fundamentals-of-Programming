#################################################
# writing_session3_solutions.py
#
# Your name: Yo-Lei Chen
# Your andrew id: yoleic
#################################################

import cs112_f19_week3_linter
import math
from tkinter import *
import string

#################################################
# Replace -1 with your code from the sheet of paper
# your TA gave you and that you just signed!!!!
#################################################

def getMyMagicCode():
    myMagicCode = 102   # <-- Replace this value here
    return myMagicCode

def actuallyDrawTheFlag():
    return True # <-- Replace this with True to draw the flag

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

def rotateString(s, k):
    if len(s)==0 or len(s)==1:
        return s
    while k!=0:
        if k>0:
            s = s[1:len(s)]+s[0]
            k-=1
        else:
            s = s[len(s)-1]+s[:len(s)-1]
            k+=1
    return s


def applyCaesarCipher(message, shift):
    shift = shift%len(string.ascii_uppercase)
    newMsg = ''
    for i in range(len(message)):
        elem = message[i]
        if elem.isalpha():
            if elem.isupper():
                start = ord("A")
            else:
                start = ord("a")
            index = ord(elem)-start
            newIndex = (index+shift)%len(string.ascii_uppercase)
            elem = chr(newIndex+start)
        newMsg += elem
    return newMsg

def hasBalancedParentheses(s):
    return 42

def largestNumber(s):
    return 42

def longestSubpalindrome(s):
    longest=''
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            string = s[i:j]
            reverse = string[::-1]
            if string == reverse:
                if len(string)>=len(longest) and string>longest:
                    longest = string
    return longest


def collapseWhitespace(s):
    return 42

def topScorer(data):
    return 42

def drawFlagOfQatar(canvas, width, height):
    canvas.create_text(width/2, height/2, text='<TBD: Draw Flag of Qatar>')

def drawFlagOfTheEU(canvas, width, height):
    canvas.create_rectangle(0,0,width,height,fill = "blue")
    numCircs = 12
    dTheta = 2*math.pi/numCircs
    x0, y0 = width//2, height//2
    r0 = height/3
    r1 = height/16
    for circs in range(numCircs):
        theta = dTheta*circs
        x1, y1 = x0 + math.cos(theta)*r0, y0 - math.sin(theta)*r0
        canvas.create_oval(x1+r1, y1+r1, x1-r1, y1-r1, fill="yellow")

#################################################
# Test Functions
#################################################

def testRotateString():
    print("Testing rotateString()...", end="")
    assert(rotateString("abcde", 0) == "abcde")
    assert(rotateString("abcde", 1) == "bcdea")
    assert(rotateString("abcde", 2) == "cdeab")
    assert(rotateString("abcde", 3) == "deabc")
    assert(rotateString("abcde", 4) == "eabcd")
    assert(rotateString("abcde", 5) == "abcde")
    assert(rotateString("abcde", 25) == "abcde")
    assert(rotateString("abcde", 28) == "deabc")
    assert(rotateString("abcde", -1) == "eabcd")
    assert(rotateString("abcde", -2) == "deabc")
    assert(rotateString("abcde", -3) == "cdeab")
    assert(rotateString("abcde", -4) == "bcdea")
    assert(rotateString("abcde", -5) == "abcde")
    assert(rotateString("abcde", -25) == "abcde")
    assert(rotateString("abcde", -28) == "cdeab")
    print("Passed!")

def testApplyCaesarCipher():
    print("Testing applyCaesarCipher()...", end="")
    assert(applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 3) ==
                             "defghijklmnopqrstuvwxyzabc")
    assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
    assert(applyCaesarCipher("1234", 6) == "1234")
    assert(applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 25) ==
                             "zabcdefghijklmnopqrstuvwxy")
    assert(applyCaesarCipher("We Attack At Dawn", 2)  == "Yg Cvvcem Cv Fcyp")
    assert(applyCaesarCipher("We Attack At Dawn", 4)  == "Ai Exxego Ex Hear")
    assert(applyCaesarCipher("We Attack At Dawn", -1) == "Vd Zsszbj Zs Czvm")
    # And now, the whole point...
    assert(applyCaesarCipher(applyCaesarCipher('This is Great', 25), -25)
           == 'This is Great')
    print("Passed.")

def testHasBalancedParentheses():
    print("Testing hasBalancedParentheses()...", end="")
    assert(hasBalancedParentheses("()") == True)
    assert(hasBalancedParentheses("") == True)
    assert(hasBalancedParentheses("())") == False)
    assert(hasBalancedParentheses("()(") == False) 
    assert(hasBalancedParentheses(")(") == False)
    assert(hasBalancedParentheses("(()())") == True)
    assert(hasBalancedParentheses("((()())(()(()())))") == True)
    assert(hasBalancedParentheses("((()())(()((()())))") == False)
    assert(hasBalancedParentheses("((()())(((()())))") == False)
    print("Passed!")

def testLargestNumber():
    print("Testing largestNumber()...", end="")
    assert(largestNumber("I saw 3") == 3)
    assert(largestNumber("3 I saw!") == 3)
    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17)
    assert(largestNumber("I saw 3 dogs, 1700 cats, and 14 cows!") == 1700)
    assert(largestNumber("One person ate two hot dogs!") == None)
    print("Passed!")

def testLongestSubpalindrome():
    print("Testing longestSubpalindrome()...", end="")
    assert(longestSubpalindrome("ab-4-be!!!") == "b-4-b")
    assert(longestSubpalindrome("abcbce") == "cbc")
    assert(longestSubpalindrome("aba") == "aba")
    assert(longestSubpalindrome("a") == "a")
    print("Passed!")

def testCollapseWhitespace():
    print("Testing collapseWhitespace()...", end="")
    assert(collapseWhitespace("a\nb") == "a b")
    assert(collapseWhitespace("a\n   \t    b") == "a b")
    assert(collapseWhitespace("a\n   \t    b  \n\n  \t\t\t c   ") == "a b c ")
    assert(collapseWhitespace("abc") == "abc")
    assert(collapseWhitespace("   \n\n  \t\t\t  ") == " ")
    assert(collapseWhitespace(" A  \n\n  \t\t\t z  \t\t ") == " A z ")
    print("Passed!")

def testTopScorer():
    print('Testing topScorer()...', end='')
    data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''
    assert(topScorer(data) == 'Fred')

    data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
    assert(topScorer(data) == 'Wilma')

    data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
    assert(topScorer(data) == 'Fred,Wilma')
    assert(topScorer('') == None)
    print('Passed!')

def runDrawFlagOfQatar(width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawFlagOfQatar(canvas, width, height)
    root.mainloop()
    print("bye!")

def drawFlagCheck():
    if (actuallyDrawTheFlag() == False):
        print('    Skipping this test for now.')
        print('    To draw the flag, edit actuallyDrawTheFlag()')
        print('    (at the top of your file) to return True instead of False.')
    return actuallyDrawTheFlag()

def testDrawFlagOfQatar():
    print('Testing drawFlagOfQatar()...')
    if (drawFlagCheck()):
        print('  Calling runDrawFlagOfQatar(400, 400):')
        runDrawFlagOfQatar(400, 400)
        #print('  Calling runDrawFlagOfQatar(800, 400):')
        #runDrawFlagOfQatar(800, 400)

def runDrawFlagOfTheEU(width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawFlagOfTheEU(canvas, width, height)
    root.mainloop()
    print("bye!")

def testDrawFlagOfTheEU():
    print('Testing drawFlagOfTheEU()...')
    if (drawFlagCheck()):
        print('  Calling runDrawFlagOfTheEU(400, 400):')
        runDrawFlagOfTheEU(400, 400)
        #print('  Calling runDrawFlagOfTheEU(800, 400):')
        #runDrawFlagOfTheEU(800, 400)

#################################################
# testAll and main
#################################################

# DO NOT MODIFY THIS FUNCTION!!!!
def getRequiredFunctions():
    # DO NOT MODIFY THIS FUNCTION!!!!!
    magicCode = getMyMagicCode()
    if (magicCode < 0):
        raise Exception('***** YOU NEED TO UPDATE getMyMagicCode()!!!! *****')
    selector = (43**(magicCode + 37)//10**12)
    requiredFns = '  rotateString\n'
    if (selector%2 == 0): requiredFns += '  applyCaesarCipher\n'
    else: requiredFns += '  hasBalancedParentheses\n'
    if ((selector//10)%4 == 0): requiredFns += '  largestNumber\n'
    elif ((selector//10)%4 == 1): requiredFns += '  longestSubpalindrome\n'
    elif ((selector//10)%4 == 2): requiredFns += '  collapseWhitespace\n'
    else: requiredFns += '  topScorer\n'
    if ((selector//100)%2 == 0): requiredFns += '  drawFlagOfQatar'
    else: requiredFns += '  drawFlagOfTheEU'
    return requiredFns

# DO NOT MODIFY THIS FUNCTION!!!!
def testAll():
    # DO NOT MODIFY THIS FUNCTION!!!!
    requiredFns = getRequiredFunctions()
    print('************************************')
    print('Testing these functions:')
    print(requiredFns)
    print('************************************')
    if ('rotateString' in requiredFns):
       testRotateString()
    if ('applyCaesarCipher' in requiredFns):
        testApplyCaesarCipher()
    if ('hasBalancedParentheses' in requiredFns):
        testHasBalancedParentheses()
    if ('largestNumber' in requiredFns):
        testLargestNumber()
    if ('longestSubpalindrome' in requiredFns):
        testLongestSubpalindrome()
    if ('collapseWhitespace' in requiredFns):
        testCollapseWhitespace()
    if ('topScorer' in requiredFns):
        testTopScorer()
    if ('drawFlagOfQatar' in requiredFns):
        testDrawFlagOfQatar()
    if ('drawFlagOfTheEU' in requiredFns):
        testDrawFlagOfTheEU()
    print('*** Done with all tests!')

def main():
    cs112_f19_week3_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
