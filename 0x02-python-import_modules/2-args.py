#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number = len(argv)
    if len(argv) == 1:
        print("{:d} .".format(number))
    elif len(argv) == 2:
        print("{:d} argument:".format(number - 1))
    else:
        print("{:d} arguments:".format(number - 1))
    for i in range(1, number):
        print("{:d}: {:s}".format(i, (argv[i])))
