import sys


def operations(a, b):
    if b == 0:
        return a + b, a - b, a * b, "Error (div by zero)",\
                "Error (modulo by zero)"
    return a + b, a - b, a * b, a / b, a % b


err_flag = 0

if len(sys.argv) == 3:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except ValueError:
        print("InputError: only numbers\n")
        err_flag = 1
elif len(sys.argv) > 3:
    print("InputError: too many arguments\n")
    err_flag = 1

if len(sys.argv) < 3 or err_flag:
    print("Usage: python operations.py <number1> <number2>\n")
    print("Example:\npython operations.py 10 3")
    exit()

add, diff, mul, div, mod = operations(a, b)
print('Sum:\t\t{}\nDifference:\t{}\nProduct:\t{}\nQuotient:\t{}\nRemainder:\
        \t{}'.format(add, diff, mul, div, mod))
