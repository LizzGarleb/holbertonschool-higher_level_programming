#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, mul, div, sub
    import sys

    ac = len(sys.argv)

    if ac != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    ope = "+-*/"
    a = int(sys.argv[1])
    input_ope = sys.argv[2]
    b = int(sys.argv[3])

    if input_ope == '+':
        result = a + b
        print("{} {} {} = {}".format(a, input_ope, b, result))
    elif input_ope == '-':
        result = a - b
        print("{} {} {} = {}".format(a, input_ope, b, result))
    elif input_ope == '*':
        result = a * b
        print("{} {} {} = {}".format(a, input_ope, b, result))
    elif input_ope == '/':
        result = a / b
        print("{} {} {} = {}".format(a, input_ope, b, int(result)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
