import numpy as np
import tabulate
import csv

# Generates elementary matrix from row op
from elem import gen_elementary_matrix

CurInv = None;
RowCount = 0;

# Previously written RREF - from matrices.py
def integerCheck(x):
    try:
        return(int(x))
    except:
        raise ValueError("Input must be an integer")

def floatCheck(x):
    try:
        return(float(x))
    except:
        raise ValueError("Input must be an number")

def scale(A, r, s):
    print("Scale {} {}".format(r, s));
    global CurInv;
    global RowCount;
    r = integerCheck(r)
    s = floatCheck(s)
    if(r >= len(A)):
        raise ValueError("Row number too large")
    for i in range(len(A[r])):
        A[r][i] *= s;
    E = gen_elementary_matrix(False, [RowCount, "scale", r + 1, s]);
    #print("Generated elementary matrix:\n", E);
    CurInv = E@CurInv;
    #print("CurInv is now:\n", CurInv);

def swap(A, i, j):
    print("swap {} {}".format(i, j));
    global CurInv;
    global RowCount;
    i = integerCheck(i)
    j = integerCheck(j)
    if(i >= len(A) or j >= len(A)):
        raise ValueError("Row number too large")
    for col in range(len(A[0])):
        temp = A[i][col]
        A[i][col] = A[j][col]
        A[j][col] = temp
    E = gen_elementary_matrix(False, [RowCount, "swap", i + 1, j + 1]);
    CurInv = E@CurInv;

# Add a scalar multiple of row j to row i
def addMult(A, i, j, s):
    print("add {} {} {}".format(i, j, s));
    global CurInv;
    global RowCount;
    i = integerCheck(i)
    j = integerCheck(j)
    s = floatCheck(s)
    if(i >= len(A) or j >= len(A)):
        raise ValueError("Row number too large")
    for k in range(len(A[i])):
        A[i][k] += s * A[j][k]
    E = gen_elementary_matrix(False, [RowCount, "add", i + 1, j + 1, s]);
    CurInv = E@CurInv;

def setVal(A, i, j, s):
    i = integerCheck(i)
    j = integerCheck(j)
    s = floatCheck(s)
    if(i >= len(A) or j >= len(A[i])):
        raise ValueError("Row or column number too large")
    A[i][j] = s

def print_row(A, r):
    r = integerCheck(r)
    if(r >= len(A)):
        raise ValueError("Row number too large")
    o = "["
    for i in range(len(A[r])):
        if(i != 0):
            o += ", "
        o += str(A[r][i])
    o += "]"
    print(o)

def rowReduce(N):
    curStartRow = 0
    for col in range(len(N[0])):
        useRow = -1
        for row in range(curStartRow, len(N)):
            if(N[row][col] != 0.0):
                #print("Userow: {}".format(row));
                useRow = row
                break
        if(useRow == -1):
            continue
        swap(N, useRow, curStartRow)
        #print(N);
        scale(N, curStartRow, 1.0 / N[curStartRow][col])
        #print(N);
        for row in range(len(N)):
            if(row != curStartRow):
                addMult(N, row, curStartRow, -1.0 * N[row][col])
                #print(N);
        #print(tabulate(N))
        curStartRow += 1
# END previously written rref

# CODE FROM inverses.py

# import a matrix M from a CSV text file
with open("M_matrix.txt") as f:
  reader = csv.reader(f)
  d = list(reader)

M = np.array(d,dtype=float)
M_copy = np.array(d,dtype=float)
print("M read in as:\n", M);
RowCount = np.shape(M)[0]
CurInv = np.eye(RowCount)

# END CODE FROM inverses.py

rowReduce(M);
print("After row reduction, M is now:\n");
print(M);
print("Computed inverse for RREF:\n");
print(CurInv);
print("Checking (original) M*CurInv:\n", M_copy@CurInv);
