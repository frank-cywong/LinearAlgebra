import numpy as np

def gen_elementary_matrix():
    size = input("Input new elementary matrix size: ");
    try:
        size = int(size)
    except:
        print("Error! Size {} is not a number!".format(size))
        return
    A = np.eye(size)
    op = input("Input operation `swap`, `scale`, or `add`: ")
    if(op == "swap"):
        argstr = input("Input two rows (1-indexed) to swap, separated by spaces eg. `1 3`: ");
        argli = argstr.split(" ");
        if(len(argli) < 2):
            print("Error! {} has no spaces!".format(argstr));
            return;
        try:
            arg1 = int(argli[0])
        except:
            print("Error! arg1 {} is not a number!".format(argli[0]));
        try:
            arg2 = int(argli[1])
        except:
            print("Error! arg2 {} is not a number!".format(argli[1]));
        if(arg1 > size or arg2 > size or arg1 <= 0 or arg2 <= 0):
            print("Error! arg1 {} and/or arg2 {} out of bounds! Size is {} and values are 1-indexed.".foramt(arg1, arg2, size));
            return
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
            print("Error! arg1 [row] {} is not a number!".format(argli[0]));
        argstr = input("Input scalar to scale by: ");
        try:
            arg2 = int(argstr)
        except:
            print("Error! arg2 [scalar] {} is not a number!".format(argli[1]));
        if(arg1 > size or arg1 <= 0):
            print("Error! arg1 {} (row number) is out of bounds! Size is {} and values are 1-indexed.".foramt(arg1, size));
            return
        A[arg1-1][arg1-1] = arg2;
        return A
    elif (op == "add"):
        pass
    else:
        print("Error! Operation {} is not valid!".format(op));
        return

R = gen_elementary_matrix()
print("Returned elementary matrix:\n", R);
