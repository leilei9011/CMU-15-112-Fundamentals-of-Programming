#################################################
# hw4.py
#
# Your name: Yo-Lei Chen
# Your andrew id: yoleic
#################################################

import cs112_f19_week4_linter
import math, copy
import string

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
# bestScrabbleScore
#################################################

def bestScrabbleScore(dictionary, letterScores, hand):
    highestPoints = 0
    highestWord = list()
    currentPoints = 0
    result = list()

    for i in range(len(dictionary)):
        index = 0
        if isLegal(dictionary[i], hand):
            for c in dictionary[i]:
                currentPoints += letterScores[(ord(c)-ord("a"))%
                len(string.ascii_lowercase)]
        else:
            currentPoints += 0
        if currentPoints > highestPoints:
            highestPoints = currentPoints
            highestWord = dictionary[i]
        elif currentPoints == highestPoints:
            if type(highestWord) == str:
                highestWord = [highestWord] + [dictionary[i]]
            else:
                highestWord.append(dictionary[i])
        else:
            pass
        currentPoints = 0
        
    if  highestPoints == 0: 
        return None
    
    result = (highestWord, highestPoints)

    return result

def isLegal(word, hand):
    newHand = copy.copy(hand)
    for c in range(len(word)):
        x = word[c]
        if x in newHand:
            newHand.pop(newHand.index(x))
        else: 
            return False
    return True


#################################################
# Person class
#################################################

class Person(object):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []
        
    def getName(self):
        return self.name

    def getAge(self):
        return self.age
    
    def getFriends(self):
        if self.friends == None:
            return self.friends
        if len(self.friends) == 0:
            self.friends =  None
        return self.friends
    
    def addFriend(self, Person):
        if self.friends == None:
            self.friends = []
        if containsRepeats(self.friends, Person) or self == Person:
            pass
        else:
            self.friends.append(Person)

def containsRepeats(L, Person):
    if Person in L:
        return True
    return False

#################################################
# playMyTextAdventureGame
#################################################
"""
1. family room

2. the method getDirection returns an index when it detects that the parameter 
consists certain keyword

3. the player cannot add/remove items to the room ; we will get an Attribute 
Error

4. By using the string join methods, the method getAvailableDirNames is saying 
that all directions are available, the player can go to any of the given 
directions

5. an item's name is the full name of the item that shows the player what's 
in the room/what the player is carrying. A short name is the name the player 
used to enter his/her command. 

6. game.inventory is a list of items the player is carrying

7. the method uses the string split method to split the input and read them and
put them into two variables: command and target

8. We use game.findItem to if the target (which is written in a short name) 
given from the user input is inside the room/in the itemList (by converting 
the available items from its full name into its short name) . If it does, 
the method would return the full name of the item to finish the method for 
the command. Otherwise, it would return None, and the method for 
the command would print a line telling the player that they unable to 
do that command because those items do not exist inside the room

9. It is enforced by game.doGet by checking if the length of the list of 
items the player is carrying (len(self.inventory)) is bigger than 2. If so, no
items can be removed rom the room or add to the inventory. 

9. if the player gave a command to pour water, the game.doPour method would 
include the word 'full' in glass.name. The method game.doDrink would then check 
if the word 'full'is inside glass.name before drinking it. 
"""
class Room(object):

    def __init__(self, name):
        self.name = name
        self.exits = [None] * 8 # north, south, east, west, ns , ne , se, sw
        self.items = []

    def getDirection(self, dirName):
        dirName = dirName.lower()
        if (dirName in ['n', 'north']): return 0
        elif (dirName in ['s', 'south']): return 1
        elif (dirName in ['e', 'east']): return 2
        elif (dirName in ['w', 'west']): return 3
        elif (dirName in ['ne', 'north east']): return 4
        elif (dirName in ['nw', 'north west']): return 5
        elif (dirName in ['se', 'south east']): return 6
        elif (dirName in ['sw', 'south west']): return 7
        else:
            print(f'Sorry, I do not recognize the direction {dirName}')
            return None

    def setExit(self, dirName, room):
        direction = self.getDirection(dirName)
        self.exits[direction] = room

    def getExit(self, dirName):
        direction = self.getDirection(dirName)
        if (direction == None):
            return None
        else:
            return self.exits[direction]

    def getAvailableDirNames(self):
        availableDirections = [ ]
        for dirName in ['North', 'South', 'East', 'West', 'South East', 
        'South West', 'North East', 'North West']:
            if (self.getExit(dirName) != None):
                availableDirections.append(dirName)
        if (availableDirections == [ ]):
            return 'None'
        else:
            return ', '.join(availableDirections)

class Item(object):
    def __init__(self, name, shortName):
        self.name = name
        self.shortName = shortName

class Game(object):
    def __init__(self, name, goal, startingRoom, startingInventory):
        self.name = name
        self.goal = goal
        self.room = startingRoom
        self.commandCounter = 0
        self.inventory = startingInventory
        self.gameOver = False

    def getCommand(self):
        self.commandCounter += 1
        response = input(f'[{self.commandCounter}] Your command --> ')
        print()
        if (response == ''): 
            response = 'help me'
        index = response.find(' ')
        responseParts = response
        command = responseParts[:index]
        target = responseParts[index+1:]
        return command, target

    def play(self):
        print(f'Welcome to {self.name}!')
        print(f'Your goal: {self.goal}!')
        print('Just press enter for help.')
        while (not self.gameOver):
            self.doLook()
            command, target = self.getCommand()
            if (command == 'help'): self.doHelp()
            elif (command == 'look'): self.doLook()
            elif (command == 'go'): self.doGo(target)
            elif (command == 'take'): self.doTake(target)
            elif (command == 'hug'): self.doHug(target)
            elif (command == 'quit'): break
            elif(command == 'superhelp'): self.superPlay()
            else: print("""Unknown command: {command}. 
            Enter "help mequi" for help.""")
        print('Goodbye!')

    def doHelp(self):
        print('''
Welcome to this fine game!  Here are some commands I know:
    help me (print this message)
    look (see what's around you)
    go north, go south, go east, go west, go northeast, go southeast, 
    go nortwest, go southwest (or just 'go n/s/e/w/ne/nw/se/sw')
    take quiz/writing session
    hug Taylor
    quit game
Have fun!''')


    def printItems(self, items):
        if (len(items) == 0):
            print('Nothing.')
        else:
            itemNames = [item.name for item in items]
            print(', '.join(itemNames))

    def findItem(self, targetItemName, itemList):
        for item in itemList:
            if (item.shortName == targetItemName):
                return item
        return None

    def doLook(self):
        print(f'\nI am in {self.room.name}')
        print(f'I can go these directions: {self.room.getAvailableDirNames()}')
        print('I can see these things: ', end='')
        self.printItems(self.room.items)
        print('Things I have not finished: ', end='')
        self.printItems(self.inventory)
        print()

    def doGo(self, dirName):
        newRoom = self.room.getExit(dirName)
        if (newRoom == None):
            print(f'Sorry, I cannot go in that direction.')
        else:
            self.room = newRoom

    def doTake(self, itemName):
        item = self.findItem(itemName, self.inventory)
        if (item == None):
            print('Sorry, but I do not need to do that.')

        else:
            if (itemName == 'quiz'):
                if(self.room.name == 'Doherty Hall'):
                    self.inventory.remove(item)
                else:
                    print("you can only take your quiz in the classroom")
            elif (itemName == 'writing session'):
                print(self.room.name == 'Gates Hillman Center')
                if(self.room.name == 'Gates Hillman Center'):
                    self.inventory.remove(item)
                    print("""
                    Testing multiplyPolynomials()...Passed!
                    Testing multiplyPolynomials()...Passed!
                    Testing lookAndSay()...Passed!
                    Testing inverseLookAndSay()...Passed!
                    Testing nondestructiveRemoveRepeats()Passed.
                    Testing destructiveRemoveRepeats()Passed.
                    *** Done with all tests!
                    """
                    )
                else:
                    print(""" you can only take your quiz in your recitation 
                    classroom
                    """)
            else:
                print("Sorry, but you are incapable of taking this.")

    def doHug(self, itemName):
        
        if (itemName != 'Taylor'):
            print('I only want to hug Taylor!')
        if (self.room.name == 'The CFA Lawn'):
            print('''Oops! I hugged the wrong person. Turns out this guy
            is actually Kosbie. Where is Taylor? ''')
        elif (len(self.inventory) != 0):
            print("""
            Taylor says you can't hug him unless you finished all your work :(
            """
            )
        else:
            print('You did it! You hugged Taylor!')
    
    def superPlay(self):

        print("""
        go nw
        take writing session
        go s
        take quiz
        go s
        hug Taylor
        (there are also a trap on the cfa lawn)
        """)

def playMyTextAdventureGame():
    # Make the Rooms
    doherty = Room('Doherty Hall')
    wean = Room('Wean Hall')
    gates = Room('Gates Hillman Center')
    mall = Room('The Mall')
    cut = Room('The Cut')
    cfalawn = Room('The CFA Lawn')

    # Make the map (note: it need not be physically possible)
    doherty.setExit('North East', cut)
    doherty.setExit('South', mall)
    gates.setExit('South', doherty)
    gates.setExit('South East', cut)
    cfalawn.setExit('North', cut)
    cfalawn.setExit('East', mall)
    mall.setExit('West', cfalawn)
    cut.setExit('South', cfalawn)
    mall.setExit('North', doherty)
    cut.setExit('North West', gates)
    cut.setExit('South West', doherty)

    # Make some items 
    quiz = Item('quiz', 'quiz')
    quiz2 = Item('students panicking + quiz', 'quiz')
    doherty.items.append(quiz2)
    ws = Item('writing session', 'writing session')
    ws2 = Item('blue hoodies army + writing session', 'writing session')
    gates.items.append(ws2)
    taylor = Item('Taylor taking a nap in the grass', 'Taylor?')
    mall.items.append(taylor)
    taylor2 = Item('Taylor', 'Taylor?')
    cfalawn.items.append(taylor2)
    
    # Make the game and play it
    game = Game('This Simple Example Game',
                'Hug Taylor',
                cut,
                [quiz, ws])
    game.play()

    playMyTextAdventureGame()


#################################################
# bonus: linearRegression
#################################################

def linearRegression(pointsList):
    return 42

#################################################
# bonus: runSimpleProgram
#################################################

def runSimpleProgram(program, args):
    return 42
def dictionary1(): return ["a", "b", "c"]
def letterScores1(): return [1] * 26
def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
def letterScores2(): return [1+(i%5) for i in range(26)]

#################################################
# Test Functions
#################################################

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")

def testPersonClass():
    print('Testing Person Class...', end='')
    fred = Person('fred', 32)
    assert(isinstance(fred, Person))
    assert(fred.getName() == 'fred')
    assert(fred.getAge() == 32)
    assert(fred.getFriends() == None)

    wilma = Person('wilma', 35)
    assert(wilma.getName() == 'wilma')
    assert(wilma.getAge() == 35)
    assert(wilma.getFriends() == None)

    wilma.addFriend(fred)
    assert(wilma.getFriends() == [fred])
    assert(fred.getFriends() == None)
    wilma.addFriend(fred)
    assert(wilma.getFriends() == [fred]) # don't add twice!

    barney = Person('barney', 28)
    fred.addFriend(wilma)
    fred.addFriend(barney)
    assert(fred.getFriends() == [wilma, barney])
 
    fred.addFriend(barney)  # don't add twice
    fred.addFriend(fred)    # ignore self as a friend
    assert(fred.getFriends() == [wilma, barney])
    print('Passed!')

def testPlayMyTextAdventureGame():
    print('***************************************************')
    print('Testing playMyTextAdventureGame()...')
    print('This requires manual testing, so we will just run the game:')
    print('***************************************************')
    playMyTextAdventureGame()
    print('***************************************************')

def relaxedAlmostEqual(d1, d2):
    epsilon = 10**-3 # really loose here
    return abs(d1 - d2) < epsilon

def tuplesAlmostEqual(t1, t2):
    if (len(t1) != len(t2)): return False
    for i in range(len(t1)):
        if (not relaxedAlmostEqual(t1[i], t2[i])):
            return False
    return True

def testBonusLinearRegression():
    print("Testing bonus problem linearRegression()...", end="")

    ans = linearRegression([(1,3), (2,5), (4,8)])
    target = (1.6429, 1.5, .9972)
    assert(tuplesAlmostEqual(ans, target))
    
    ans = linearRegression([(0,0), (1,2), (3,4)])
    target = ((9.0/7), (2.0/7), .9819805061)
    assert(tuplesAlmostEqual(ans, target))

    #perfect lines
    ans = linearRegression([(1,1), (2,2), (3,3)])
    target = (1.0, 0.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))
    
    ans = linearRegression([(0,1), (-1, -1)])
    target = (2.0, 1.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))

    #horizontal lines
    ans = linearRegression([(1,0), (2,0), (3,0)])
    target = (0.0, 0.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))

    ans = linearRegression([(1,1), (2,1), (-1,1)])
    target = (0.0, 1.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))
    print("Passed!")

def testBonusRunSimpleProgram():
    print("Testing bonus problem runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testBestScrabbleScore()
    testPersonClass()
    #testPlayMyTextAdventureGame()
    #testBonusLinearRegression()
    #testBonusRunSimpleProgram()

def main():
    cs112_f19_week4_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
