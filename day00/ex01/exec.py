import sys

if len(sys.argv) < 2:
    exit()
for arg in sys.argv[::-1][:-1:]:
    print(arg.swapcase()[::-1], end=' ')
print()
