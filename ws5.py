#################################################
# writing_session5.py
#
# Your name: Yo-Lei Chen
# Your andrew id: yoleic
#################################################

import cs112_f19_week5_linter
import math, copy

#################################################
# Replace -1 with your code from the sheet of paper
# your TA gave you and that you just signed!!!!
#################################################

def getMyMagicCode():
    myMagicCode = 452   # <-- Replace this value here
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

def a(s):
    print("a:", s)
    s = s[1:-1]
    b(s)
    print(s)
def b(s):
    print("b:", s)
    s = s + s
    return s
def c(s):
    print("c:", s)
    t = ""
    for x in s:
        if x not in t:
            t += x
    return t

def nondestructiveRemoveRowAndCol(A, row, col):
    result = [[] for x in range(len(A))]
    for r in range(len(A)):
        for c in range(len(A[0])):
            if r != row and c != col:
                result[r].append(A[r][c])
    
    for x in result:
        if x == []:
            result.remove(x)
    
    return result

def destructiveRemoveRowAndCol(A, row, col):
    return 42

def bestQuiz(a):
    return 42

def matrixAdd(L, M):
    return 42

def isMostlyMagicSquare(a):
    return 42

class DataTable(object):
    def __init__(self, csvString):
        self.table = []
        for line in csvString.splitlines():
            line = line.strip()
            if line != '':
                for i in range(1, len(self.table)):
                    for j in range(1, len(self.table[0])):
                        self.table[i][j] = int(self.table[i][j])
                row = line.split(',')
                self.table.append(row)
            
        for i in range(1, len(self.table)):
            for j in range(1, len(self.table[0])):
                self.table[i][j] = int(self.table[i][j])
    
    def getDims(self):
        return(len(self.table), len(self.table[0]))
    
    def getColumn(self, columnIndex):
        return DataColumn(self, columnIndex)

class DataColumn(object):
    def __init__(self, dataTable, columnIndex):
        self.label = dataTable.table[0][columnIndex]
        self.data = []
        for i in range(1, len(dataTable.table)):
            self.data.append(dataTable.table[i][columnIndex])
    
    def average(self):
        return sum(self.data)/len(self.data)


#################################################
# Test Functions
#################################################

def testNondestructiveRemoveRowAndCol():
    print('Testing nondestructiveRemoveRowAndCol()...', end='')
    a = [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]]
    aCopy = copy.copy(a)
    assert(nondestructiveRemoveRowAndCol(a, 1, 2) == [[2, 3, 5], [0, 1, 3]])
    assert(a == aCopy)
    assert(nondestructiveRemoveRowAndCol(a, 0, 0) == [[7, 6, 5], [1, 2, 3]])
    assert(a == aCopy)
    b = [[37, 78, 29, 70, 21, 62, 13, 54, 5],
    [6,     38, 79, 30, 71, 22, 63, 14, 46],
    [47,    7,  39, 80, 31, 72, 23, 55, 15],
    [16,    48, 8,  40, 81, 32, 64, 24, 56],
    [57,    17, 49, 9,  41, 73, 33, 65, 25],
    [26,    58, 18, 50, 1,  42, 74, 34, 66], 
    [67,    27, 59, 10, 51, 2,  43, 75, 35],
    [36,    68, 19, 60, 11, 52, 3,  44, 76],
    [77,    28, 69, 20, 61, 12, 53, 4,  45]]

    c = [[37, 78, 29, 70, 21, 62,     54, 5],
    [6,     38, 79, 30, 71, 22,     14, 46],
    [47,    7,  39, 80, 31, 72,     55, 15],
    [16,    48, 8,  40, 81, 32,     24, 56],
    [57,    17, 49, 9,  41, 73,     65, 25],
    [26,    58, 18, 50, 1,  42,     34, 66], 
    [67,    27, 59, 10, 51, 2,      75, 35],
    [36,    68, 19, 60, 11, 52, 44, 76]]

    bCopy = copy.copy(b)
    assert(nondestructiveRemoveRowAndCol(b,8,6) == c)
    assert(b == bCopy)
    print('Passed!')

def testDestructiveRemoveRowAndCol():
    print("Testing destructiveRemoveRowAndCol()...", end='')
    A = [ [ 2, 3, 4, 5],
          [ 8, 7, 6, 5],
          [ 0, 1, 2, 3]
        ]
    B = [ [ 2, 3, 5],
          [ 0, 1, 3]
        ]
    assert(destructiveRemoveRowAndCol(A, 1, 2) == None)
    assert(A == B) # but now A is changed!
    A = [ [ 1, 2 ], [3, 4] ]
    B = [ [ 4 ] ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    A = [ [ 1, 2 ] ]
    B = [ ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    print("Passed!")

def testBestQuiz():
    print('Testing bestQuiz()...', end='')
    a = [ [ 88,  80, 91 ],
          [ 68, 100, -1 ]]
    aCopy = copy.copy(a)
    assert(bestQuiz(a) == 2)
    assert(a == aCopy) # must be non-destructive!
    a = [ [ 88,  80, 80 ],
          [ 68, 100, 100 ]]
    assert(bestQuiz(a) == 1)
    a = [ [88, -1, -1 ],
          [68, -1, -1 ]]
    assert(bestQuiz(a) == 0)
    a = [ [-1, -1, -1 ],
          [-1, -1, -1 ]]
    assert(bestQuiz(a) == None)
    assert(bestQuiz([[]]) == None)
    print('Passed')

def testMatrixAdd():
    print('Testing matrixAdd()...', end='')
    L = [ [1,  2,  3],
          [4,  5,  6] ]
    M = [ [21, 22, 23],
          [24, 25, 26]]
    N = [ [1+21, 2+22, 3+23],
          [4+24, 5+25, 6+26]]
    lCopy = copy.copy(L)
    mCopy = copy.copy(M)
    assert(matrixAdd(L, M) == N)
    assert((L == lCopy) and (M == mCopy)) # must be non-destructive!
    assert(matrixAdd(L, [ [ 1, 2, 3] ]) == None) # dimensions mismatch
    print('Passed!')

def testIsMostlyMagicSquare():
    print("Testing isMostlyMagicSquare()...", end="")
    assert(isMostlyMagicSquare([[42]]) == True)
    assert(isMostlyMagicSquare([[2, 7, 6],
                                [9, 5, 1],
                                [4, 3, 8]]) == True)
    assert(isMostlyMagicSquare([[4-7, 9-7, 2-7],
                                [3-7, 5-7, 7-7],
                                [8-7, 1-7, 6-7]]) == True)
    a = [[7  ,12 ,1  ,14],
         [2  ,13 ,8  ,11],
         [16 ,3  ,10 ,5],
         [9  ,6  ,15 ,4]]
    assert(isMostlyMagicSquare(a))
    assert(isMostlyMagicSquare([[1, 2], [2, 1]]) == False) # bad diagonals!
    a = [[113**2, 2**2, 94**2],
         [ 82**2,74**2, 97**2],
         [ 46**2,127**2,58**2]]
    assert(isMostlyMagicSquare(a) == False) # it's close, but not quite!
    a = [[  35**2, 3495**2, 2958**2],
         [3642**2, 2125**2, 1785**2],
         [2775**2, 2058**2, 3005**2]]
    assert(isMostlyMagicSquare(a) == False) # ditto!
    print("Passed!")

def testDataTableAndDataColumnClasses():
    print('Testing DataTable and DataColumn classes...', end='')
    csvData = '''
    Name,Hw1,Hw2,Quiz1,Quiz2
    Fred,94,88,82,92
    Wilma,98,80,80,100
    '''
    dataTable = DataTable(csvData)
    rows, cols = dataTable.getDims()
    assert((rows == 3) and (cols == 5))

    column3 = dataTable.getColumn(3)
    assert(isinstance(column3, DataColumn))
    assert(column3.label == 'Quiz1')
    assert(column3.data == [82, 80])
    assert(almostEqual(column3.average(), 81))

    column4 = dataTable.getColumn(4)
    assert(isinstance(column4, DataColumn))
    assert(column4.label == 'Quiz2')
    assert(column4.data == [92, 100])
    assert(almostEqual(column4.average(), 96))

    column0 = dataTable.getColumn(0)
    assert(isinstance(column0, DataColumn))
    assert(column0.label == 'Name')
    assert(column0.data == ['Fred', 'Wilma'])

    print('Passed!')

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
    if (magicCode%2 >= 0): requiredFns += '  nondestructiveRemoveRowAndCol\n'
    if (magicCode%37 + 2*magicCode%20 > 80):
        requiredFns += '  bestQuiz\n'
        requiredFns += '  matrixAdd\n  isMostlyMagicSquare\n'
    else:
        requiredFns += '  dataTableAndDataColumnClasses'
    return requiredFns

# DO NOT MODIFY THIS FUNCTION!!!!
def testAll():
    # DO NOT MODIFY THIS FUNCTION!!!!
    requiredFns = getRequiredFunctions()
    print('************************************')
    print('Testing these functions:')
    print(requiredFns)
    print('************************************')
    if ('nondestructiveRemoveRowAndCol' in requiredFns):
        testNondestructiveRemoveRowAndCol()
    if ('DestructiveRemoveRowAndCol' in requiredFns):
        testDestructiveRemoveRowAndCol()
    if ('bestQuiz' in requiredFns):
        testBestQuiz()
    if ('matrixAdd' in requiredFns):
        testMatrixAdd()
    if ('isMostlyMagicSquare' in requiredFns):
        testIsMostlyMagicSquare()
    if ('dataTableAndDataColumnClasses' in requiredFns):
        testDataTableAndDataColumnClasses()
    print('*** Done with all tests!')

def main():
    cs112_f19_week5_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
