import string


def text_analyzer(*args):
    """Count and display upper/lowercase, punctuation and whitespace counts."""
    if len(args) > 1:
        print("ERROR")
        return
    elif len(args) == 0:
        text = input("What is the text to analyse ?\n")
    else:
        text = args[0]
    upper = lower = punct = space = 0
    for char in text:
        if char in string.ascii_uppercase:
            upper += 1
        elif char in string.ascii_lowercase:
            lower += 1
        elif char in string.punctuation:
            punct += 1
        elif char in string.whitespace:
            space += 1
    print()
    print(f'The text contains {len(text)} characters:')
    print(f'- {upper} upper letters')
    print(f'- {lower} lower letters')
    print(f'- {punct} punctuation marks')
    print(f'- {space} spaces')
