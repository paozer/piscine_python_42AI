import sys

if len(sys.argv) == 1:
    exit()
elif len(sys.argv) > 2:
    print("ERROR")
    exit()

try:
    nbr = int(sys.argv[1])
except ValueError:
    print("ERROR")
    exit()

if nbr == 0:
    print("I'm Zero.")
elif nbr % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
