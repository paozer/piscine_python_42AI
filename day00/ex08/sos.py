import sys
import string

dict = {
        'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

if __name__ == "__main__":
    tokens = []
    for i in range(1, len(sys.argv)):
        str = sys.argv[i].upper().split()
        if str != [s for s in str if s.isalnum()]:
            print ('ERROR')
            exit()
        tokens += str
    ret = ''
    for token in tokens:
        ret += ' '.join(dict.get(i, '') for i in token)
        if token != tokens[len(tokens) - 1]:
            ret += ' / '
    print(ret)
