#################################################
# hw8.py
#
# Your name: Yo-Lei Chen
# Your andrew id: yoleic
#################################################

import cs112_f19_week8_linter
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
"""
# 1A: switch the first and last element on a list
def slow1(lst): # N is the length of the list lst
    assert(len(lst) >= 2)
    a = lst.pop()    # O(1)
    b = lst.pop(0)   # O(N)
    lst.insert(0, a) # O(N)
    lst.append(b)    # O(1)
# 1B: Big-O: O(N)
"""
# 1C:
def fast1(lst):
    assert(len(lst) >= 2)
    temp1 = lst[0]     # O(1)
    temp2 = lst.pop()  # O(1)
    lst[0] = temp2     # O(1)
    lst.append(temp1)  # O(1)
    return lst

# 1D: Big-O: O(1)

"""
# 2A: count the number of elements in a list that never appeared before
def slow2(lst): # N is the length of the list lst
    counter = 0                   # O(1)
    for i in range(len(lst)):     # N Loops
        if lst[i] not in lst[:i]: # O(N)
            counter += 1          # O(1)
    return counter                # O(1)
# 2B: O(N**2)
"""
# 2C:
def fast2(lst):
    s = set(lst)                    # O(N)
    return len(s)                   # O(1)

# 2D:Big-O: O(N)

"""
# 3A: return the lower-cased letters that appeared the most 
in a string , if there are an equal amount of lower cased letters, 
the function returns the smallest lower-cased among those 

def slow3(s): # N is the length of the string s
    maxLetter = ""                              # O(1)
    maxCount = 0                                # O(1)
    for c in s:                                 # N Loops
        for letter in string.ascii_lowercase:   # K Loops or 26 Loops
            if c == letter:                     # O(1)
                if s.count(c) > maxCount or \
                   s.count(c) == maxCount and \
                   c < maxLetter:               # O(N)
                    maxCount = s.count(c)       # O(N)
                    maxLetter = c               # O(1)
    return maxLetter                            # O(1)
# 3B: Big-O: O(N**2)
"""
# 3C:
def fast3(s):
    maxLetter = ""                                                     # O(1)
    maxCount = -1                                                       # O(1)
    for letter in string.ascii_lowercase:                              # K Loops
        count = s.count(letter)                                        # O(N)
        if count > maxCount or (count == maxCount and letter 
        > maxLetter):                                                  # O(1)
            maxCount = count                                           # O(1)
            maxLetter = letter                                         # O(1)
    if maxCount == 0:                                                  # O(1)
        return ""                                                      # O(1)
    return maxLetter                                                   # O(1)

# 3D: Big-O: O(N)

"""
# 4A: find the largest difference between two numbers, each number 
is from a different list (a or b) 

def slow4(a, b): # a and b are lists with the same length N
    assert(len(a) == len(b))
    result = abs(a[0] - b[0])    # O(1)
    for c in a:                  # N Loops
        for d in b:              # N Loops
            delta = abs(c - d)   # O(1)
            if (delta > result): # O(1)
                result = delta   # O(1)
    return result                # O(1)
# 4B: Big-O: O(N**2)
"""
# 4C: 
def fast4(a, b):
    maxA, maxB = max(a), max(b)
    minA, minB = min(a), min(b)
    max1, max2 = maxA - minB, maxB - minA   # O(N)
    return max(max1, max2) # O(1)

# 4D: Big-O: O(N)

#################################################
# Autograde Section
#################################################

"""
find pair of num in a list that add up to a target num
"""
def getPairSum(lst, target):

    if len(lst)<2: 
        return None
    #O(1)

    s = set(lst)
    b = dict()
    size = len(lst)
    #O(1)

    for elem in lst:
       diff = target - elem
       key, value = diff, elem
       b[key] = value
    #O(N)
    
    for elem in lst:
        targetDiff = b.get(elem,'') #return str
        if targetDiff != '':
            if elem == int(targetDiff): 
                #to prevent situations where elem + elem = target
                if len(lst) == len(s): #check if there are duplicates of num
                    return None
            return (elem, int(targetDiff))
    #O(N)

    return None
    #O(1)

    #Big-Oh: O(N)

def getpairSum2(lst, target):
    d = dict()

    for elem in lst:
        d[elem] = d.get(elem, 0) + 1
    
    for elem in lst:
        diff = target - elem
        if diff in d:
            if diff == elem:
                if d[elem] > 1:
                    return [diff, elem]
                else:
                    return [diff, elem]
    return []

"""
if there are 3 values in the list taht form a Pythagorean Triple
"""
def containsPythagoreanTriple(lst):
    L = [x**2 for x in lst] #O(N)
    result = False #O(1)


    for elem in lst:  #loop N times
        target = elem**2
        t = getPairSum(L,target) #O(N)
        # find if there are 2 num (a**2 + b**2) = target
        if t != None:
            result = True
    #O(N**2)

    return result

"""
function returns a dictionary mapping each movie 
to the number of the awards that it won
"""
def movieAwards(oscarResults):
    d = dict()

    for award, movie in oscarResults: 
        if movie in d:
            d[movie] += 1  #add one more award
        else:
            d[movie] = 1 #movie not in dict, start w/ one award
    return d

"""
returns a new dictionary mapping all the same people 
to sets of their friends-of-friends.
"""
def friendsOfFriends(d):
    result = dict()

    for person in d:
        if person not in result:
            result[person] = set()
        for friend in d[person]: #loop thru the friends of friends
            for fof in d[friend]:      
                #avoid repeats and friends and the person him/herself
                if fof not in d[person] and fof != person:  
                    result[person].add(fof)
    return result

#################################################
# Test Functions
#################################################

def testFast1():
    A = [1,2,3,4]
    assert(fast1(A) == [4,2,3,1])
    B = [0, 1]
    assert(fast1(B) == [1, 0])
    print("testFast1()...Passed!")
    
def testFast2():
    A = [1,2,1,2,3]
    assert(fast2(A) == 3)
    B = []
    assert(fast2(B) == 0)
    C = [1,1,1]
    assert(fast2(C) == 1)
    print("testFast2()...Passed!")

def testFast3():
    a = 'aaaaa123bb456ccc'
    assert(fast3(a)== 'a')
    b = 'aabbcc'
    assert(fast3(b)== 'c')
    c = '1234'
    assert(fast3(c)== "")
    print("testFast3()...Passed!")
    
def testFast4():
    A = [1,2,3,4]
    B = [1,2,3,4]
    assert(fast4(A, B) == 3)
    C = [7,8,-36]
    D = [-1,-2]
    assert(fast4(C, D) == 35)
    print("testFast4()...Passed!")

def testGetPairSum():
    assert(getPairSum([1], 1) == None)
    assert(getPairSum([5, 2], 7) in [ (5, 2), (2, 5) ])
    assert(getPairSum([10, -1, 1, -8, 3, 1], 2) in [ (10, -8), (-8, 10), (-1, 3)
    , (3, -1), (1, 1) ])
    assert(getPairSum([1, 2], 4) == None)
    assert(getPairSum([10, -1, 1, -8, 3, 1], 10) == None)
    print("testGetPairSum()...Passed!")

def testContainsPythagoreanTriple():
    assert(containsPythagoreanTriple([1, 3, 6, 2, 5, 1, 4]) == True)
    assert(containsPythagoreanTriple([2,2,2]) == False)
    print("testContainsPythagoreanTriple()...Passed!")

def testMovieAwards():
    L =   { 
    ("Best Picture", "Green Book"), 
    ("Best Actor", "Bohemian Rhapsody"),
    ("Best Actress", "The Favourite"),
    ("Film Editing", "Bohemian Rhapsody"),
    ("Best Original Score", "Black Panther"),
    ("Costume Design", "Black Panther"),
    ("Sound Editing", "Bohemian Rhapsody"),
    ("Best Director", "Roma")
    }
    M =   { 
    "Black Panther" : 2,
    "Bohemian Rhapsody" : 3,
    "The Favourite" : 1,
    "Green Book" : 1,
    "Roma" : 1
    }
    assert(movieAwards(L) == M)
    print("testMovieAwards()...Passed!")

def testFriendsOfFriends():
    d = { }
    d["jon"] = set(["arya", "tyrion"])
    d["tyrion"] = set(["jon", "jaime", "pod"])
    d["arya"] = set(["jon"])
    d["jaime"] = set(["tyrion", "brienne"])
    d["brienne"] = set(["jaime", "pod"])
    d["pod"] = set(["tyrion", "brienne", "jaime"])
    d["ramsay"] = set()
    
    L = {
    'tyrion': {'arya', 'brienne'}, 
    'pod': {'jon'}, 
    'brienne': {'tyrion'}, 
    'arya': {'tyrion'}, 
    'jon': {'pod', 'jaime'}, 
    'jaime': {'pod', 'jon'}, 
    'ramsay': set()
    }
    assert(friendsOfFriends(d)==L)
    print("testFriendsOfFriends()...Passed!")


#################################################
# testAll and main
#################################################

def testAll():
    testFast1()
    testFast2()
    testFast3()
    testFast4()
    testGetPairSum()
    testContainsPythagoreanTriple()
    testMovieAwards()
    testFriendsOfFriends()

def main():
    cs112_f19_week8_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
