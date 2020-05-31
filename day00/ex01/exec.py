import sys

rev = sys.argv[::-1]
for arg in rev[:-1:]:
    print(arg.swapcase()[::-1])
