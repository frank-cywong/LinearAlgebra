import numpy as np

def gen_elementary_matrix():
    size = input("Input new elementary matrix size: ");
    try:
        size = int(size)
    except:
        print("Error! Size {} is not a number!".format(size))
        return None
    A = np.eye(size)
    op = input("Input operation `swap`, `scale`, or `add`: ")
    if(op == "swap"):
        argstr = input("Input two rows (1-indexed) to swap, separated by spaces eg. `1 3`: ");
        argli = argstr.split(" ");
        if(len(argli) < 2):
            print("Error! {} has no spaces!".format(argstr));
            return None;
        try:
            arg1 = int(argli[0])
        except:
            print("Error! arg1 {} is not a number!".format(argli[0]));
            return None
        try:
            arg2 = int(argli[1])
        except:
            print("Error! arg2 {} is not a number!".format(argli[1]));
            return v
        if(arg1 > size or arg2 > size or arg1 <= 0 or arg2 <= 0):
            print("Error! arg1 {} and/or arg2 {} out of bounds! Size is {} and values are 1-indexed.".format(arg1, arg2, size));
            return None
        A[arg1-1][arg1-1] = 0
        A[arg2-1][arg2-1] = 0
        A[arg1-1][arg2-1] = 1
        A[arg2-1][arg1-1] = 1
        return A
    elif (op == "scale"):
        argstr = input("Input row to scale: ");
        try:
            arg1 = int(argstr)
        except:
            print("Error! arg1 [row] {} is not a number!".format(argstr));
            return None
        argstr = input("Input scalar to scale by: ");
        try:
            arg2 = int(argstr)
        except:
            print("Error! arg2 [scalar] {} is not a number!".format(argstr));
            return None
        if(arg1 > size or arg1 <= 0):
            print("Error! arg1 {} (row number) is out of bounds! Size is {} and values are 1-indexed.".format(arg1, size));
            return None
        A[arg1-1][arg1-1] = arg2;
        return A
    elif (op == "add"):
        argstr = input("Input destination row (row that is modified): ");
        try:
            arg1 = int(argstr)
        except:
            print("Error! arg1 [dest row] {} is not a number!".format(argstr));
            return None
        argstr = input("Input source row (row that you are adding a multiple of): ");
        try:
            arg2 = int(argstr)
        except:
            print("Error! arg2 [source row] {} is not a number!".format(argstr));
            return None
        argstr = input("Input scalar to scale by: ");
        try:
            arg3 = int(argstr)
        except:
            print("Error! arg3 [scalar] {} is not a number!".format(argstr));
            return None
        if(arg1 > size or arg1 <= 0 or arg2 > size or arg2 <= 0):
            print("Error! arg1 {} (dest) and/or arg2 {} (source) is out of bounds! Size is {} and values are 1-indexed.".format(arg1, arg2, size));
            return None
        A[arg1-1][arg2-1] = arg3;
        return A
    else:
        print("Error! Operation {} is not valid!".format(op));
        return None

R = gen_elementary_matrix()
if(R is not None):
    print("Returned elementary matrix:\n", R);
else:
    print("gen_elementary_matrix returned None");
