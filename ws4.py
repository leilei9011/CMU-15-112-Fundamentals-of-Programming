#################################################
# writing_session4.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_f19_week4_linter
import math, copy

#################################################
# Replace -1 with your code from the sheet of paper
# your TA gave you and that you just signed!!!!
#################################################

def getMyMagicCode():
    myMagicCode = 108   # <-- Replace this value here
    return myMagicCode

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

def smallestDifference(L):
    return 42

def multiplyPolynomials(p1, p2):
    result = [0 for x in range(len(p1)-1 + len(p2)-1 +1)]
    for i1 in range(len(p1)):
        for i2 in range(len(p2)):
            coeff = p1[i1] * p2[i2]
            newIndex = i1 + i2
            result[newIndex] += coeff
    return result

def lookAndSay(L):
    result = []
    if len(L) == 0:
        return result
    prev = L[0]
    num = 0
    for elem in L:
        if elem == prev:
            num += 1
        else:
            result += [(num, prev)]
            num = 1
            prev = elem
    if num != 0:
        result += [(num, prev)]
    return result

def inverseLookAndSay(L):
    result = []
    for elem in L:
        for x in range(elem[0]):
            result += [elem[1]]
    return result

def nondestructiveRemoveRepeats(L):
    result = []
    for elem in L:
        if elem not in result:
            result += [elem]
    return result

def destructiveRemoveRepeats(L):
    i = len(L)-1
    while(containsRepeats(L)):
        elem = L[i]
        if L.count(elem) >1:
            L.pop(i)
        i -= 1
def containsRepeats(L):
    for elem in L:
        if L.count(elem) >1:
            return True
    return False

#################################################
# Test Functions
#################################################

def testSmallestDifference():
    print('Testing smallestDifference()...', end='')
    assert(smallestDifference([]) == -1)
    assert(smallestDifference([2,3,5,9,9]) == 0)
    assert(smallestDifference([-2,-5,7,15]) == 3)
    assert(smallestDifference([19,2,83,6,27]) == 4)
    assert(smallestDifference(list(range(0, 10**3, 5)) + [42]) == 2)
    print('Passed')

def testMultiplyPolynomials():
    print("Testing multiplyPolynomials()...", end="")
    # (2)*(3) == 6
    assert(multiplyPolynomials([2], [3]) == [6])
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    assert(multiplyPolynomials([2,-4],[3,5]) == [6,-2,-20])
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    assert(multiplyPolynomials([2,0,-4],[3,0,2,0]) == [6,0,-8,0,-8,0])
    print("Passed!")

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = a + [ ] # copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = a + [ ] # copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def _verifyNondestructiveRemoveRepeatsIsNondestructive():
    a = [3, 5, 3, 3, 6]
    b = a + [ ] # copy.copy(a)
    # ignore result, just checking for destructiveness here
    nondestructiveRemoveRepeats(a)
    return (a == b)

def testNondestructiveRemoveRepeats():
    print("Testing nondestructiveRemoveRepeats()", end="")
    assert(_verifyNondestructiveRemoveRepeatsIsNondestructive())
    assert(nondestructiveRemoveRepeats([1,3,5,3,3,2,1,7,5]) == [1,3,5,2,7])
    assert(nondestructiveRemoveRepeats([1,2,3,-2]) == [1,2,3,-2])
    print("Passed.")

def testDestructiveRemoveRepeats():
    print("Testing destructiveRemoveRepeats()", end="")
    a = [1,3,5,3,3,2,1,7,5]
    assert(destructiveRemoveRepeats(a) == None)
    assert(a == [1,3,5,2,7])
    b = [1,2,3,-2]
    assert(destructiveRemoveRepeats(b) == None)
    assert(b == [1,2,3,-2])
    print("Passed.")

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
    requiredFns = ''
    if (selector%2 == 0): requiredFns += '  smallestDifference\n'
    else: requiredFns += '  multiplyPolynomials\n'
    requiredFns += '  lookAndSay\n  inverseLookAndSay\n'
    requiredFns += '  nondestructiveRemoveRepeats\n  destructiveRemoveRepeats'
    return requiredFns

# DO NOT MODIFY THIS FUNCTION!!!!
def testAll():
    # DO NOT MODIFY THIS FUNCTION!!!!
    requiredFns = getRequiredFunctions()
    print('************************************')
    print('Testing these functions:')
    print(requiredFns)
    print('************************************')
    if ('smallestDifference' in requiredFns):
        testSmallestDifference()
    if ('multiplyPolynomials' in requiredFns):
        testMultiplyPolynomials()
    if ('lookAndSay' in requiredFns):
        testLookAndSay()
    if ('inverseLookAndSay' in requiredFns):
        testInverseLookAndSay()
    if ('nondestructiveRemoveRepeats' in requiredFns):
        testNondestructiveRemoveRepeats()
    if ('destructiveRemoveRepeats' in requiredFns):
        testDestructiveRemoveRepeats()
    print('*** Done with all tests!')

def main():
    cs112_f19_week4_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
