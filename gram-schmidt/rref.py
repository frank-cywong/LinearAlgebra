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
    #print("Scale {} {}".format(r, s));
    global CurInv;
    global RowCount;
    r = integerCheck(r)
    s = floatCheck(s)
    if(r >= len(A)):
        raise ValueError("Row number too large")
    for i in range(len(A[r])):
        A[r][i] *= s;

def swap(A, i, j):
    #print("swap {} {}".format(i, j));
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

# Add a scalar multiple of row j to row i
def addMult(A, i, j, s):
    #print("add {} {} {}".format(i, j, s));
    global CurInv;
    global RowCount;
    i = integerCheck(i)
    j = integerCheck(j)
    s = floatCheck(s)
    if(i >= len(A) or j >= len(A)):
        raise ValueError("Row number too large")
    for k in range(len(A[i])):
        A[i][k] += s * A[j][k]

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
