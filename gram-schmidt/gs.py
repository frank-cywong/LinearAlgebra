from rref import rowReduce # Custom RREF from previous work
from math import sqrt # Python STL 

EPSILON = 1.0e-9

def matrixCopy(m):
    o = [];
    for a in m:
        r = [];
        for e in a:
            r.append(e);
        o.append(r);
    return o;

def vectorCopy(v):
    o = [];
    for i in v:
        o.append(i);
    return o;

def norm(v):
    counter = 0.0;
    for x in v:
        counter += (x * x);
    return(sqrt(counter));

def normalize(v):
    n = norm(v);
    for i in range(len(v)):
        v[i] /= n;

def printVector(v):
    print("[", end="");
    first = True;
    for x in v:
        if(not first):
            print(", ", end="");
        print(x, end="");
        first = False;
    print("]");

def printBasis(b):
    print("Basis size:", len(b));
    for v in b:
        printVector(v);

def basisCheck(b):
    rowCount = len(b);
    colCount = len(b[0]);
    if(rowCount > colCount):
        print("Error! Too many vectors for set to be a basis!");
        return False;
    m = matrixCopy(b);
    rowReduce(m);
    #printBasis(m);
    lastRow = m[rowCount - 1];
    for i in lastRow:
        if(i > EPSILON or i < -EPSILON):
            return True;
    print("Error! Basis is dependent as there's a all zeros row after row-reduction!");
    print("Row-reduced basis:");
    printBasis(m);
    return False;

# Adds v to u, modifies u
def vectorAdd(u, v):
    #print("ADD");
    #printVector(u);
    #printVector(v);
    if(len(u) != len(v)):
        print("Error! Trying to add vector u with size {} and vector v with size {}!".format(len(u), len(v)));
        return;
    for i in range(len(u)):
        u[i] += v[i];

# Scales u by m, modifies u
def vectorScale(m, u):
    for i in range(len(u)):
        u[i] *= m;

def dotProduct(u, v):
    if(len(u) != len(v)):
        print("Error! Trying to add vector u with size {} and vector v with size {}!".format(len(u), len(v)));
        return;
    s = 0;
    for i in range(len(u)):
        s += (u[i] * v[i]);
    return s;

def gramSchmidt(b):
    if not basisCheck(b):
        return None;
    n = [];
    for v in b:
        #printBasis(n);
        u = vectorCopy(v);
        for ev in n:
            t = vectorCopy(ev);
            vectorScale(-dotProduct(u, ev), t);
            vectorAdd(u, t);
        normalize(u);
        n.append(u);
    return n;

def printHelp():
    print("Commands:");
    print("help: Prints this help message");
    print("clear: Clears the basis");
    print("add: Adds a vector to the basis");
    print("gram-schmidt: Generates and prints an orthonormal basis based on current basis with the Gram-Schmidt algorithm");
    print("exit: Exits the program");
    print("");

def addVect(b):
    sanityCheck = (False if len(b) == 0 else True);
    print("NOTE: Input vectors with brackets, eg. 3 -1 4.1");
    print("Input vector", end="");
    if(sanityCheck):
        print(" of size", len(b[0]), end="");
    print(" to add to basis:");
    vin = input();
    varr = vin.split(" ");
    darr = [];
    for q in varr:
        try:
            darr.append(float(q));
        except ValueError:
            print("Error! One of your values ({}) could not be parsed as a number, please retry.".format(q));
            return;
    if(sanityCheck):
        if(len(darr) != len(b[0])):
            print("Error! Inputted vector has size {}, expected size {} to match size of vectors in basis.".format(len(darr), len(b[0])));
            return;
    b.append(darr);

def main():
    basis = [];
    printHelp();
    while True:
        print("Current basis:");
        printBasis(basis);
        print("");
        cmd = input("Input Command: ");
        if(cmd == "help"):
            printHelp();
        elif(cmd == "clear"):
            basis = [];
        elif(cmd == "add"):
            addVect(basis);
        elif(cmd == "gram-schmidt"):
            gb = gramSchmidt(basis);
            if gb is not None:
                print("Orthonormal basis found:");
                printBasis(gb);
                print("\n");
        elif(cmd == "exit"):
            break;
        else:
            print("Command not recognized! Type `help` to get a list of commands.");

if __name__ == "__main__":
    main();
