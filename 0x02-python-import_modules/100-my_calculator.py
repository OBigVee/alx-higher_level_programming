#!/usr/bin/python3
""" """
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    n_arg = len(sys.argv)
    info = "Available operators: +, -, * and /"
    if n_arg == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operators = [("+", add), ("-", sub), ("*", mul), ("/", div)]

        for op in operators:
            if sys.argv[2] == op[0]:
                result = op[1](a, b)
                print("{} {} {} = {}".format(a, op[0], b, result))
                sys.exit()
        print("Unknown operator. {:s}".format(info))
        sys.exit(1)
    else:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
