###############################################################################
# Writing Session 10, Coding Portion: [15 pts]
                                  
# Do not edit these lines:
#   user: 'yoleic@andrew.cmu.edu' (do not edit this!)
#   downloaded at: '2019-11-01 15:38:57' (do not edit this!)
#   downloaded ip: '128.237.157.146' (do not edit this!)
#   security code: '3230222345767869634YSNEMDDCRERGZ1ENY1GGY' (do not edit this!)
                
# Note #1: If you are not in a proctored writing-session lab, close this file
# immediately and email koz@cmu.edu and mdtaylor@andrew.cmu.edu to let
# us know that this occurred.
                
# Note #2: Do not edit this header, only edit the code below the header.
     
# Note #3: Select-all and copy this entire file, all of it, exactly as it
# is here, paste it into your ws10.py starter file, then edit it, and submit
# that edited file to Autolab while you are still in the proctored
# writing-session lab.
         
# Note #4: You will need to download the ws10_linter.py from here:
# http://www.cs.cmu.edu/~112/notes/ws10_linter.py
       
###############################################################################
                    
import ws10_linter
import math, copy
                  
#################################################
# Helper functions
#################################################
               
def almostEqual(d1, d2, epsilon=1e-07):
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
            
# Note: you must use recursion properly to solve all these problems.
# You may not use any interation ('for' or 'while' loops).
        
# Write the function power(base, expt) that takes two integers, base and expt,
# and uses recursion to compute (base**expt).   Note that you may not use
# '**' or 'pow' here.  Also, the base will always be positive, but the expt
# may be positive, negative, or 0.
                               
def power(base, expt):
    if expt == 0:
        return 1
    elif expt < 0:
        return 1.0/power(base, abs(expt))
    else:
        return base*power(base, expt-1)
    
# In the Fibonacci sequence, each element is the sum of the two
# elements before it.  With that in mind, write the recursive function
# fib(n) that computes the nth Fibonacci number, where both fib(0) and fib(1)
# are 1, and fib(2) is 2, and so on.  You must use recursion here,
# and not compute fib(n) any other way.
                    
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
                  
# We are providing you with this implementation of merge(A, B) taken straight
# from the notes.  You do not have to write merge(A, B)!  You can simply
# call this function when you write mergeSort (see below).
               
def merge(A, B):
    # beautiful, but impractical for large N
    if ((len(A) == 0) or (len(B) == 0)):
        return A+B
    else:
        if (A[0] < B[0]):
            return [A[0]] + merge(A[1:], B)
        else:
            return [B[0]] + merge(A, B[1:])
                                  
# Write the function mergeSort(L), that takes a list L and returns a new
# sorted list using recursive mergeSort, as we covered in the notes.
# You should not write merge(A, B), but rather simply call the one
# we provided for you above.
                                
def mergeSort(L):
    if len(L) <2 :
        return L
    else:
        mid = len(L)//2
        left = mergeSort(L[:mid])
        right = mergeSort(L[mid:])
        return merge(left, right)
                                  
#################################################
# Test Functions
#################################################
                              
def testPower():
    print('Testing power()...', end='')
    assert(power(2, 3) == 8)
    assert(power(3, 2) == 9)
    assert(power(3, 1) == 3)
    assert(power(3, 0) == 1)
    assert(almostEqual(power(2, -2), 0.25))
    print('Passed!')
              
def testFib():
    print('Testing fib()...', end='')
    assert(fib(0) == 1)
    assert(fib(1) == 1)
    assert(fib(2) == 2)
    assert(fib(3) == 3)
    assert(fib(4) == 5)
    assert(fib(5) == 8)
    assert(fib(6) == 13)
    print('Passed!')
             
def testMergeSort():
    print('Testing mergeSort()...', end='')
    assert(mergeSort([ ]) == [ ])
    assert(mergeSort([ 1 ]) == [ 1 ])
    assert(mergeSort([ 1, 2 ]) == [ 1, 2 ])
    assert(mergeSort([ 2, 1 ]) == [ 1, 2 ])
    assert(mergeSort([ 5, 3, 4, 1, 2 ]) == [ 1, 2, 3, 4, 5 ])
    print('Passed!')
                                  
#################################################
# testAll and main
#################################################
                                
def testAll():
    testPower()
    testFib()
    testMergeSort()
                                
def main():
    ws10_linter.lint()
    testAll()
                               
if __name__ == '__main__':
    main()