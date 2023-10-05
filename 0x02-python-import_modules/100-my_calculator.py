#!/usr/bin/python3
import sys
import calculator_1

if __name__ == "__main__":
    n = len(sys.argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a, opr, b = sys.argv[1], sys.argv[2], sys.argv[3]
    a = int(a)
    b = int(b)
    if opr == '+':
        print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    elif opr == '-':
        print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    elif opr == '*':
        print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    elif opr == '/':
        print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
