#!/usr/bin/python3
import sys

if __name__ == "__main__":
    n = len(sys.argv)
    if n == 1:
        print("0")
    elif n == 2:
        print("What should I add {} to?".format(sys.argv[1]))
    else:
        sum = 0
        for x in range(1, n):
            try:
                sum += int(sys.argv[x])
            except ValueError:
                print("{} is not a valid number".format(sys.argv[x]))
        print("{}".format(sum))
