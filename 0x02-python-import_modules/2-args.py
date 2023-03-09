#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    counter = len(argv)
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("{:d} argument:".format(counter - 1))
    else:
        print("{:d} arguments:".format(counter - 1))
    for i in range(1, counter):
        print("{:d}: {:s}".format(i, (argv[i])))
