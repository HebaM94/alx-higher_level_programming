#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argsc = len(sys.argv) - 1
    if argsc == 0:
        print("{} arguments.".format(argsc))
    elif argsc == 1:
        print("{} argument:".format(argsc))
    else:
        print("{} arguments:".format(argsc))
    for i in range(argsc):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
