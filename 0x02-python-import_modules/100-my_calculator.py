#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from sys import exit
    from calculator_1 import add, sub, mul, div
    argv = sys.argv
    n = len(argv)

    error = "Unknown operator. Available operators:"
    if n < 4 or n > 4:
        exit("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]
        if op == "+":
            print("{} {} {} = {}".format(a, op, b, add(a, b)))
        elif op == "-":
            print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        elif op == "*":
            print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        elif op == "/":
            print("{} {} {} = {}".format(a, op, b, div(a, b)))
        else:
            exit("{} +, -, * and /".format(error))
