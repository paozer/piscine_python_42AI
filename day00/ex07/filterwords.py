import sys
import string

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERROR")
        exit()

    try:
        lim = int(sys.argv[2])
    except ValueError:
        print("ERROR")
        exit()

    string = ''.join(c for c in sys.argv[1] if c not in string.punctuation)
    tokens = [s for s in string.split() if len(s) > lim]
    print(tokens)
