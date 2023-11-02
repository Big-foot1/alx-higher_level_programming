#!/usr/bin/python3
from sys import argv


def main():
    arg_num = len(argv)
    if arg_num == 1:
        print("{} arguments.".format(arg_num-1))
    elif arg_num == 2:
        print("{} argument:".format(arg_num-1))
    else:
        print("{} arguments:".format(arg_num-1))
    for i in range(arg_num):
        if i == 0:
            continue
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
