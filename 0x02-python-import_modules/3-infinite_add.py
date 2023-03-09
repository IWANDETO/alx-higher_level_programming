#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    counter = len(sys.argv)
    sum = 0
    if counter == 1:
        print("0")
    else:
        for i in range(1, counter):
            sum += (int(sys.argv[i]))
    print(sum)
