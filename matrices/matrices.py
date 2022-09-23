# Matrices as Lists of Lists
# A simple introduction to handling matrices as lists of lists in Python
# Patrick Honner 9/21/22

# Need this to deepcopy lists
import copy

# Makes presenting a table of data easier
from tabulate import tabulate

# We'll hardcode the matrix as a list of lists
# The nested lists function as the rows of the matrix

row_1 = [3, -4, 0, 5]
row_2 = [-1, -2, 3, 10]
row_3 = [4, 1, 1, 3]

M = [ row_1, row_2, row_3]

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
    r = integerCheck(r)
    s = floatCheck(s)
    if(r >= len(A)):
        raise ValueError("Row number too large")
    for i in range(len(A[r])):
        A[r][i] *= s;

def swap(A, i, j):
    i = integerCheck(i)
    j = integerCheck(j)
    if(i >= len(A) or j >= len(A)):
        raise ValueError("Row number too large")
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# Add a scalar multiple of row j to row i
def addMult(A, i, j, s):
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
            if(N[row][col] != 0):
                useRow = row
                break
        if(useRow == -1):
            continue
        swap(N, useRow, curStartRow)
        scale(N, curStartRow, 1.0 / N[curStartRow][col])
        for row in range(len(N)):
            if(row != curStartRow):
                addMult(N, row, curStartRow, -1.0 * N[row][col])
        #print(tabulate(N))
        curStartRow += 1
        

def print_help():
    print("- p to print the current matrix")
    print("- pr [row] to print a row")
    #print("- pc [row] to print a column")
    print("- s [row] [col] [val] to set a value")
    print("- add [row1] [row2] [scalar] to add scalar * row2 to row1")
    print("- scale [row] [scalar] to scale row by scalar")
    print("- swap [row1] [row2] to swap row 1 and row 2")
    print("- r to reduce to reduced row echelon form")
    print("- reset to reset to the default matrix")

print("Here is matrix M shown as a table in Python:\n")
print(tabulate(M))


# Create a new copy of the matrix
# deepcopy creates a copy of values, not a copy of references

N = copy.deepcopy(M)

while(True):
    instr = input("\nInput mode, type h for help, q to quit: ");
    args = instr.split(' ')
    instr = args.pop(0)
    #print(args)
    try:
        if(instr == 'h'):
            print_help()
        elif(instr == 'q'):
            break;
        elif(instr == 'p'):
            print(tabulate(N))
        elif(instr == 'pr'):
            print_row(N, args[0])
        elif(instr == 's'):
            setVal(N, args[0], args[1], args[2])
        elif(instr == 'add'):
            addMult(N, args[0], args[1], args[2])
        elif(instr == 'scale'):
            scale(N, args[0], args[1])
        elif(instr == 'swap'):
            swap(N, args[0], args[1])
        elif(instr == 'r'):
            rowReduce(N)
        elif(instr == 'reset'):
            N = copy.deepcopy(M)
        else:
            print("Invalid input")
    except Exception as e:
        print(e)

'''
print(tabulate(N))

scale(N, 0, 3)

print(tabulate(N))

swap(N, 1, 2)

print(tabulate(N))

addMult(N, 0, 2, 9)

print(tabulate(N))

scale(N, 0, 1.0 / 3.0)

print(tabulate(N))
'''

'''

# Ask user to perform an elementary row operation
row_choice = input("Choose a row to multiply by a scalar:  ")
scalar = input("Enter a scalar to multiply by:  ")

# Convert row_choice to the appropriate index for the list
row = int(row_choice) - 1
# Convert the string input to a float
scalar = float(scalar)

# Perform the elementary row operation
for i in range(len(N[row])):
  N[row][i]=scalar*N[row][i]

print("Here is the new matrix:")
print(tabulate(N))



# A function to print out a list of lists, i.e. a matrix
# tabulate is nicer, so I didn't use this, but left as an example
def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      # M[i][j] is the jth entry in the ith list
      # in other words, it's exactly the ij-th entry in the matrix M
      print (A[i][j], "\t", end="")
    print("\n")

'''
