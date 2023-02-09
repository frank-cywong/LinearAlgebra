import numpy as np

def gen_elementary_matrix(use_stdin, args = []):
    if use_stdin:
        size = input("Input new elementary matrix size: ");
    else:
        if(len(args) == 0):
            print("Error! Not enough args!");
            return None;
        size = args.pop(0);
    try:
        size = int(size)
    except:
        print("Error! Size {} is not a number!".format(size))
        return None
    A = np.eye(size)
    if use_stdin:
        op = input("Input operation `swap`, `scale`, or `add`: ");
    else:
        if(len(args) == 0):
            print("Error! Not enough args!");
            return None;
        op = args.pop(0);
    if(op == "swap"):
        if use_stdin:
            argstr = input("Input two rows (1-indexed) to swap, separated by spaces eg. `1 3`: ");
            argli = argstr.split(" ");
        else:
            if(len(args) < 2):
                print("Error! Not enough args!");
                return None;
            argtmp = args.pop(0);
            argli = [];
            argli.append(argtmp);
            argtmp = args.pop(0);
            argli.append(argtmp);
            argstr = "";
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
        if use_stdin:
            argstr = input("Input row to scale: ");
        else:
            if(len(args) == 0):
                print("Error! Not enough args!");
                return None;
            argstr = args.pop(0);
        try:
            arg1 = int(argstr)
        except:
            print("Error! arg1 [row] {} is not a number!".format(argstr));
            return None
        if use_stdin:
            argstr = input("Input scalar to scale by: ");
        else:
            if(len(args) == 0):
                print("Error! Not enough args!");
                return None;
            argstr = args.pop(0);
        try:
            arg2 = float(argstr)
        except:
            print("Error! arg2 [scalar] {} is not a number!".format(argstr));
            return None
        if(arg1 > size or arg1 <= 0):
            print("Error! arg1 {} (row number) is out of bounds! Size is {} and values are 1-indexed.".format(arg1, size));
            return None
        A[arg1-1][arg1-1] = arg2;
        return A
    elif (op == "add"):
        if use_stdin:
            argstr = input("Input destination row (row that is modified): ");
        else:
            if(len(args) == 0):
                print("Error! Not enough args!");
                return None;
            argstr = args.pop(0);
        try:
            arg1 = int(argstr)
        except:
            print("Error! arg1 [dest row] {} is not a number!".format(argstr));
            return None
        if use_stdin:
            argstr = input("Input source row (row that you are adding a multiple of): ");
        else:
            if(len(args) == 0):
                print("Error! Not enough args!");
                return None;
            argstr = args.pop(0);
        try:
            arg2 = int(argstr)
        except:
            print("Error! arg2 [source row] {} is not a number!".format(argstr));
            return None
        if use_stdin:
            argstr = input("Input scalar to scale by: ");
        else:
            if(len(args) == 0):
                print("Error! Not enough args!");
                return None;
            argstr = args.pop(0);
        try:
            arg3 = float(argstr)
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

def main():
    R = gen_elementary_matrix(True)
    if(R is not None):
        print("Returned elementary matrix:\n", R);
    else:
        print("gen_elementary_matrix returned None");

# Boilerplate to make Python behave more like C or Java by making it have a main function - also makes import work as expected
if __name__ == "__main__":
    main()
