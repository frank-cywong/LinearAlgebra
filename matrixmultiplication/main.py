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
    

print(tabulate(M))
print("\n")
print(tabulate(N))
print("\n")


# Challenge 1
# Write a function that returns the dimensions of a matrix


# Returns the dimensions of matrix A as a tuple (number of rows, number of columns)
def matrix_dimensions(A):
  num_rows = 0
  num_cols = 0
  return((num_rows,num_cols))


# Challenge 2
# Write a function that determines if two matrices can be multiplied

# Returns True or False
def can_multiply_matrices(A,B):
  if (0==0):
    return True
  else:
    return False

# Challenge 3
# Write a function that determines the entry in row i, column j of the matrix product A*B 

# Returns the entry in row i, column j of the matrix product A*B

def matrix_product_entry(A,B,i,j):

  # Should probably check first to see if the matrices can be multiplied!
  return 0


# Challenge 4
# Write a function that multiplies two matrices A and B

# Returns the matrix product

def matrix_product(A,B):

  # Should probably check first to see if the matrices can be multiplied!

  # Initialize a new empty list for your row lists 
  P = []
  # Use matrix_product_entry!

  return P

# Challenge 5
# Write a function that transposes a matrix
  
def matrix_transpose(A):
  
  M = []
  return M

