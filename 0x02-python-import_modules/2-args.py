#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number = len(argv)
    if len(argv) == 1:
        print("{:d} .".format(len(argv)))
    elif len(argv) == 2:
        print("{:d} argument:".format(len(argv - 1)))
    else:
        print("{:d} arguments:".format(len(argv - 1)))
        
        for i in range(1, number):
            print("{:d}: {:d}".format(i, (argv[i])))
            

   
