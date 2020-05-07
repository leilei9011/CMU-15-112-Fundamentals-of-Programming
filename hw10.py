#################################################
# hw10.py
#
# Your name: Yo-Lei Chen
# Your andrew id: yoleic
#################################################

import cs112_f19_week10_linter
import math, copy

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

# returns the alternating sum of the list, 
# where every other value is subtracted rather than added
def alternatingSum(L):
    if len(L) == 1: 
    #to proceed we must have 2 elem, 
    # if only one we return the one elem (as int)
        return L[0]
    elif len(L) == 0: 
        return 0
    else:
        return (alternatingSum([L[0]]) - alternatingSum([L[1]]) +
        alternatingSum(L[2:]))

#returns a new list of the same numbers only without their odd digits
def onlyEvenDigits(L): #loop through list
    if len(L)==0:
        return [] 
    else:
        return [onlyEvenDigitsHelper(L[0])] + onlyEvenDigits(L[1:])


def stri(a, b):
    result = 0
    while(result < len(a) and result < len(b)):
        if (a[result] != b[result]):
            result += 1
            print(result)
            return result
        else:
            result += 1
    print(result)
    return result;

def onlyEvenDigitsHelper(num): #loop through digits in elem
    if num == 0:
        return 0
    else:
        n = num%10
        if n%2 == 0: #add even digit to the elem
            return onlyEvenDigitsHelper(num//10)*10 + n
        else: #skip to next num
            return onlyEvenDigitsHelper(num//10)

#returns a list of the positive powers of 3 up to and including n          
def powersOf3ToN(n):
    if n < 1: 
    #1 is 3 to the smallest power (3**0) if n smaller than 1,  
    # no such powers of 3 exist
        return []
    return powersOf3ToNHelper(n, 0)

def powersOf3ToNHelper(n, num): #num keeps track of the power
    if n < 1:
        return []
    else:
        return [3**(num)] + powersOf3ToNHelper(n/3, num+1)

#returns a list of tuples of the values that Binary Search must check to 
# verify whether or not the item is in the list
def binarySearchValues(L, item):
    lo = 0
    hi = len(L)-1
    return binarySearchHelper(L, item, lo, hi) 

#keep track of the lo and hi indexes as they changed
def binarySearchHelper(L, item, lo, hi): 
    mid = (hi+lo)//2
    if lo>hi:
        return [] #return empty lst when item not found in lst
    elif L[mid] == item:
        return [(mid, item)]
    elif L[mid] < item:
        lo = mid+1
        return [(mid, L[mid])]+binarySearchHelper(L, item, lo, hi)
    else:
        hi = mid-1
        return [(mid, L[mid])]+ binarySearchHelper(L, item, lo, hi)

#find second largest num in a list
def secondLargest(L):
    if len(L) == 1 or len(L) == 0:
        return None 
    if L[1] > L[0]:
        maximum = L[1]
        secondMax = L[0]
    else:
        maximum = L[0]
        secondMax = L[1]
    if len(L) == 2:
        return secondMax

    return helper(L[3:], maximum, secondMax)

def helper(L, maximum, secondMax): #check if 1st elem of new lst is second max
    if len(L) == 0:
        return secondMax 
    
    if L[0] > maximum:
        secondMax = maximum
        maximum = L[0]
    return helper(L[1:], maximum, secondMax) #loop through rest of list



#################################################
# Test Functions
#################################################

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(alternatingSum([1,2,3,4,5]) == 1-2+3-4+5)
    assert(alternatingSum([ ]) == 0)
    print('Passed!')

def testSecondLargest():
    print('Testing secondLargest()...', end='')
    assert(secondLargest([1,2,3,4,5]) == 4)
    assert(secondLargest([4,3]) == 3)
    assert(secondLargest([4,4,3]) == 4)
    assert(secondLargest([-3,-4]) == -4)
    assert(secondLargest([4]) == None)
    assert(secondLargest([ ]) == None)
    print('Passed!')

def testOnlyEvenDigits():
    print('Testing onlyEvenDigits()...', end='')
    assert(onlyEvenDigits([43, 23265, 17, 58344]) == [4, 226, 0, 844])
    assert(onlyEvenDigits([ ]) == [ ])
    print('Passed!')

def testPowersOf3ToN():
    print('Testing powersOf3ToN()...', end='')
    assert(powersOf3ToN(10.5) == [1, 3, 9])
    assert(powersOf3ToN(27) == [1, 3, 9, 27])
    assert(powersOf3ToN(26.999) == [1, 3, 9])
    assert(powersOf3ToN(-1) == [ ])
    print('Passed!')

def testBinarySearchValues():
    print('Testing binarySearchValues()...', end='')
    assert(binarySearchValues(['a', 'c', 'f', 'g', 'm', 'q'], 'c') ==
           [(2, 'f'), (0, 'a'), (1, 'c')])
    assert(binarySearchValues(['a', 'c', 'f', 'g', 'm', 'q'], 'n') ==
           [(2, 'f'), (4, 'm'), (5, 'q')])
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testAlternatingSum()
    testOnlyEvenDigits()
    testPowersOf3ToN()
    testBinarySearchValues()
    testSecondLargest()
    stri("abc", "")

def main():
    cs112_f19_week10_linter.lint()
    testAll()

if (__name__ == '__main__'):
    main()
