# Intro to Matrix Multiplication
# A starter for exploring matrix multiplication

# Import the csv module for handling data
import csv

# Makes presenting a table of data easier
from tabulate import tabulate

# The matrix M is encoded as a list of lists
# Recall that the nested lists serve as the rows of the matrix

row_1 = [3, -4, 0, 5]
row_2 = [-1, -2, 3, 10]
row_3 = [4, 1, 1.2, 3]

M = [ row_1, row_2, row_3]

# We'll import the matrix N from a file using the CSV library
# Recall: This reads in the comma separated-values as a list of lists of strings
#                                               Each line is a list

with open("matrix.txt") as f:
  reader = csv.reader(f)
  N = list(reader)

# By default lists have strings as entries, so convert them to floats
for i in range(len(N)):
  for j in range(len (N[i])):
    N[i][j]=float(N[i][j])
    
print("Matrix M:")
print(tabulate(M))
print("\n")
print("Matrix N:")
print(tabulate(N))
print("\n")


# Challenge 1
# Write a function that returns the dimensions of a matrix


# Returns the dimensions of matrix A as a tuple (number of rows, number of columns)
def matrix_dimensions(A):
  num_rows = len(A)
  num_cols = len(A[0])
  return((num_rows,num_cols))


# Challenge 2
# Write a function that determines if two matrices can be multiplied

# Returns True or False
def can_multiply_matrices(A,B):
  if (len(A[0])==len(B)):
    return True
  else:
    return False

# Challenge 3
# Write a function that determines the entry in row i, column j of the matrix product A*B 

# Returns the entry in row i, column j of the matrix product A*B

def matrix_product_entry(A,B,i,j):

  # Should probably check first to see if the matrices can be multiplied!
    o = 0.0;
    if(not can_multiply_matrices(A,B)):
        raise Exception("Cannot multiply matrices of these dimensions")
    for k in range(len(B)): # for (int k = 0; k < len(B); ++k)
        o += A[i][k] * B[k][j];
    return o;


# Challenge 4
# Write a function that multiplies two matrices A and B

# Returns the matrix product

def matrix_product(A,B):

    # Should probably check first to see if the matrices can be multiplied!

    # Initialize a new empty list for your row lists 
    P = []
    # Use matrix_product_entry!

    if(not can_multiply_matrices(A,B)):
        raise Exception("Cannot multiply matrices of these dimensions")
    for i in range(len(A)):
        P.append([]);
        for j in range(len(B[0])):
            P[i].append(matrix_product_entry(A,B,i,j));

    return P

# Challenge 5
# Write a function that transposes a matrix
  
def matrix_transpose(A):
  
  M = []
  for i in range(len(A[0])):
    M.append([]);
    for j in range(len(A)):
        M[i].append(A[j][i]);
  return M

# Challenge 5+
# Find ij-th entry of A^3 without computing all of A^3
# Step 1: Find i-th row of A^2
# Step 2: Mult to get ij-th entry of A^3
def matrix_cube_entry(A,i,j):
    A2 = [];
    for k in range(len(A)):
        # find ik-th entry of A^2
        A2.append(matrix_product_entry(A,A,i,k))
    #ij-th entry of A^3 = ij-th entry of A^2*A = 0-j-th entry of (i-th row of A^2 * A)
    return (matrix_product_entry([A2], A, 0, j));


print("Matrix NM:")
O = matrix_product(N,M);
print(tabulate(O));
print("\n");

print("Matrix Mt:")
print(tabulate(matrix_transpose(M)));
print("\n");

print("Matrix N^2:")
N2 = matrix_product(N,N);
print(tabulate(N2));

print("Matrix N^3:")
N3 = matrix_product(N2, N);
print(tabulate(N3));

print("Quick computation of 1,2-th entry (0-indexed) of N^3:")
print(matrix_cube_entry(N, 1, 2));
