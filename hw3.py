#################################################
# hw3.py
#
# Your name: Yo-Lei Chen
# Your andrew id: yoleic
#################################################

import cs112_f19_week3_linter
import math
from tkinter import *
import string

#################################################
# quiz prep
#################################################
def mostFrequentLetters(s):
    s = s.lower()
    result = ''
    for c in s:
        num = len(c)



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

#################################################
# patternedMessage
#################################################

"""returns a string produced by replacing the non-whitespace characters 
in the pattern with the non-whitespace characters in the message """
def patternedMessage(msg, pattern):
    newMsg = ''
    msgIndex = 0
    pattern = pattern.strip() #remove leading and trailing new nums
    for i in pattern:
        if i in string.whitespace:
            newMsg += i 
        else:
            while msg[msgIndex] in string.whitespace: #removes spaces in msg
                msgIndex = (msgIndex+1)%len(msg) 
            newMsg += msg[msgIndex]
            msgIndex = (msgIndex+1)%len(msg) 
    return newMsg

#################################################
# encodeRightLeftRouteCipher + decodeRightLeftRouteCipher
#################################################

"""constructs a grid with that number of rows and the minimum number 
of columns required, writing the message in successive columns"""

def encodeRightLeftRouteCipher(text, rows):
    finalText = newText(text, rows) #new text with lower-case letters
    result = str(rows)
    col = len(finalText)//rows
    subStr = ''
    for r in range(0,rows):
        for c in range(0,col):
            index = c*rows+r
            subStr += finalText[index]
        if(r%2 == 0):
            result+=subStr
        else:
            reverse = subStr[::-1]
            result+=reverse
        subStr = ''

    return result

def newText(text, rows):
    start = ord("z")+1 #start from z to a
    while len(text)%rows > 0:
            start -= 1
            newAlphaIndex = (start - ord("a"))%len(string.ascii_lowercase)
            elem = chr(newAlphaIndex + ord("a"))
            text+= elem
    return text

"""reverse
encodeRightLeftRouteCipher(text, rows)"""

def decodeRightLeftRouteCipher(cipher):
    rows = 0
    n = 0 #number of digits of rows
    for c in cipher: #find the number of rows
        if c.isdigit():
            rows = rows*10 +int(c)
            n+=1
        else:
            break

    cipher = cipher[n:] #cut the digits from the cipher
    col = len(cipher)//rows
    result=''

    for c in range(0,col):
        for r in range(0,rows):
            if r%2 == 0:
                result += cipher[col*r + c]
            else:
                result += cipher[col*(r+1)-(c+1)]

    #delete lower-cased letters
    index = len(result)-1
    character = result[index]
    while(character.islower()):
        character = result[index]
        result = result[0:index+1]
        index-=1
            
    return result

#################################################
# drawSimpleTortoiseProgram
#################################################

"""creates a game similar 
to the turtle game"""

def drawSimpleTortoiseProgram(program, canvas, width, height):

    canvas.create_text(10, 0, anchor = "nw", text = program, font = 10, 
    fill = "grey") 
    
    x0 = width/2
    y0 = height/2
    x1, y1 = x0, y0
    degree = 0
    distance = 0
    color = "none"

    for lines in program.splitlines():
        if lines in string.whitespace:
            continue
        else:
            if lines.find("#") != -1: 
                if lines.startswith("#"): #delete comments
                    continue
                else:
                    index = lines.index("#") #delete comments after commands
                    lines = lines[:index-1]

            spaceIndex = lines.index(" ")
            command = lines[:spaceIndex] 
            commandDetail = lines[spaceIndex+1:] 

            if command == "move":
                distance = int(commandDetail)
                radian = math.radians(degree)
                x1,y1=x0+math.cos(radian)*distance,y0-math.sin(radian)*distance
                
                if color == "none":
                    pass
                else:
                    canvas.create_line(x0, y0, x1, y1, fill = color, width=4)
                x0, y0 = x1, y1

            elif command == "color":
                color = commandDetail

            elif command == "right":
                degree -= int(commandDetail)

            elif command == "left":
                degree += int(commandDetail)    

        
#################################################
# drawNiceRobot
#################################################

def drawNiceRobot(canvas, width, height):
    drawBody(canvas, width, height)
    drawHead(canvas, width, height)
    drawHands(canvas, width, height)
    drawLegs(canvas, width, height)
    

def drawHead(canvas, width, height):
    x0, y0 = width/5*2, height/10
    x1, y1 = width-x0, height/3  #coordinates for head
    headHeight = y1-y0
    headWidth = x1-x0

    canvas.create_oval(x0,y0,x1,y1,fill="light blue" ) #big head
    canvas.create_rectangle(x0,y1-(headHeight/5),x1, y1, fill = "grey") #neck
    canvas.create_oval(x0+headWidth/6,y0+headHeight/3, 
    x0+headWidth/2,y1-headHeight/3,fill="black", outline = "white", width = 6 )
    #left eyes
    canvas.create_oval(x1-headWidth/2,y0+headHeight/3,
    x1-headWidth/6,y1-headHeight/3,fill="black", outline = "white", width =6 )
    #right eyes

def drawHands(canvas, width, height):
    bodyWStart = width/3
    bodyHStart = height/3
    bodyWEnd = width-bodyWStart
    bodyHEnd = height-bodyHStart

    canvas.create_line(bodyWStart, height/2, width/6, height/2, width/6,
    bodyHStart,fill = "grey", smooth = 1, width = width/30) #left arms
    canvas.create_line(bodyWEnd, height/2, width - width/6, 
    height/2,width - width/6,height/3 ,fill = "grey", smooth = 1, 
    width = width/30) #right arm
    canvas.create_text(width/6, height/3, 
    text= "Quiz!\nHomework!\nWritting Session!\nStress!", width=width/5, 
    fill="black")
    canvas.create_text(width-width/6, height/3, 
    text= "Quiz!\nHomework!\nWritting Session!\nStress!", width=width/5, 
    fill="black")

def drawLegs(canvas, width, height):
    bodyWStart = width/3
    bodyHStart = height/3
    bodyWEnd = width-bodyWStart
    bodyHEnd = height-bodyHStart
    bodyWidth = bodyWEnd - bodyWStart

    x0, y0 = bodyWStart+bodyWidth/10, bodyHEnd
    x1, y1 = width/2, height - height/10
    x2, y2 = bodyWEnd-bodyWidth/10,  bodyHEnd
    canvas.create_polygon(x0, y0, x1, y1, x2, y2, outline = "black", 
    fill = "grey")

    a0, b0 = bodyWStart+bodyWidth/10, height - height/8
    a1, b1 = bodyWEnd-bodyWidth/10, height - height/8
    a2, b2 = width/3, height - height/25
    a3, b3 = bodyWEnd, height - height/25
    canvas.create_polygon(a0, b0, a1, b1, a2, b2, a3, b3, fill = "light blue", 
    smooth = 1)

def drawBody(canvas, width, height):
    bodyWStart = width/3
    bodyHStart = height/3
    bodyWEnd = width-bodyWStart
    bodyHEnd = height-bodyHStart
    bodyWidth = bodyWEnd - bodyWStart
    bodyHeight = bodyHEnd - bodyWStart

    canvas.create_rectangle(bodyWStart, bodyHStart,bodyWEnd, bodyHEnd,
    fill = "light blue")
    canvas.create_rectangle(bodyWStart+bodyWidth/10, bodyHStart+ bodyHeight/10,
    bodyWEnd-bodyWidth/10, bodyHStart +bodyHeight/3,
    fill = "light yellow")
    canvas.create_text(bodyWStart+bodyWidth/2, bodyHStart+ bodyHeight/5,
    fill="darkBlue",text = "15112", font="Times 28 bold italic")


#################################################
# bonus/optional getEvalSteps
#################################################

def getEvalSteps(expr):
    return 42

#################################################
# bonus/optional topLevelFunctionNames
#################################################

def topLevelFunctionNames(code):
    return 42

#################################################
# Test Functions
#################################################

def testPatternedMessage():
    print("Testing patternedMessage()...", end="")
    assert(patternedMessage("abc def",   "***** ***** ****")   ==
           "abcde fabcd efab")
    assert(patternedMessage("abc def", "\n***** ***** ****\n") == 
           "abcde fabcd efab")
    parms = [
    ("Go Pirates!!!", """
***************
******   ******
***************
"""),
    ("Three Diamonds!","""
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""),
    ("Go Steelers!","""
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
""")]
    solns = [
"""
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
,
"""
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
"""
,
"""
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
"""
    ]
    parms = [("A-C D?", """
*** *** ***
** ** ** **
"""),
    ("A", "x y z"),
    ("The pattern is empty!", "")
    ]
    solns = [
"""
A-C D?A -CD
?A -C D? A-
""",
"A A A",
""
    ]
    for i in range(len(parms)):
        (msg,pattern) = parms[i]
        soln = solns[i]
        soln = soln.strip("\n")
        observed = patternedMessage(msg, pattern)
        #observed = patternedMessage(msg, pattern).strip("\n")
        #print "\n\n***********************\n\n"
        #print msg, pattern
        #print "<"+patternedMessage(msg, pattern)+">"
        #print "<"+soln+">"
        assert(observed == soln)
    print("Passed!")

def testEncodeRightLeftRouteCipher():
    print('Testing encodeRightLeftRouteCipher()...', end='')
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",4) ==
                                      "4WTAWNTAEACDzyAKT")
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",3) ==
                                      "3WTCTWNDKTEAAAAz") 
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",5) ==
                                      "5WADACEAKWNATTTz") 
    print('Passed!')

def testDecodeRightLeftRouteCipher():
    print('Testing decodeRightLeftRouteCipher()...', end='')
    assert(decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT") ==
                                      "WEATTACKATDAWN")
    assert(decodeRightLeftRouteCipher("3WTCTWNDKTEAAAAz") ==
                                      "WEATTACKATDAWN") 
    assert(decodeRightLeftRouteCipher("5WADACEAKWNATTTz") ==
                                      "WEATTACKATDAWN") 
    text = "WEATTACKATDAWN"
    cipher = encodeRightLeftRouteCipher(text, 6)
    plaintext = decodeRightLeftRouteCipher(cipher)
    assert(plaintext == text)
    print('Passed!')

def runDrawNiceRobot(width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawNiceRobot(canvas, width, height)
    root.mainloop()
    print("bye!")

def runDrawSimpleTortoiseProgram(program, width, height):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawSimpleTortoiseProgram(program, canvas, width, height)
    root.mainloop()
    print("bye!")

def testDrawSimpleTortoiseProgram():
    print("Testing drawSimpleTortoiseProgram()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    runDrawSimpleTortoiseProgram("""
# This is a simple tortoise program
color blue
move 50

left 90

color red
move 100

color none # turns off drawing
move 50

right 45

color green # drawing is on again
move 50

right 45

color orange
move 50

right 90

color purple
move 100
""", 300, 400)

    runDrawSimpleTortoiseProgram("""
# Y
color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none # space
right 45
move 25

# E
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  # space
color none
move 25

# S
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
right 90
move 42
right 90
move 50
""", 500, 500)
    print("Done!")

def testDrawNiceRobot():
    print('Calling runDrawRobot(400, 400):')
    runDrawNiceRobot(400, 400)
    print('Calling runDrawRobot(800, 800):')
    runDrawNiceRobot(800, 800)

def testBonusTopLevelFunctionNames():
    print("Testing topLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assert(topLevelFunctionNames(code) == "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert(topLevelFunctionNames(code) == "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assert(topLevelFunctionNames(code) == "f.g")

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.h.j")
    print("Passed!")

def testBonusGetEvalSteps():
    print("Testing getEvalSteps()...", end="")
    assert(getEvalSteps("0") == "0 = 0")
    assert(getEvalSteps("2") == "2 = 2")
    assert(getEvalSteps("3+2") == "3+2 = 5")
    assert(getEvalSteps("3-2") == "3-2 = 1")
    assert(getEvalSteps("3**2") == "3**2 = 9")
    assert(getEvalSteps("31%16") == "31%16 = 15")
    assert(getEvalSteps("31*16") == "31*16 = 496")
    assert(getEvalSteps("32//16") == "32//16 = 2")
    assert(getEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(getEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(getEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(getEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    #testPatternedMessage()
    #testEncodeRightLeftRouteCipher()
    #testDecodeRightLeftRouteCipher()
    testDrawSimpleTortoiseProgram()
    #testDrawNiceRobot()
    #testBonusTopLevelFunctionNames()
    #testBonusGetEvalSteps()

def main():
    cs112_f19_week3_linter.lint()
    testAll()

if __name__ == '__main__':
    main()


